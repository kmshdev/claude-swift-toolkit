---
name: swift-project-scaffold
description: Use when creating a new iOS or macOS Xcode project. Provides XcodeGen project.yml templates, app entry point archetypes, and post-scaffold build setting patches for Swift 6.2 / iOS 26 / macOS 26 with strict concurrency.
---

## 1. Template Variables

| Variable | Description |
|----------|-------------|
| `__APP_NAME__` | App display name and target name |
| `__BUNDLE_PREFIX__` | Bundle ID prefix (e.g., `com.username`) |
| `__BUNDLE_ID__` | Full bundle ID (`__BUNDLE_PREFIX__.__APP_NAME__`) |
| `__MACOS_TARGET__` | macOS deployment target (default: `26.0`) |
| `__IOS_TARGET__` | iOS deployment target (default: `26.0`) |

## 2. XcodeGen Path (Primary)

Steps when `xcodegen` is available:

1. Create directory structure: `Sources/<AppName>/`, `Tests/<AppName>Tests/`
2. Write `project.yml` from template (select `macos.project.yml` or `ios.project.yml`)
3. Replace all `__TEMPLATE_VAR__` placeholders with actual values
4. Write `AppEntry.swift` and `ContentView.swift` from templates
5. Write `.gitignore` from template
6. Run `xcodegen generate`
7. Open the generated project in Xcode and verify with `BuildProject` when the bridge is available, otherwise use `xcodebuild`

## 3. Manual Xcode Fallback

Steps when `xcodegen` is NOT available:

1. Stop the automated scaffold path and tell the user there is no official Xcode
   MCP project-scaffolding tool in this toolkit.
2. Ask the user to either install XcodeGen or create a new App project in Xcode
   manually.
3. Once the project exists, write the template-based `AppEntry.swift`,
   `ContentView.swift`, and `.gitignore` files into that project structure.
4. Verify with `BuildProject` if the project is open in Xcode, otherwise use
   `xcodebuild`.

## 4. App Archetypes

### Standard (WindowGroup)

```swift
@main
struct __APP_NAME__App: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Document-Based

```swift
@main
struct __APP_NAME__App: App {
    var body: some Scene {
        DocumentGroup(newDocument: __APP_NAME__Document()) { file in
            ContentView(document: file.$document)
        }
    }
}
```

### Menu Bar Extra

```swift
@main
struct __APP_NAME__App: App {
    var body: some Scene {
        MenuBarExtra("__APP_NAME__", systemImage: "star.fill") {
            ContentView()
        }
        .menuBarExtraStyle(.window)
    }
}
```

### Utility (Single Window)

```swift
@main
struct __APP_NAME__App: App {
    var body: some Scene {
        Window("__APP_NAME__", id: "main") {
            ContentView()
        }
        .defaultSize(width: 600, height: 400)
    }
}
```

## 5. Post-Scaffold Checklist

| Requirement | How to verify |
|-------------|---------------|
| Swift 6.2 strict concurrency | `SWIFT_STRICT_CONCURRENCY = complete` in build settings |
| Correct deployment target | Check `MACOSX_DEPLOYMENT_TARGET` or `IPHONEOS_DEPLOYMENT_TARGET` |
| Working .xcodeproj | `BuildProject` succeeds with clean build |
| Test target wired | `RunAllTests` runs (even with 0 tests) |
| RenderPreview works | ContentView has `#Preview` block |
| Proper app bundle (.app) | Target type is `application` |
| Git-friendly | `.gitignore` excludes `.xcodeproj` (if XcodeGen), includes `project.yml` |

## Cross-References

- `apple-app-architect:swift-app-lifecycle` — scene structure details
- `apple-app-builder:xcode-mcp` — BuildProject, diagnostics, previews, and targeted tests
