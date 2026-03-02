import Foundation
import SwiftUI

// MARK: - AppState

/// Codable model capturing all restorable app state.
///
/// Add fields for each piece of UI state you want to persist
/// across app launches and background termination.
///
/// Usage:
/// ```swift
/// var state = AppState()
/// state.selectedTab = 2
/// state.navigationPathData = try? JSONEncoder().encode(path.codable)
/// ```
struct AppState: Codable, Sendable {
    /// Currently selected tab index or tag.
    var selectedTab: Int = 0

    /// Encoded NavigationPath data for restoration.
    /// Use `NavigationPath.CodableRepresentation` to encode/decode.
    var navigationPathData: Data?

    /// Scroll positions keyed by scroll view identifier.
    /// Maps a scroll view ID string to the ID of the item at the top.
    var scrollPositions: [String: String] = [:]

    /// Form draft values keyed by form ID, then field key.
    /// Cleared when the form is successfully submitted.
    var formDrafts: [String: [String: String]] = [:]

    /// Timestamp of the last successful save.
    /// Used for time-limited restore behavior.
    var lastSavedDate: Date = .distantPast

    /// State schema version for migration support.
    /// Increment when making breaking changes to this struct.
    var stateVersion: Int = 1
}

// MARK: - StateStorageMethod

/// Storage backend for state persistence.
enum StateStorageMethod {
    /// Persist to a JSON file in Application Support.
    case file(directory: URL? = nil)

    /// Persist to UserDefaults with a given suite name.
    case userDefaults(suiteName: String? = nil)
}

// MARK: - RestoreBehavior

/// Controls when saved state is restored.
enum RestoreBehavior {
    /// Always restore saved state on launch.
    case always

    /// Restore only if the state was saved within the given number of minutes.
    case timeLimited(minutes: Int)

    /// Show a prompt asking the user whether to restore.
    case askUser
}

// MARK: - StateRestorationManager

/// Central manager for saving and restoring app state.
///
/// Observes state changes and auto-saves with debouncing.
/// Restores state on initialization based on the configured behavior.
///
/// `@MainActor` is required: `@Observable` property mutations and the debounced
/// `Task` inside `scheduleSave()` both write to stored properties from concurrent
/// contexts. Isolating to the main actor eliminates those data races under Swift 6
/// strict concurrency.
///
/// Usage:
/// ```swift
/// @State private var stateManager = StateRestorationManager()
///
/// ContentView()
///     .environment(stateManager)
/// ```
@MainActor
@Observable
final class StateRestorationManager {
    // MARK: - Public State

    /// The currently selected tab.
    var selectedTab: Int = 0

    /// The navigation path for NavigationStack.
    ///
    /// Persist using `NavigationPath.codable`:
    /// ```swift
    /// // Save
    /// if let codable = navigationPath.codable {
    ///     appState.navigationPathData = try? JSONEncoder().encode(codable)
    /// }
    ///
    /// // Restore
    /// if let data = appState.navigationPathData,
    ///    let codable = try? JSONDecoder().decode(NavigationPath.CodableRepresentation.self, from: data) {
    ///     navigationPath = NavigationPath(codable)
    /// }
    /// ```
    ///
    /// All route types stored in the path must conform to both `Codable` and `Hashable`.
    /// If any type changes between app versions, decoding fails and the path resets to empty.
    var navigationPath = NavigationPath()

    /// Whether the user should be prompted to restore (for .askUser behavior).
    var showRestorePrompt = false

    // MARK: - Private

    private var appState = AppState()
    private let storage: StateStorageMethod
    private let restoreBehavior: RestoreBehavior
    private let fileURL: URL
    private var saveTask: Task<Void, Never>?
    private let debounceInterval: Duration

    // MARK: - Init

