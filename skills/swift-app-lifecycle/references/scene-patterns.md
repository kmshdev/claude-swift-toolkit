# Scene Patterns Reference

## Multi-Window macOS App

```swift
@main
struct ProjectManager: App {
    var body: some Scene {
        // Main project list window
        WindowGroup {
            ProjectListView()
        }

        // Per-project detail window
        WindowGroup("Project", for: Project.ID.self) { $projectID in
            if let projectID {
                ProjectDetailView(projectID: projectID)
            }
        }
        .defaultSize(width: 800, height: 600)

        // Single-instance inspector
        Window("Inspector", id: "inspector") {
            InspectorView()
        }
        .defaultSize(width: 300, height: 500)
        .windowResizability(.contentSize)

        // Preferences
        Settings {
            SettingsView()
        }

        // Menu bar widget
        MenuBarExtra("Status", systemImage: "checkmark.circle") {
            QuickStatusView()
        }
        .menuBarExtraStyle(.window)  // .menu for simple popover
    }
}
```

## Document-Based App

```swift
@main
struct TextEditor: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditorView(document: file.$document)
        }
    }
}

struct TextDocument: FileDocument {
    static var readableContentTypes: [UTType] = [.plainText]
    var text: String = ""

    init() {}

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents,
              let string = String(data: data, encoding: .utf8)
        else { throw CocoaError(.fileReadCorruptFile) }
        text = string
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        FileWrapper(regularFileWithContents: Data(text.utf8))
    }
}
```

## Tab-Based iOS App

```swift
@main
struct MyApp: App {
    @State private var selectedTab: Tab = .home

    var body: some Scene {
        WindowGroup {
            TabView(selection: $selectedTab) {
                Tab("Home", systemImage: "house", value: .home) {
                    HomeView()
                }
                Tab("Search", systemImage: "magnifyingglass", value: .search) {
                    SearchView()
                }
                Tab("Profile", systemImage: "person", value: .profile) {
                    ProfileView()
                }
            }
            .onOpenURL { url in
                // Route deep links to tabs
                if url.host == "profile" { selectedTab = .profile }
            }
        }
    }
}

enum Tab: Hashable {
    case home, search, profile
}
```

## State Restoration

```swift
@main
struct MyApp: App {
    @AppStorage("lastOpenTab") private var lastTab: String = "home"
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            ContentView(initialTab: lastTab)
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .background {
                // Save restoration state
                lastTab = currentTab.rawValue
            }
        }
    }
}
```
