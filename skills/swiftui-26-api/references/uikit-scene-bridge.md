# UIKit Scene Bridge API
Bridge UIKit scene lifecycle with SwiftUI scenes via UIHostingSceneDelegate.

## UIHostingSceneDelegate

**URL:** https://sosumi.ai/documentation/SwiftUI/UIHostingSceneDelegate?.md

**Contents:**
- Overview
- Inherits From
- Associated Types
- Type Properties
- Displaying SwiftUI views in UIKit

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+

Declare any SwiftUI scenes you wish to activate from UIKit in the static `rootScene` property of your conforming class:

Use a class conforming to [UIHosting Scene Delegate](/documentation/swiftui/uihostingscenedelegate) to  activate a scene by its ID or presented value with `UISceneSessionActivationRequest`:

When a SwiftUI scene declared in your `rootScene` property is activated, an instance of your conforming class will be created by SwiftUI and receive window scene lifecycle callbacks.

Your `UIHostingSceneDelegate` class can be used with a `UISceneConfiguration` in your app delegate's `application(_:configurationForConnecting:options:)`method to activate a SwiftUI scene in response to an external event:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol UIHostingSceneDelegate : UISceneDelegate
```

Example 2 (swift):
```swift
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }

    // Add UISceneDelegate lifecycle callbacks here
}
```

Example 3 (swift):
```swift
if let requestWithID = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: requestWithID)
}

if let requestWithData = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    value: FavoriteNumber(13)
) {
    UIApplication.shared.activateSceneSession(for: requestWithData)
}
```

Example 4 (swift):
```swift
class AppDelegate: UIApplicationDelegate {

    func application(
        _ app: UIApplication,
        configurationForConnecting sceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {
        let config = UISceneConfiguration(
            name: nil, sessionRole: sceneSession.role)
        config.delegateClass = HostingSceneDelegate.self
        return config
    }

}
```

---

## Migration: UIHostingController → UIHostingSceneDelegate

**Why migrate:** Declarative scene management — no manual UIWindow creation, scene lifecycle handled by SwiftUI.

**Before (pre-iOS 26):** UIHostingController in scene delegate
```swift
class SceneDelegate: UIWindowSceneDelegate {
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options: UIScene.ConnectionOptions) {
        let window = UIWindow(windowScene: scene as! UIWindowScene)
        window.rootViewController = UIHostingController(rootView: ContentView())
        window.makeKeyAndVisible()
    }
}
```

**After (iOS 26+):** UIHostingSceneDelegate with declarative scenes
```swift
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "main") { ContentView() }
    }
}
// Activate: UISceneSessionActivationRequest(hostingDelegateClass:id:)
```

**Gotcha:** The `rootScene` property must be `static var`, not `static func`. Scene ID in activation request must match exactly.

## Reading Paths

**Path C — Web Content (this file is step 2):**
← From `webkit.md` → this file

**Path D — App Migration:**
Start here for UIKit-to-SwiftUI scene bridge migration