    init(
        storage: StateStorageMethod = .file(),
        restoreBehavior: RestoreBehavior = .timeLimited(minutes: 30),
        debounceInterval: Duration = .milliseconds(500)
    ) {
        self.storage = storage
        self.restoreBehavior = restoreBehavior
        self.debounceInterval = debounceInterval

        switch storage {
        case .file(let directory):
            let dir = directory ?? FileManager.default
                .urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
                .appendingPathComponent("StateRestoration", isDirectory: true)
            try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
            self.fileURL = dir.appendingPathComponent("appState.json")
        case .userDefaults:
            self.fileURL = URL(fileURLWithPath: "/dev/null") // Not used for UserDefaults
        }

        // Note: Performs synchronous file I/O on init. Consider deferring to .task modifier for large state files.
        restoreState()
    }

    // MARK: - Save

    /// Save current state immediately.
    func saveState() {
        appState.selectedTab = selectedTab
        appState.lastSavedDate = Date()

        // Encode navigation path
        if let codable = navigationPath.codable {
            appState.navigationPathData = try? JSONEncoder().encode(codable)
        }

        persistState()
    }

    /// Schedule a debounced save. Call this on every state change.
    func scheduleSave() {
        saveTask?.cancel()
        saveTask = Task { [weak self] in
            try? await Task.sleep(for: self?.debounceInterval ?? .milliseconds(500))
            guard !Task.isCancelled else { return }
            self?.saveState()
        }
    }

    /// Save state when the app enters the background.
    ///
    /// Call from `.onChange(of: scenePhase)`:
    /// ```swift
    /// .onChange(of: scenePhase) { _, newPhase in
    ///     if newPhase == .background {
    ///         stateManager.saveOnBackground()
    ///     }
    /// }
    /// ```
    func saveOnBackground() {
        saveTask?.cancel()
        saveState()
    }

    // MARK: - Restore

    /// Restore state from persistent storage.
    func restoreState() {
        guard let loaded = loadState() else { return }

        switch restoreBehavior {
        case .always:
            applyState(loaded)

        case .timeLimited(let minutes):
            let elapsed = Date().timeIntervalSince(loaded.lastSavedDate)
            let limit = TimeInterval(minutes * 60)
            if elapsed <= limit {
                applyState(loaded)
            }

        case .askUser:
            appState = loaded
            showRestorePrompt = true
        }
    }

    /// Apply the pending restored state (called after user confirms in .askUser mode).
    func confirmRestore() {
        applyState(appState)
        showRestorePrompt = false
    }

    /// Discard the pending restored state.
    func declineRestore() {
        appState = AppState()
        showRestorePrompt = false
        clearState()
    }

    // MARK: - Scroll Positions

    /// Save the scroll position for a given scroll view.
    func saveScrollPosition(id scrollViewID: String, topItemID: String) {
        appState.scrollPositions[scrollViewID] = topItemID
        scheduleSave()
    }

    /// Get the saved scroll position for a given scroll view.
    func scrollPosition(for scrollViewID: String) -> String? {
        appState.scrollPositions[scrollViewID]
    }

    // MARK: - Form Drafts

    /// Save a form field value as a draft.
    func saveFormDraft(formID: String, key: String, value: String) {
        if appState.formDrafts[formID] == nil {
            appState.formDrafts[formID] = [:]
        }
        appState.formDrafts[formID]?[key] = value
        scheduleSave()
    }

    /// Get a saved draft value for a form field.
    func formDraftValue(formID: String, key: String) -> String? {
        appState.formDrafts[formID]?[key]
    }

    /// Clear all draft data for a form (call on successful submission).
    func clearFormDraft(formID: String) {
        appState.formDrafts.removeValue(forKey: formID)
        scheduleSave()
    }

    // MARK: - Clear

    /// Clear all saved state.
    func clearState() {
        appState = AppState()
        selectedTab = 0
        navigationPath = NavigationPath()

        switch storage {
        case .file:
            try? FileManager.default.removeItem(at: fileURL)
        case .userDefaults(let suiteName):
            let defaults = suiteName.map { UserDefaults(suiteName: $0) } ?? UserDefaults.standard
            defaults?.removeObject(forKey: stateDefaultsKey)
        }
    }

    // MARK: - Private Helpers

    private let stateDefaultsKey = "com.app.stateRestoration.appState"

