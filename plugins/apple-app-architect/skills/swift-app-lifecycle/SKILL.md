---
name: swift-app-lifecycle
description: Design and implement the app entry point, scene structure, deep links, and system integrations. Use when scaffolding a new app, adding multi-window support, implementing URL schemes, or configuring push notifications.
---

# Swift App Lifecycle

## Lifecycle Position

Phase 0-1 (Scaffold/Architecture). Load when setting up app entry point, scenes, and system integration. Related: `macos-development` for macOS-specific architecture patterns.

## App Entry Point

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        #if os(macOS)
        Settings {
            SettingsView()
        }

        Window("About", id: "about") {
            AboutView()
        }

        MenuBarExtra("Status", systemImage: "circle.fill") {
            MenuBarView()
        }
        #endif
    }
}
```

## Scene Types

| Scene | Use Case | Platform |
|-------|----------|----------|
| `WindowGroup` | Main app window (supports multiple instances) | All |
| `Window` | Single-instance utility window | macOS |
| `DocumentGroup` | Document-based app (open/save/new) | All |
| `Settings` | Preferences window (⌘,) | macOS |
| `MenuBarExtra` | Menu bar icon with popover or window | macOS |

### WindowGroup with Value (macOS multi-window)
```swift
WindowGroup(for: Project.ID.self) { $projectID in
    if let projectID {
        ProjectView(id: projectID)
    }
}

// Open from anywhere:
@Environment(\.openWindow) private var openWindow
Button("Open Project") { openWindow(value: project.id) }
```

## ScenePhase Lifecycle

```swift
@Environment(\.scenePhase) private var scenePhase

.onChange(of: scenePhase) { oldPhase, newPhase in
    switch newPhase {
    case .active:
        // App is visible and interactive
        refreshData()
    case .inactive:
        // App is visible but not interactive (e.g., notification shade)
        pauseTimers()
    case .background:
        // App is not visible — save state NOW
        saveState()
        scheduleBackgroundRefresh()
    @unknown default: break
    }
}
```

**State preservation pattern:**
```swift
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .background {
                // For actor-based persistence, see swift-actor-persistence skill
                PersistenceController.shared.save()
            }
        }
    }
}
```

## Deep Links

### Custom URL Schemes
```swift
// Info.plist: Add URL Types → URL Schemes: "myapp"
// Handles: myapp://path/to/content?id=123

WindowGroup {
    ContentView()
        .onOpenURL { url in
            router.handle(url)
        }
}

// Router pattern
@Observable class DeepLinkRouter {
    var selectedTab: Tab = .home
    var presentedItem: Item?

    func handle(_ url: URL) {
        guard url.scheme == "myapp" else { return }
        switch url.host {
        case "item":
            if let id = url.pathComponents.last {
                presentedItem = Item(id: id)
            }
        case "settings":
            selectedTab = .settings
        default: break
        }
    }
}
```

### Universal Links
```swift
// Requires Associated Domains entitlement: applinks:example.com
// apple-app-site-association file on your server

.onOpenURL { url in
    // Handles both custom scheme AND https://example.com/item/123
    router.handle(url)
}
```

## Push Notifications

### Permission Flow
```swift
import UserNotifications

func requestNotificationPermission() async -> Bool {
    let center = UNUserNotificationCenter.current()
    do {
        let granted = try await center.requestAuthorization(options: [.alert, .badge, .sound])
        if granted {
            await MainActor.run { UIApplication.shared.registerForRemoteNotifications() }
        }
        return granted
    } catch {
        return false
    }
}
```

### Registration
```swift
// In AppDelegate adaptor:
class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = deviceToken.map { String(format: "%02x", $0) }.joined()
        // Send token to your server
    }

    func application(_ application: UIApplication,
                     didFailToRegisterForRemoteNotificationsWithError error: Error) {
        print("Push registration failed: \(error)")
    }
}

// Connect in App
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate
    // ...
}
```

## Background Tasks

```swift
import BackgroundTasks

// Register in App init or AppDelegate
BGTaskScheduler.shared.register(forTaskWithIdentifier: "com.app.refresh", using: nil) { task in
    handleAppRefresh(task: task as! BGAppRefreshTask)
}

// Schedule
func scheduleBackgroundRefresh() {
    let request = BGAppRefreshTaskRequest(identifier: "com.app.refresh")
    request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60) // 15 min
    try? BGTaskScheduler.shared.submit(request)
}

// Handle
func handleAppRefresh(task: BGAppRefreshTask) {
    scheduleBackgroundRefresh() // Schedule next one

    let operation = Task {
        await refreshContent()
    }

    task.expirationHandler = { operation.cancel() }

    Task {
        await operation.value
        task.setTaskCompleted(success: true)
    }
}
```

**Info.plist requirement:**
```xml
<key>BGTaskSchedulerPermittedIdentifiers</key>
<array>
    <string>com.app.refresh</string>
</array>
```

## macOS-Specific

### NSApplicationDelegateAdaptor
```swift
class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) { }
    func applicationWillTerminate(_ notification: Notification) {
        // Final cleanup
    }
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        true  // Quit when last window closes (document apps usually return false)
    }
}

@main
struct MyApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var delegate
    // ...
}
```

### Menu Commands
```swift
var body: some Scene {
    WindowGroup { ContentView() }
        .commands {
            CommandGroup(replacing: .newItem) {
                Button("New Project") { /* ... */ }
                    .keyboardShortcut("n", modifiers: .command)
            }
            CommandMenu("Tools") {
                Button("Run Analysis") { /* ... */ }
                    .keyboardShortcut("r", modifiers: [.command, .shift])
            }
        }
}
```

## Common Mistakes

1. Not saving state on `.background` — data lost when system terminates backgrounded app
2. Requesting notification permission on launch — ask in context when user understands the value
3. Missing `@UIApplicationDelegateAdaptor` / `@NSApplicationDelegateAdaptor` — needed for push tokens and system callbacks
4. Background tasks not registered in Info.plist — silently fails to schedule
5. `applicationShouldTerminateAfterLastWindowClosed` not set on macOS — app stays running with no windows

## Checklist

- [ ] State saved on `.background` scene phase transition
- [ ] Deep link routes cover all app entry points
- [ ] Notification permissions requested contextually (not on first launch)
- [ ] Background tasks registered in Info.plist with matching identifiers
- [ ] macOS apps handle `applicationShouldTerminateAfterLastWindowClosed`
- [ ] Universal Links have apple-app-site-association file on server
- [ ] `@main` App struct is the single entry point (no duplicate `@main`)

## Templates

App lifecycle helpers in `templates/` — copy and adapt:

- **`ForceUpdateChecker.swift`** — Version comparison with remote config, hard-block vs soft-prompt UI, App Store redirect
- **`StateRestorationManager.swift`** — `@MainActor @Observable` state restoration with `NavigationPath` persistence, debounced save, restore-behavior policies

## Cross-References

- `macos-development` — macOS architecture patterns, SwiftData setup, AppKit bridging
- `swift-concurrency` — async/await in app delegate methods and background tasks
- `swift-networking` — background transfer configuration for downloads
- `app-development-workflow` — lifecycle Phase 0-1 context
- `swift-actor-persistence` — actor-based repositories for implementing `save()` on `.background` scene phase
- `swiftui-26-api` — `UIHostingSceneDelegate` for bridging UIKit scene lifecycle to SwiftUI
