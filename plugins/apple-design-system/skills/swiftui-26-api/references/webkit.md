# WebKit Integration APIs
APIs for embedding and controlling web content in SwiftUI using WebView and WebPage.

## Table of Contents
- [WebView](#webview) — SwiftUI view that embeds and renders web content from a URL or WebPage
- [WebPage](#webpage) — Observable model object for controlling navigation, JavaScript, and page state

## WebView

**URL:** https://sosumi.ai/documentation/WebKit/WebView-swift.struct?.md

**Contents:**
- Overview
- Conforms To
- Creating web views
- Modifying web interactions
- Essentials

**Navigation:** [WebKit](/documentation/WebKit)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+

Present HTML, CSS, and JavaScript content alongside an app's native views with [Web View-swift.struct](/documentation/webkit/webview-swift.struct). Specify web content with a [URL](/documentation/Foundation/URL) when using the [init(url:)](/documentation/webkit/webview-swift.struct/init(url:)) initializer, or with a [Web Page](/documentation/webkit/webpage) when using the [init(*:)](/documentation/webkit/webview-swift.struct/init(*:)) initializer, which allows full control of the browsing experience. Any updates to the page propagate the information to the view.

[Web View-swift.struct](/documentation/webkit/webview-swift.struct) provides a complete browsing experience, including the ability to navigate between different webpages using links, forward and back buttons, and more. When a person clicks a link in the content, the view acts like a browser and displays the content at that link. To customize navigation, use a [Web Page](/documentation/webkit/webpage) with a [Web View-swift.struct](/documentation/webkit/webview-swift.struct) and customize the [Configuration](/documentation/webkit/webpage/configuration), or create a new type that conforms to [Navigation Deciding](/documentation/webkit/webpage/navigationdeciding).

The following example displays two different URLs depending on the state of a toggle, and also prevents back-forward navigation gestures:

A [Web View-swift.struct](/documentation/webkit/webview-swift.struct) is a scrollable view, and behaves similarly to [Scroll View](/documentation/SwiftUI/ScrollView). Customize scrolling in a [Web View-swift.struct](/documentation/webkit/webview-swift.struct) with:

Customize [Web View-swift.struct](/documentation/webkit/webview-swift.struct) display and interactions with view modifiers, such as:

To further customize and control a web interaction, connect a [Web View-swift.struct](/documentation/webkit/webview-swift.struct) to a [Web Page](/documentation/webkit/webpage). The following example demonstrates this by configuring the view's navigation title to be the webpage's title, which the system updates automatically because [Web Page](/documentation/webkit/webpage) is an `Observable` type:

A [Web Page](/documentation/webkit/webpage) can only be bound to a single [Web View-swift.struct](/documentation/webkit/webview-swift.struct) at a time.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct WebView
```

Example 2 (swift):
```swift
import SwiftUI
import WebKit

struct ContentView: View {
    @State private var toggle = false

    private var url: URL? {
        toggle ? URL(string: "https://www.webkit.org") : URL(string: "https://www.swift.org")
    }

    var body: some View {
        WebView(url: url)
            .toolbar {
                Button(buttonName, systemImage: buttonIcon) {
                    toggle.toggle()
                }
            }
            .webViewBackForwardNavigationGestures(.disabled)
    }
}
```

Example 3 (swift):
```swift
struct ContentView: View {
    @State private var page = WebPage()

    var body: some View {
        NavigationStack {
            WebView(page)
                .navigationTitle(page.title)
        }
    }
}
```

---

## WebPage

**URL:** https://sosumi.ai/documentation/WebKit/WebPage?.md

**Contents:**
- Overview
- Conforms To
- Creating a WebPage
- Managing navigation between webpages
- Observing navigation between webpages
- Configuring a WebPage
- Loading web content
- Managing the loading process
- Inspecting page information
- Executing JavaScript

**Navigation:** [WebKit](/documentation/WebKit)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+

A [Web Page](/documentation/webkit/webpage) is an [Observable](/documentation/Observation/Observable) type for accessing various properties of web content and tracking changes to them. Use [Web Page](/documentation/webkit/webpage) to interact with web content, like evaluating JavaScript or converting the page to PDF data. The following example shows how to combine these capabilities to get specific metadata from an ephemeral page with a custom user agent:

Use [Web Page](/documentation/webkit/webpage) to programmatically navigate to various types of resources like URL requests, HTML strings, and data. Optionally, observe these navigations through the async sequence returned by their associated loading functions, and customize them by using a type that conforms to the [Navigation Deciding](/documentation/webkit/webpage/navigationdeciding) protocol. The [back Forward List-swift.property](/documentation/webkit/webpage/backforwardlist-swift.property) property can be used to observe changes to people's navigation history, and to programmatically navigate to a specific back-forward list item.

[Web Page](/documentation/webkit/webpage) also conforms to the `Transferable` protocol. This conformance allows exporting the page to various different types of content, like PDF, web archive data, and other types. For customization of PDF or image export, use [exported(as:)](/documentation/webkit/webpage/exported(as:)).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor final class WebPage
```

Example 2 (swift):
```swift
func fetchMetadata(for url: URL) async throws -> (title: String, description: String) {
    let botAgent = """
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0
    """

    var configuration = WebPage.Configuration()
    configuration.loadsSubresources = false
    configuration.defaultNavigationPreferences.allowsContentJavaScript = false
    configuration.websiteDataStore = .nonPersistent()

    // Set up the configured page.

    let page = WebPage(configuration: configuration)
    page.customUserAgent = botAgent

    // Load the request and wait for navigation to complete.

    let request = URLRequest(url: url)
    for try await event in page.load(request) {
        // Optionally do something with `event`.
    }

    // At this point, the navigation is complete.
    // Now, use JavaScript to query the appropriate properties of the page.

    let fetchOpenGraphProperty = """
    const propertyValues = document.querySelectorAll(`meta[property="${property}"]`);
    return propertyValues[0];
    """

    let javaScriptResult = try await page.callJavaScript(fetchOpenGraphProperty, arguments: arguments)
    guard let description = javaScriptResult as? String else {
        // Handle failure, like throwing an error.
    }

    guard let title = page.title else {
        // Handle failure, like throwing an error.
    }

    return (title, description)
}
```

---

## Migration: WKWebView → WebView

**Why migrate:** Native SwiftUI view with Observable WebPage controller — no UIViewRepresentable boilerplate, automatic state observation.

**Before (pre-iOS 26):** WKWebView wrapped in UIViewRepresentable
```swift
struct WebViewWrapper: UIViewRepresentable {
    let url: URL
    func makeUIView(context: Context) -> WKWebView { WKWebView() }
    func updateUIView(_ view: WKWebView, context: Context) {
        view.load(URLRequest(url: url))
    }
}
```

**After (iOS 26+):** Native SwiftUI WebView
```swift
import WebKit
WebView(url: url)
// Or with full control:
@State private var page = WebPage()
WebView(page).navigationTitle(page.title)
```

**Gotcha:** `WebPage` is `@MainActor`. If loading from a background task, wrap in `await MainActor.run { }`.

## Anti-Patterns

| Don't | What Happens | Do Instead |
|-------|-------------|-----------|
| Bind one `WebPage` to two `WebView`s | Undefined behavior — only one WebPage can bind to a single WebView | One `@State var page = WebPage()` per `WebView` instance |
| Access `WebPage` off main actor | Concurrency violation — `WebPage` is `@MainActor` | Use `await MainActor.run { }` or keep in `@MainActor` context |

## Reading Paths

**Path C — Web Content (this file is step 1):**
Next → `uikit-scene-bridge.md` (if hosting in UIKit)