    private func applyState(_ state: AppState) {
        appState = state
        selectedTab = state.selectedTab

        // Restore navigation path using NavigationPath.codable persistence pattern
        if let data = state.navigationPathData,
           let codable = try? JSONDecoder().decode(
               NavigationPath.CodableRepresentation.self,
               from: data
           ) {
            navigationPath = NavigationPath(codable)
        }
    }

    private func persistState() {
        guard let data = try? JSONEncoder().encode(appState) else { return }

        switch storage {
        case .file:
            try? data.write(to: fileURL, options: .atomic)

        case .userDefaults(let suiteName):
            let defaults = suiteName.map { UserDefaults(suiteName: $0) } ?? UserDefaults.standard
            defaults?.set(data, forKey: stateDefaultsKey)
        }
    }

    private func loadState() -> AppState? {
        let data: Data?

        switch storage {
        case .file:
            data = try? Data(contentsOf: fileURL)

        case .userDefaults(let suiteName):
            let defaults = suiteName.map { UserDefaults(suiteName: $0) } ?? UserDefaults.standard
            data = defaults?.data(forKey: stateDefaultsKey)
        }

        guard let data else { return nil }
        return try? JSONDecoder().decode(AppState.self, from: data)
    }
}

// MARK: - Environment Integration

private struct StateRestorationManagerKey: EnvironmentKey {
    static let defaultValue: StateRestorationManager? = nil
}

extension EnvironmentValues {
    var stateRestorationManager: StateRestorationManager? {
        get { self[StateRestorationManagerKey.self] }
        set { self[StateRestorationManagerKey.self] = newValue }
    }
}

// MARK: - NavigationStateModifier

/// ViewModifier that persists and restores NavigationStack path.
///
/// Wraps a NavigationStack and automatically saves the path
/// whenever it changes. Restores on appear.
///
/// Usage:
/// ```swift
/// NavigationStack(path: $stateManager.navigationPath) {
///     RootView()
///         .navigationDestination(for: Route.self) { route in
///             RouteView(route: route)
///         }
/// }
/// .modifier(NavigationStateModifier(stateManager: stateManager))
/// ```
///
/// **Important:** All route types in the NavigationPath must conform
/// to both `Codable` and `Hashable`. If any type changes between
/// app versions, decoding fails and the path resets to empty.
struct NavigationStateModifier: ViewModifier {
    let stateManager: StateRestorationManager

    @Environment(\.scenePhase) private var scenePhase

    func body(content: Content) -> some View {
        content
            .onChange(of: stateManager.navigationPath) {
                stateManager.scheduleSave()
            }
            .onChange(of: scenePhase) { _, newPhase in
                if newPhase == .background {
                    stateManager.saveOnBackground()
                }
            }
    }
}

extension View {
    /// Attach navigation state persistence to a NavigationStack.
    func persistNavigationState(using stateManager: StateRestorationManager) -> some View {
        modifier(NavigationStateModifier(stateManager: stateManager))
    }
}

// MARK: - TabRestorationModifier

/// ViewModifier that persists the selected tab to @AppStorage.
///
/// Automatically saves the tab selection whenever it changes
/// and restores it on app launch.
///
/// Usage:
/// ```swift
/// TabView(selection: $stateManager.selectedTab) {
///     HomeView().tag(0)
///     SearchView().tag(1)
///     ProfileView().tag(2)
/// }
/// .modifier(TabRestorationModifier(stateManager: stateManager))
/// ```
///
/// For String-based tab tags, use `@AppStorage("selectedTab") private var selectedTab = "home"` directly.
struct TabRestorationModifier: ViewModifier {
    let stateManager: StateRestorationManager

    @Environment(\.scenePhase) private var scenePhase

    func body(content: Content) -> some View {
        content
            .onChange(of: stateManager.selectedTab) {
                stateManager.scheduleSave()
            }
            .onChange(of: scenePhase) { _, newPhase in
                if newPhase == .background {
                    stateManager.saveOnBackground()
                }
            }
    }
}

extension View {
    /// Attach tab selection persistence.
    func persistTabSelection(using stateManager: StateRestorationManager) -> some View {
        modifier(TabRestorationModifier(stateManager: stateManager))
    }
}
