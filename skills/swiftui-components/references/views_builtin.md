# Swiftui-Components - Views Builtin

**Pages:** 22

---

## Button

**URL:** https://sosumi.ai/documentation/swiftui/button?.md

**Contents:**
- Overview
  - Adding buttons to containers
  - Assigning a role
  - Styling buttons
- Conforms To
- Creating a button
- Creating a button with a role
- Creating a button from a configuration
- Creating a button to perform an App Intent
- Initializers

---
title: Button
description: A control that initiates an action.
source: https://developer.apple.com/documentation/swiftui/button
timestamp: 2026-02-13T19:32:31.118Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control that initiates an action.

You create a button by providing an action and a label. The action is either a method or closure property that does something when a user clicks or taps the button. The label is a view that describes the button’s action — for example, by showing text, an icon, or both.

The label of a button can be any kind of view, such as a [Text](/documentation/swiftui/text) view for text-only labels:

Or a [Label](/documentation/swiftui/label) view, for buttons with both a title and an icon:

For those common cases, you can also use the convenience initializers that take a title string or [Localized String Key](/documentation/swiftui/localizedstringkey) as their first parameter, and optionally a system image name or `ImageResource` as their second parameter, instead of a trailing closure:

Prefer to use these convenience initializers, or a [Label](/documentation/swiftui/label) view, when providing both a title and an icon. This allows the button to dynamically adapt its appearance to render its title and icon correctly in containers such as toolbars and menus. For example, on iOS, buttons only display their icons by default when placed in toolbars, but show both a leading title and trailing icon in menus. Defining labels this way also helps with accessibility — for example, applying the [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:)) modifier with an [icon Only](/documentation/swiftui/labelstyle/icononly) style to the button will cause it to only visually display its icon, but still use its title to describe the button in accessibility modes like VoiceOver:

Avoid labels that only use images or exclusively visual components without an accessibility label.

How the user activates the button varies by platform:

- In iOS and watchOS, the user taps the button.
- In macOS, the user clicks the button.
- In tvOS, the user presses “select” on an external remote, like the Siri Remote, while focusing on the button.

The appearance of the button depends on factors like where you place it, whether you assign it a role, and how you style it.

Use buttons for any user interface element that initiates an action. Buttons automatically adapt their visual style to match the expected style within these different containers and contexts. For example, to create a [List](/documentation/swiftui/list) cell that initiates an action when selected by the user, add a button to the list’s content:

Similarly, to create a context menu item that initiates an action, add a button to the [contextMenu(_:)](/documentation/swiftui/view/contextmenu(_:)) modifier’s content closure:

This pattern extends to most other container views in SwiftUI that have customizable, interactive content, like [Form](/documentation/swiftui/form) instances.

You can optionally initialize a button with a [Button Role](/documentation/swiftui/buttonrole) that characterizes the button’s purpose. For example, you can create a [destructive](/documentation/swiftui/buttonrole/destructive) button for a deletion action:

The system uses the button’s role to style the button appropriately in every context. For example, a destructive button in a contextual menu appears with a red foreground color:

If you don’t specify a role for a button, the system applies an appropriate default appearance.

You can customize a button’s appearance using one of the standard button styles, like [bordered](/documentation/swiftui/primitivebuttonstyle/bordered), and apply the style with the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)) modifier:

If you apply the style to a container view, as in the example above, all the buttons in the container use the style:

You can also create custom styles. To add a custom appearance with standard interaction behavior, create a style that conforms to the [Button Style](/documentation/swiftui/buttonstyle) protocol. To customize both appearance and interaction behavior, create a style that conforms to the [Primitive Button Style](/documentation/swiftui/primitivebuttonstyle) protocol. Custom styles can also read the button’s role and use it to adjust the button’s appearance.

- [View](/documentation/swiftui/view)

- [init(action:label:)](/documentation/swiftui/button/init(action:label:)) Creates a button that displays a custom label.
- [init(_:action:)](/documentation/swiftui/button/init(_:action:)) Creates a button that generates its label from a localized string key.
- [init(_:image:action:)](/documentation/swiftui/button/init(_:image:action:)) Creates a button that generates its label from a localized string key and image resource.
- [init(_:systemImage:action:)](/documentation/swiftui/button/init(_:systemimage:action:)) Creates a button that generates its label from a localized string key and system image name.

- [init(role:action:label:)](/documentation/swiftui/button/init(role:action:label:)) Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](/documentation/swiftui/button/init(_:role:action:)) Creates a button with a specified role that generates its label from a localized string key.
- [init(_:image:role:action:)](/documentation/swiftui/button/init(_:image:role:action:)) Creates a button with a specified role that generates its label from a localized string key and an image resource.
- [init(_:systemImage:role:action:)](/documentation/swiftui/button/init(_:systemimage:role:action:)) Creates a button with a specified role that generates its label from a localized string key and a system image.

- [init(_:)](/documentation/swiftui/button/init(_:)) Creates a button based on a configuration for a style with a custom appearance and custom interaction behavior.

- [init(_:intent:)](/documentation/swiftui/button/init(_:intent:)) Creates a button that performs an  and generates its label from a localized string key.
- [init(intent:label:)](/documentation/swiftui/button/init(intent:label:)) Creates a button that performs an .
- [init(_:role:intent:)](/documentation/swiftui/button/init(_:role:intent:)) Creates a button with a specified role that performs an  and generates its label from a string.
- [init(role:intent:label:)](/documentation/swiftui/button/init(role:intent:label:)) Creates a button with a specified role that performs an .
- [init(_:image:role:intent:)](/documentation/swiftui/button/init(_:image:role:intent:)) Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](/documentation/swiftui/button/init(_:systemimage:role:intent:)) Creates a button with a specified role that generates its label from a string and a system image.

- [init(role:action:)](/documentation/swiftui/button/init(role:action:)) Creates a button that displays a default label.

- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:))
- [buttonBorderShape(_:)](/documentation/swiftui/view/buttonbordershape(_:))
- [buttonRepeatBehavior(_:)](/documentation/swiftui/view/buttonrepeatbehavior(_:))
- [buttonRepeatBehavior](/documentation/swiftui/environmentvalues/buttonrepeatbehavior)
- [ButtonBorderShape](/documentation/swiftui/buttonbordershape)
- [ButtonRole](/documentation/swiftui/buttonrole)
- [ButtonRepeatBehavior](/documentation/swiftui/buttonrepeatbehavior)
- [ButtonSizing](/documentation/swiftui/buttonsizing)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Button<Label> where Label : View
```

Example 2 (swift):
```swift
Button(action: signIn) {
    Text("Sign In")
}
```

Example 3 (swift):
```swift
Button(action: signIn) {
    Label("Sign In", systemImage: "arrow.up")
}
```

Example 4 (swift):
```swift
Button("Sign In", systemImage: "arrow.up", action: signIn)
```

---

## ShareLink

**URL:** https://sosumi.ai/documentation/swiftui/sharelink?.md

**Contents:**
- Overview
- Conforms To
- Sharing an item
- Sharing an item with a preview
- Sharing items
- Sharing items with a preview
- Supporting types
- Linking to other content

---
title: ShareLink
description: A view that controls a sharing presentation.
source: https://developer.apple.com/documentation/swiftui/sharelink
timestamp: 2026-02-13T19:32:57.145Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+

> A view that controls a sharing presentation.

People tap or click on a share link to present a share interface. The link typically uses a system-standard appearance; you only need to supply the content to share:

You can control the appearance of the link by providing view content. For example, you can use a [Label](/documentation/swiftui/label) to display a link with a custom icon:

If you only wish to customize the link’s title, you can use one of the convenience initializers that takes a string and creates a `Label` for you:

The link can share any content that is [Transferable](/documentation/CoreTransferable/Transferable). Many framework types, like [URL](/documentation/Foundation/URL), already conform to this protocol. You can also make your own types transferable.

For example, you can use [Proxy Representation](/documentation/CoreTransferable/ProxyRepresentation) to resolve your own type to a framework type:

Sometimes the content that your app shares isn’t immediately available. You can use [File Representation](/documentation/CoreTransferable/FileRepresentation) or [Data Representation](/documentation/CoreTransferable/DataRepresentation) when you need an asynchronous operation, like a network request, to retrieve and prepare the content.

Note that some applications offer their sharing service for files, but not for a wide range of different data types, for example, Mail.app, Notes.app, Messages.app or AirDrop. If you don’t see a particular sharing service in the presented `ShareLink`, try adding a [File Representation](/documentation/CoreTransferable/FileRepresentation) to the type’s `Transferable` conformance.

A `Transferable` type also lets you provide multiple content types for a single shareable item. The share interface shows relevant sharing services based on the types that you provide.

The previous example also shows how you provide a preview of your content to show in the share interface.

A preview isn’t required when sharing URLs or non-attributed strings. When sharing these types of content, the system can automatically determine a preview.

You can provide a preview even when it’s optional. For instance, when sharing URLs, the automatic preview first shows a placeholder link icon alongside the base URL while fetching the link’s metadata over the network. The preview updates once the link’s icon and title become available. If you provide a preview instead, the preview appears immediately without fetching data over the network.

Some share activities support subject and message fields. You can pre-populate these fields with the `subject` and `message` parameters:

- [View](/documentation/swiftui/view)

- [init(item:subject:message:)](/documentation/swiftui/sharelink/init(item:subject:message:)) Creates an instance that presents the share interface.
- [init(_:item:subject:message:)](/documentation/swiftui/sharelink/init(_:item:subject:message:)) Creates an instance, with a custom label, that presents the share interface.
- [init(item:subject:message:label:)](/documentation/swiftui/sharelink/init(item:subject:message:label:)) Creates an instance that presents the share interface.

- [init(item:subject:message:preview:)](/documentation/swiftui/sharelink/init(item:subject:message:preview:)) Creates an instance that presents the share interface.
- [init(_:item:subject:message:preview:)](/documentation/swiftui/sharelink/init(_:item:subject:message:preview:)) Creates an instance, with a custom label, that presents the share interface.
- [init(item:subject:message:preview:label:)](/documentation/swiftui/sharelink/init(item:subject:message:preview:label:)) Creates an instance that presents the share interface.

- [init(items:subject:message:)](/documentation/swiftui/sharelink/init(items:subject:message:)) Creates an instance that presents the share interface.
- [init(_:items:subject:message:)](/documentation/swiftui/sharelink/init(_:items:subject:message:)) Creates an instance, with a custom label, that presents the share interface.
- [init(items:subject:message:label:)](/documentation/swiftui/sharelink/init(items:subject:message:label:)) Creates an instance that presents the share interface.

- [init(items:subject:message:preview:)](/documentation/swiftui/sharelink/init(items:subject:message:preview:)) Creates an instance that presents the share interface.
- [init(_:items:subject:message:preview:)](/documentation/swiftui/sharelink/init(_:items:subject:message:preview:)) Creates an instance, with a custom label, that presents the share interface.
- [init(items:subject:message:preview:label:)](/documentation/swiftui/sharelink/init(items:subject:message:preview:label:)) Creates an instance that presents the share interface.

- [DefaultShareLinkLabel](/documentation/swiftui/defaultsharelinklabel) The default label used for a share link.

- [Link](/documentation/swiftui/link)
- [SharePreview](/documentation/swiftui/sharepreview)
- [TextFieldLink](/documentation/swiftui/textfieldlink)
- [HelpLink](/documentation/swiftui/helplink)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ShareLink<Data, PreviewImage, PreviewIcon, Label> where Data : RandomAccessCollection, PreviewImage : Transferable, PreviewIcon : Transferable, Label : View, Data.Element : Transferable
```

Example 2 (swift):
```swift
ShareLink(item: URL(string: "https://developer.apple.com/xcode/swiftui/")!)
```

Example 3 (swift):
```swift
ShareLink(item: URL(string: "https://developer.apple.com/xcode/swiftui/")!) {
    Label("Share", image: "MyCustomShareIcon")
}
```

Example 4 (swift):
```swift
ShareLink("Share URL", item: URL(string: "https://developer.apple.com/xcode/swiftui/")!)
```

---

## AsyncImage

**URL:** https://sosumi.ai/documentation/swiftui/asyncimage?.md

**Contents:**
- Overview
- Conforms To
- Loading an image
- Loading an image in phases
- Loading images asynchronously

---
title: AsyncImage
description: A view that asynchronously loads and displays an image.
source: https://developer.apple.com/documentation/swiftui/asyncimage
timestamp: 2026-02-13T19:32:29.149Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> A view that asynchronously loads and displays an image.

This view uses the shared [URLSession](/documentation/Foundation/URLSession) instance to load an image from the specified URL, and then display it. For example, you can display an icon that’s stored on a server:

Until the image loads, the view displays a standard placeholder that fills the available space. After the load completes successfully, the view updates to display the image. In the example above, the icon is smaller than the frame, and so appears smaller than the placeholder.

You can specify a custom placeholder using [init(url:scale:content:placeholder:)](/documentation/swiftui/asyncimage/init(url:scale:content:placeholder:)). With this initializer, you can also use the `content` parameter to manipulate the loaded image. For example, you can add a modifier to make the loaded image resizable:

For this example, SwiftUI shows a [Progress View](/documentation/swiftui/progressview) first, and then the image scaled to fit in the specified frame:

> [!IMPORTANT]
> You can’t apply image-specific modifiers, like [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)), directly to an `AsyncImage`. Instead, apply them to the [Image](/documentation/swiftui/image) instance that your `content` closure gets when defining the view’s appearance.

To gain more control over the loading process, use the [init(url:scale:transaction:content:)](/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)) initializer, which takes a `content` closure that receives an [Async Image Phase](/documentation/swiftui/asyncimagephase) to indicate the state of the loading operation. Return a view that’s appropriate for the current phase:

- [View](/documentation/swiftui/view)

- [init(url:scale:)](/documentation/swiftui/asyncimage/init(url:scale:)) Loads and displays an image from the specified URL.
- [init(url:scale:content:placeholder:)](/documentation/swiftui/asyncimage/init(url:scale:content:placeholder:)) Loads and displays a modifiable image from the specified URL using a custom placeholder until the image loads.

- [init(url:scale:transaction:content:)](/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)) Loads and displays a modifiable image from the specified URL in phases.

- [AsyncImagePhase](/documentation/swiftui/asyncimagephase)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AsyncImage<Content> where Content : View
```

Example 2 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png"))
    .frame(width: 200, height: 200)
```

Example 3 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { image in
    image.resizable()
} placeholder: {
    ProgressView()
}
.frame(width: 50, height: 50)
```

Example 4 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

---

## SecureField

**URL:** https://sosumi.ai/documentation/swiftui/securefield?.md

**Contents:**
- Overview
  - Bind to a string
  - Guide people with a prompt
- Conforms To
- Creating a secure text field
- Deprecated initializers
- Getting text input

---
title: SecureField
description: A control into which people securely enter private text.
source: https://developer.apple.com/documentation/swiftui/securefield
timestamp: 2026-02-13T19:32:46.886Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control into which people securely enter private text.

Use a secure field when you want the behavior of a [Text Field](/documentation/swiftui/textfield), but you want to hide the field’s text. Typically, you use this for entering passwords and other sensitive information, as the second field in the following screenshot demonstrates:

- Displays one dot for each character someone types.
- Hides the dots when someone takes a screenshot in iOS.
- Prevents anyone from cutting or copying the field’s contents.
- Displays an indicator when Caps Lock is enabled.

A secure field binds to a string value and updates the string on every keystroke or other edit, so you can read its value at any time from elsewhere in your code. The following code shows how to create the above interface, with the secure field bound to a `password` string:

The field in the above example has an [onSubmit(of:_:)](/documentation/swiftui/view/onsubmit(of:_:)) modifier that sends the `username` and `password` strings to a custom `handleLogin(username:password:)` method if someone presses the Return key while the secure field has focus. You can alternatively provide another mechanism — like a button — to do the same thing.

In addition to the string or view that you provide as a label, you can also provide a [Text](/documentation/swiftui/text) view prompt to help guide someone who uses the field, as the following [Form](/documentation/swiftui/form) does:

The system uses the label and prompt in different ways depending on the context. For example, a form in macOS places the label against the leading edge of the field and uses the prompt as placeholder text inside the field. The same form in iOS also uses the prompt as placeholder text, but doesn’t display the label:

If you remove the prompt from the previous example, the field keeps the label on the leading edge and omits the placeholder text in macOS, but displays the label as a placeholder in iOS:

- [View](/documentation/swiftui/view)

- [init(_:text:)](/documentation/swiftui/securefield/init(_:text:)) Creates a secure field with a prompt generated from a .
- [init(_:text:prompt:)](/documentation/swiftui/securefield/init(_:text:prompt:)) Creates a secure field with a prompt generated from a .
- [init(text:prompt:label:)](/documentation/swiftui/securefield/init(text:prompt:label:)) Creates a secure field with a prompt generated from a .

- [init(_:text:onCommit:)](/documentation/swiftui/securefield/init(_:text:oncommit:)) Creates an instance.

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [TextField](/documentation/swiftui/textfield)
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:))
- [TextEditor](/documentation/swiftui/texteditor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct SecureField<Label> where Label : View
```

Example 2 (swift):
```swift
@State private var username: String = ""
@State private var password: String = ""

var body: some View {
    VStack {
        TextField("Username", text: $username)
            .autocorrectionDisabled(true)
            #if !os(macOS)
            .textInputAutocapitalization(.never)
            #endif

        SecureField("Password", text: $password)
            .onSubmit {
                handleLogin(username: username, password: password)
            }
    }
    .textFieldStyle(.roundedBorder)
}
```

Example 3 (swift):
```swift
Form {
    TextField(text: $username, prompt: Text("Required")) {
        Text("Username")
    }
    .autocorrectionDisabled(true)
    #if !os(macOS)
    .textInputAutocapitalization(.never)
    #endif

    SecureField(text: $password, prompt: Text("Required")) {
        Text("Password")
    }
}
```

---

## Image

**URL:** https://sosumi.ai/documentation/swiftui/image?.md

**Contents:**
- Overview
  - Making images accessible
- Conforms To
- Creating an image
- Creating an image for use as a control
- Creating an image for decorative use
- Creating a system symbol image
- Creating an image from another image
- Creating an image from drawing instructions
- Resizing images

---
title: Image
description: A view that displays an image.
source: https://developer.apple.com/documentation/swiftui/image
timestamp: 2026-02-13T19:32:27.537Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that displays an image.

Use an `Image` instance when you want to add images to your SwiftUI app. You can create images from many sources:

- Image files in your app’s asset library or bundle. Supported types include PNG, JPEG, HEIC, and more.
- Instances of platform-specific image types, like [UIImage](/documentation/UIKit/UIImage) and [NSImage](/documentation/AppKit/NSImage).
- A bitmap stored in a Core Graphics [CGImage](/documentation/CoreGraphics/CGImage) instance.
- System graphics from the SF Symbols set.

The following example shows how to load an image from the app’s asset library or bundle and scale it to fit within its container:

You can use methods on the `Image` type as well as standard view modifiers to adjust the size of the image to fit your app’s interface. Here, the `Image` type’s [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)) method scales the image to fit the current view. Then, the [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:)) view modifier adjusts this resizing behavior to maintain the image’s original aspect ratio, rather than scaling the x- and y-axes independently to fill all four sides of the view. The article [Fitting-Images-into-Available](/documentation/swiftui/fitting-images-into-available-space) shows how to apply scaling, clipping, and tiling to `Image` instances of different sizes.

An `Image` is a late-binding token; the system resolves its actual value only when it’s about to use the image in an environment.

To use an image as a control, use one of the initializers that takes a `label` parameter. This allows the system’s accessibility frameworks to use the label as the name of the control for users who use features like VoiceOver. For images that are only present for aesthetic reasons, use an initializer with the `decorative` parameter; the accessibility systems ignore these images.

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [JournalingSuggestionAsset](/documentation/JournalingSuggestions/JournalingSuggestionAsset)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Transferable](/documentation/CoreTransferable/Transferable)
- [View](/documentation/swiftui/view)

- [init(_:bundle:)](/documentation/swiftui/image/init(_:bundle:)) Creates a labeled image that you can use as content for controls.
- [init(_:variableValue:bundle:)](/documentation/swiftui/image/init(_:variablevalue:bundle:)) Creates a labeled image that you can use as content for controls, with a variable value.
- [init(_:)](/documentation/swiftui/image/init(_:)) Initialize an  with an image resource.

- [init(_:bundle:label:)](/documentation/swiftui/image/init(_:bundle:label:)) Creates a labeled image that you can use as content for controls, with the specified label.
- [init(_:variableValue:bundle:label:)](/documentation/swiftui/image/init(_:variablevalue:bundle:label:)) Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(_:scale:orientation:label:)](/documentation/swiftui/image/init(_:scale:orientation:label:)) Creates a labeled image based on a Core Graphics image instance, usable as content for controls.

- [init(decorative:bundle:)](/documentation/swiftui/image/init(decorative:bundle:)) Creates an unlabeled, decorative image.
- [init(decorative:variableValue:bundle:)](/documentation/swiftui/image/init(decorative:variablevalue:bundle:)) Creates an unlabeled, decorative image, with a variable value.
- [init(decorative:scale:orientation:)](/documentation/swiftui/image/init(decorative:scale:orientation:)) Creates an unlabeled, decorative image based on a Core Graphics image instance.

- [init(systemName:)](/documentation/swiftui/image/init(systemname:)) Creates a system symbol image.
- [init(systemName:variableValue:)](/documentation/swiftui/image/init(systemname:variablevalue:)) Creates a system symbol image with a variable value.

- [init(uiImage:)](/documentation/swiftui/image/init(uiimage:)) Creates a SwiftUI image from a UIKit image instance.
- [init(nsImage:)](/documentation/swiftui/image/init(nsimage:)) Creates a SwiftUI image from an AppKit image instance.

- [init(size:label:opaque:colorMode:renderer:)](/documentation/swiftui/image/init(size:label:opaque:colormode:renderer:)) Initializes an image of the given size, with contents provided by a custom rendering closure.

- [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)) Sets the mode by which SwiftUI resizes an image to fit its space.

- [antialiased(_:)](/documentation/swiftui/image/antialiased(_:)) Specifies whether SwiftUI applies antialiasing when rendering the image.
- [symbolRenderingMode(_:)](/documentation/swiftui/image/symbolrenderingmode(_:)) Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](/documentation/swiftui/image/renderingmode(_:)) Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](/documentation/swiftui/image/interpolation(_:)) Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](/documentation/swiftui/image/templaterenderingmode) A type that indicates how SwiftUI renders images.
- [Image.Interpolation](/documentation/swiftui/image/interpolation) The level of quality for rendering an image that requires interpolation, such as a scaled image.

- [allowedDynamicRange(_:)](/documentation/swiftui/image/alloweddynamicrange(_:)) Returns a new image configured with the specified allowed dynamic range.
- [allowedDynamicRange](/documentation/swiftui/environmentvalues/alloweddynamicrange) The allowed dynamic range for the view, or nil.
- [Image.DynamicRange](/documentation/swiftui/image/dynamicrange)

- [symbolColorRenderingMode(_:)](/documentation/swiftui/image/symbolcolorrenderingmode(_:)) Sets the color rendering mode of the image.
- [symbolVariableValueMode(_:)](/documentation/swiftui/image/symbolvariablevaluemode(_:)) Sets the variable value mode mode for symbol images within this view.
- [widgetAccentedRenderingMode(_:)](/documentation/swiftui/image/widgetaccentedrenderingmode(_:)) Specifies the how to render an  when using the  mode.

- [Image.Orientation](/documentation/swiftui/image/orientation) The orientation of an image.
- [Image.ResizingMode](/documentation/swiftui/image/resizingmode) The modes that SwiftUI uses to resize an image to fit within its containing view.
- [Image.Scale](/documentation/swiftui/image/scale) A scale to apply to vector images relative to text.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Image
```

Example 2 (swift):
```swift
Image("Landscape_4")
    .resizable()
    .aspectRatio(contentMode: .fit)
Text("Water wheel")
```

---

## Section

**URL:** https://sosumi.ai/documentation/swiftui/section?.md

**Contents:**
- Overview
  - Collapsible sections
- Conforms To
- Creating a section
- Adding headers and footers
- Controlling collapsibility
- Deprecated symbols
- Organizing views into sections

---
title: Section
description: A container view that you can use to add hierarchy within certain views.
source: https://developer.apple.com/documentation/swiftui/section
timestamp: 2026-02-13T19:33:05.481Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container view that you can use to add hierarchy within certain views.

Use `Section` instances in views like [List](/documentation/swiftui/list), [Picker](/documentation/swiftui/picker), and [Form](/documentation/swiftui/form) to organize content into separate sections. Each section has custom content that you provide on a per-instance basis. You can also provide headers and footers for each section.

Create sections that expand and collapse by using an initializer that accepts an `isExpanded` binding. A collapsible section in a [List](/documentation/swiftui/list) that uses the [sidebar](/documentation/swiftui/liststyle/sidebar) style shows a disclosure indicator next to the section’s header. Tapping on the disclosure indicator toggles the appearance of the section’s content.

> [!NOTE]
> Not all contexts provide a default control to trigger collapse or expansion.

- [Copyable](/documentation/Swift/Copyable)
- [TableRowContent](/documentation/swiftui/tablerowcontent)
- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/section/init(content:)) Creates a section with the provided section content.
- [init(_:content:)](/documentation/swiftui/section/init(_:content:)) Creates a section with the provided section content.

- [init(content:header:)](/documentation/swiftui/section/init(content:header:)) Creates a section with a header and the provided section content.
- [init(content:footer:)](/documentation/swiftui/section/init(content:footer:)) Creates a section with a footer and the provided section content.
- [init(content:header:footer:)](/documentation/swiftui/section/init(content:header:footer:)) Creates a section with a header, footer, and the provided section content.

- [init(_:isExpanded:content:)](/documentation/swiftui/section/init(_:isexpanded:content:)) Creates a section with the provided section content.
- [init(isExpanded:content:header:)](/documentation/swiftui/section/init(isexpanded:content:header:)) Creates a section with a header, the provided section content, and a binding representing the section’s expansion state.

- [init(header:content:)](/documentation/swiftui/section/init(header:content:)) Creates a section with a header and the provided section content.
- [init(footer:content:)](/documentation/swiftui/section/init(footer:content:)) Creates a section with a footer and the provided section content.
- [init(header:footer:content:)](/documentation/swiftui/section/init(header:footer:content:)) Creates a section with a header, footer, and the provided section content.
- [collapsible(_:)](/documentation/swiftui/section/collapsible(_:)) Sets whether a section can be collapsed by the user.

- [SectionCollection](/documentation/swiftui/sectioncollection)
- [SectionConfiguration](/documentation/swiftui/sectionconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Section<Parent, Content, Footer>
```

---

## List

**URL:** https://sosumi.ai/documentation/swiftui/list?.md

**Contents:**
- Overview
  - Supporting selection in lists
  - Refreshing the list content
  - Supporting multidimensional lists
  - Creating hierarchical lists
  - Styling lists
- Conforms To
- Creating a list from a set of views
- Creating a list from enumerated data
- Creating a list from hierarchical data

---
title: List
description: A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.
source: https://developer.apple.com/documentation/swiftui/list
timestamp: 2026-02-13T19:33:07.527Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.

In its simplest form, a `List` creates its contents statically, as shown in the following example:

More commonly, you create lists dynamically from an underlying collection of data. The following example shows how to create a simple list from an array of an `Ocean` type which conforms to [Identifiable](/documentation/Swift/Identifiable):

To make members of a list selectable, provide a binding to a selection variable. Binding to a single instance of the list data’s `Identifiable.ID` type creates a single-selection list. Binding to a [Set](/documentation/Swift/Set) creates a list that supports multiple selections. The following example shows how to add multiselect to the previous example:

When people make a single selection by tapping or clicking, the selected cell changes its appearance to indicate the selection. To enable multiple selections with tap gestures, put the list into edit mode by either modifying the [edit Mode](/documentation/swiftui/environmentvalues/editmode) value, or adding an [Edit Button](/documentation/swiftui/editbutton) to your app’s interface. When you put the list into edit mode, the list shows a circle next to each list item. The circle contains a checkmark when the user selects the associated item. The example above uses an Edit button, which changes its title to Done while in edit mode:

People can make multiple selections without needing to enter edit mode on devices that have a keyboard and mouse or trackpad, like Mac and iPad.

To make the content of the list refreshable using the standard refresh control, use the [refreshable(action:)](/documentation/swiftui/view/refreshable(action:)) modifier.

The following example shows how to add a standard refresh control to a list. When the user drags the top of the list downward, SwiftUI reveals the refresh control and executes the specified action. Use an `await` expression inside the `action` closure to refresh your data. The refresh indicator remains visible for the duration of the awaited operation.

To create two-dimensional lists, group items inside [Section](/documentation/swiftui/section) instances. The following example creates sections named after the world’s oceans, each of which has [Text](/documentation/swiftui/text) views named for major seas attached to those oceans. The example also allows for selection of a single list item, identified by the `id` of the example’s `Sea` type.

Because this example uses single selection, people can make selections outside of edit mode on all platforms.

> [!NOTE]
> In iOS 15, iPadOS 15, and tvOS 15 and earlier, lists support selection only in edit mode, even for single selections.

You can also create a hierarchical list of arbitrary depth by providing tree-structured data and a `children` parameter that provides a key path to get the child nodes at any level. The following example uses a deeply-nested collection of a custom `FileItem` type to simulate the contents of a file system. The list created from this data uses collapsing cells to allow the user to navigate the tree structure.

SwiftUI chooses a display style for a list based on the platform and the view type in which it appears. Use the [listStyle(_:)](/documentation/swiftui/view/liststyle(_:)) modifier to apply a different [List Style](/documentation/swiftui/liststyle) to all lists within a view. For example, adding `.listStyle(.plain)` to the example shown in the “Creating Multidimensional Lists” topic applies the [plain](/documentation/swiftui/liststyle/plain) style, the following screenshot shows:

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/list/init(content:)) Creates a list with the given content.
- [init(selection:content:)](/documentation/swiftui/list/init(selection:content:)) Creates a list with the given content that supports selecting a single row that cannot be deselected.

- [init(_:rowContent:)](/documentation/swiftui/list/init(_:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:selection:rowContent:)](/documentation/swiftui/list/init(_:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](/documentation/swiftui/list/init(_:id:rowcontent:)) Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](/documentation/swiftui/list/init(_:id:selection:rowcontent:)) Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.

- [init(_:children:rowContent:)](/documentation/swiftui/list/init(_:children:rowcontent:)) Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data.
- [init(_:children:selection:rowContent:)](/documentation/swiftui/list/init(_:children:selection:rowcontent:)) Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data and allowing users to have exactly one row always selected.
- [init(_:id:children:rowContent:)](/documentation/swiftui/list/init(_:id:children:rowcontent:)) Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:children:selection:rowContent:)](/documentation/swiftui/list/init(_:id:children:selection:rowcontent:)) Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data and allowing users to have exactly one row always selected.

- [init(_:editActions:rowContent:)](/documentation/swiftui/list/init(_:editactions:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:editActions:selection:rowContent:)](/documentation/swiftui/list/init(_:editactions:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
- [init(_:id:editActions:rowContent:)](/documentation/swiftui/list/init(_:id:editactions:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:id:editActions:selection:rowContent:)](/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

- [body](/documentation/swiftui/list/body) The content of the list.

- [Displaying data in lists](/documentation/swiftui/displaying-data-in-lists)
- [listStyle(_:)](/documentation/swiftui/view/liststyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct List<SelectionValue, Content> where SelectionValue : Hashable, Content : View
```

Example 2 (swift):
```swift
var body: some View {
    List {
        Text("A List Item")
        Text("A Second List Item")
        Text("A Third List Item")
    }
}
```

Example 3 (swift):
```swift
struct Ocean: Identifiable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

var body: some View {
    List(oceans) {
        Text($0.name)
    }
}
```

Example 4 (swift):
```swift
struct Ocean: Identifiable, Hashable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

@State private var multiSelection = Set<UUID>()

var body: some View {
    NavigationView {
        List(oceans, selection: $multiSelection) {
            Text($0.name)
        }
        .navigationTitle("Oceans")
        .toolbar { EditButton() }
    }
    Text("\(multiSelection.count) selections")
}
```

---

## Slider

**URL:** https://sosumi.ai/documentation/swiftui/slider?.md

**Contents:**
- Overview
- Conforms To
- Creating a slider
- Creating a slider with labels
- Adding ticks to a slider
- Deprecated initializers
- Initializers
- Getting numeric inputs

---
title: Slider
description: A control for selecting a value from a bounded linear range of values.
source: https://developer.apple.com/documentation/swiftui/slider
timestamp: 2026-02-13T19:32:34.996Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+

> A control for selecting a value from a bounded linear range of values.

A slider consists of a “thumb” image that the user moves between two extremes of a linear “track”. The ends of the track represent the minimum and maximum possible values. As the user moves the thumb, the slider updates its bound value.

The following example shows a slider bound to the value `speed`. As the slider updates this value, a bound [Text](/documentation/swiftui/text) view shows the value updating. The `onEditingChanged` closure passed to the slider receives callbacks when the user drags the slider. The example uses this to change the color of the value text.

You can also use a `step` parameter to provide incremental steps along the path of the slider. For example, if you have a slider with a range of `0` to `100`, and you set the `step` value to `5`, the slider’s increments would be `0`, `5`, `10`, and so on. The following example shows this approach, and also adds optional minimum and maximum value labels.

The slider also uses the `step` to increase or decrease the value when a VoiceOver user adjusts the slider with voice commands.

- [View](/documentation/swiftui/view)

- [init(value:in:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:oneditingchanged:)) Creates a slider to select a value from a given range.
- [init(value:in:step:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:step:oneditingchanged:)) Creates a slider to select a value from a given range, subject to a step increment.

- [init(value:in:label:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:label:oneditingchanged:)) Creates a slider to select a value from a given range, which displays the provided label.
- [init(value:in:step:label:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:step:label:oneditingchanged:)) Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init(value:in:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:)) Creates a slider to select a value from a given range, which displays the provided labels.
- [init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:step:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:)) Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.

- [SliderTick](/documentation/swiftui/slidertick) A representation of a tick in a slider, with associated value and optional label.
- [SliderTickBuilder](/documentation/swiftui/slidertickbuilder) A result builder that constructs s for use when creating a .
- [SliderTickContentForEach](/documentation/swiftui/slidertickcontentforeach) A type of slider content that creates content by iterating over a collection.
- [TupleSliderTickContent](/documentation/swiftui/tupleslidertickcontent) Slider content created from a Swift tuple of slider content.
- [SliderTickContent](/documentation/swiftui/slidertickcontent) A type that provides content for a .

- [init(value:in:onEditingChanged:label:)](/documentation/swiftui/slider/init(value:in:oneditingchanged:label:)) Creates a slider to select a value from a given range, which displays the provided label.
- [init(value:in:step:onEditingChanged:label:)](/documentation/swiftui/slider/init(value:in:step:oneditingchanged:label:)) Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init(value:in:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)](/documentation/swiftui/slider/init(value:in:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:)) Creates a slider to select a value from a given range, which displays the provided labels.
- [init(value:in:step:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)](/documentation/swiftui/slider/init(value:in:step:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:)) Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.

- [init(value:in:neutralValue:enabledBounds:label:currentValueLabel:minimumValueLabel:maximumValueLabel:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:neutralvalue:enabledbounds:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:oneditingchanged:)) Creates a slider to select a value from a given range, which displays the provided labels.
- [init(value:in:neutralValue:enabledBounds:label:currentValueLabel:minimumValueLabel:maximumValueLabel:ticks:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:neutralvalue:enabledbounds:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:ticks:oneditingchanged:)) Creates a slider to select a value from a given range, which displays the provided labels and customized ticks.
- [init(value:in:step:neutralValue:enabledBounds:label:currentValueLabel:minimumValueLabel:maximumValueLabel:tick:onEditingChanged:)](/documentation/swiftui/slider/init(value:in:step:neutralvalue:enabledbounds:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:tick:oneditingchanged:)) Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels and customizable ticks.

- [Stepper](/documentation/swiftui/stepper)
- [Toggle](/documentation/swiftui/toggle)
- [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Slider<Label, ValueLabel> where Label : View, ValueLabel : View
```

Example 2 (swift):
```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    VStack {
        Slider(
            value: $speed,
            in: 0...100,
            onEditingChanged: { editing in
                isEditing = editing
            }
        )
        Text("\(speed)")
            .foregroundColor(isEditing ? .red : .blue)
    }
}
```

Example 3 (swift):
```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    Slider(
        value: $speed,
        in: 0...100,
        step: 5
    ) {
        Text("Speed")
    } minimumValueLabel: {
        Text("0")
    } maximumValueLabel: {
        Text("100")
    } onEditingChanged: { editing in
        isEditing = editing
    }
    Text("\(speed)")
        .foregroundColor(isEditing ? .red : .blue)
}
```

---

## TextField

**URL:** https://sosumi.ai/documentation/swiftui/textfield?.md

**Contents:**
- Overview
  - Text field prompts
  - Styling text fields
- Conforms To
- Creating a text field with a string
- Creating a scrollable text field
- Creating a text field with a value
- Deprecated initializers
- Initializers
- Getting text input

---
title: TextField
description: A control that displays an editable text interface.
source: https://developer.apple.com/documentation/swiftui/textfield
timestamp: 2026-02-13T19:32:42.763Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control that displays an editable text interface.

You create a text field with a label and a binding to a value. If the value is a string, the text field updates this value continuously as the user types or otherwise edits the text in the field. For non-string types, it updates the value when the user commits their edits, such as by pressing the Return key.

The following example shows a text field to accept a username, and a [Text](/documentation/swiftui/text) view below it that shadows the continuously updated value of `username`. The [Text](/documentation/swiftui/text) view changes color as the user begins and ends editing. When the user submits their completed entry to the text field, the [onSubmit(of:_:)](/documentation/swiftui/view/onsubmit(of:_:)) modifier calls an internal `validate(name:)` method.

The bound value doesn’t have to be a string. By using a [Format Style](/documentation/Foundation/FormatStyle), you can bind the text field to a nonstring type, using the format style to convert the typed text into an instance of the bound type. The following example uses a [Format Style](/documentation/Foundation/PersonNameComponents/FormatStyle) to convert the name typed in the text field to a [Person Name Components](/documentation/Foundation/PersonNameComponents) instance. A [Text](/documentation/swiftui/text) view below the text field shows the debug description string of this instance.

You can set an explicit prompt on the text field to guide users on what text they should provide. Each text field style determines where and when the text field uses a prompt and label. For example, a form on macOS always places the label at the leading edge of the field and uses a prompt, when available, as placeholder text within the field itself. In the same context on iOS, the text field uses either the prompt or label as placeholder text, depending on whether the initializer provided a prompt.

The following example shows a [Form](/documentation/swiftui/form) with two text fields, each of which provides a prompt to indicate that the field is required, and a view builder to provide a label:

SwiftUI provides a default text field style that reflects an appearance and behavior appropriate to the platform. The default style also takes the current context into consideration, like whether the text field is in a container that presents text fields with a special style. Beyond this, you can customize the appearance and interaction of text fields using the [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:)) modifier, passing in an instance of [Text Field Style](/documentation/swiftui/textfieldstyle). The following example applies the [rounded Border](/documentation/swiftui/textfieldstyle/roundedborder) style to both text fields within a [VStack](/documentation/swiftui/vstack).

- [View](/documentation/swiftui/view)

- [init(_:text:)](/documentation/swiftui/textfield/init(_:text:)) Creates a text field with a text label generated from a localized title string.
- [init(_:text:prompt:)](/documentation/swiftui/textfield/init(_:text:prompt:)) Creates a text field with a text label generated from a localized title string.
- [init(text:prompt:label:)](/documentation/swiftui/textfield/init(text:prompt:label:)) Creates a text field with a prompt generated from a .

- [init(_:text:axis:)](/documentation/swiftui/textfield/init(_:text:axis:)) Creates a text field with a preferred axis and a text label generated from a localized title string.
- [init(_:text:prompt:axis:)](/documentation/swiftui/textfield/init(_:text:prompt:axis:)) Creates a text field with a preferred axis and a text label generated from a localized title string.
- [init(text:prompt:axis:label:)](/documentation/swiftui/textfield/init(text:prompt:axis:label:)) Creates a text field with a preferred axis and a prompt generated from a .

- [init(_:value:format:prompt:)](/documentation/swiftui/textfield/init(_:value:format:prompt:)) Creates a text field that applies a format style to a bound value, with a label generated from a localized title string.
- [init(value:format:prompt:label:)](/documentation/swiftui/textfield/init(value:format:prompt:label:)) Creates a text field that applies a format style to a bound value, with a label generated from a view builder.
- [init(_:value:formatter:)](/documentation/swiftui/textfield/init(_:value:formatter:)) Create an instance which binds over an arbitrary type, .
- [init(_:value:formatter:prompt:)](/documentation/swiftui/textfield/init(_:value:formatter:prompt:)) Creates a text field that applies a formatter to a bound value, with a label generated from a title string.
- [init(value:formatter:prompt:label:)](/documentation/swiftui/textfield/init(value:formatter:prompt:label:)) Creates a text field that applies a formatter to a bound optional value, with a label generated from a view builder.

- [Deprecated initializers](/documentation/swiftui/textfield-deprecated) Review deprecated text field initializers.

- [init(_:text:selection:prompt:axis:)](/documentation/swiftui/textfield/init(_:text:selection:prompt:axis:)) Creates a text field with a binding to the current selection and a text label generated from a localized title string.
- [init(text:selection:prompt:axis:label:)](/documentation/swiftui/textfield/init(text:selection:prompt:axis:label:)) Creates a text field with a binding to the current selection and a prompt generated from a .

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:))
- [SecureField](/documentation/swiftui/securefield)
- [TextEditor](/documentation/swiftui/texteditor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TextField<Label> where Label : View
```

Example 2 (swift):
```swift
@State private var username: String = ""
@FocusState private var emailFieldIsFocused: Bool = false

var body: some View {
    TextField(
        "User name (email address)",
        text: $username
    )
    .focused($emailFieldIsFocused)
    .onSubmit {
        validate(name: username)
    }
    .textInputAutocapitalization(.never)
    .disableAutocorrection(true)
    .border(.secondary)

    Text(username)
        .foregroundColor(emailFieldIsFocused ? .red : .blue)
}
```

Example 3 (swift):
```swift
@State private var nameComponents = PersonNameComponents()

var body: some View {
    TextField(
        "Proper name",
        value: $nameComponents,
        format: .name(style: .medium)
    )
    .onSubmit {
        validate(components: nameComponents)
    }
    .disableAutocorrection(true)
    .border(.secondary)
    Text(nameComponents.debugDescription)
}
```

Example 4 (swift):
```swift
Form {
    TextField(text: $username, prompt: Text("Required")) {
        Text("Username")
    }
    SecureField(text: $password, prompt: Text("Required")) {
        Text("Password")
    }
}
```

---

## Text

**URL:** https://sosumi.ai/documentation/swiftui/text?.md

**Contents:**
- Overview
  - Localizing strings
- Conforms To
- Creating a text view
- Choosing a font
- Styling the view’s text
- Fitting text into available space
- Localizing text
- Configuring voiceover
- Providing accessibility information

---
title: Text
description: A view that displays one or more lines of read-only text.
source: https://developer.apple.com/documentation/swiftui/text
timestamp: 2026-02-13T19:32:23.467Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that displays one or more lines of read-only text.

A text view draws a string in your app’s user interface using a [body](/documentation/swiftui/font/body) font that’s appropriate for the current platform. You can choose a different standard font, like [title](/documentation/swiftui/font/title) or [caption](/documentation/swiftui/font/caption), using the [font(_:)](/documentation/swiftui/view/font(_:)) view modifier.

If you need finer control over the styling of the text, you can use the same modifier to configure a system font or choose a custom font. You can also apply view modifiers like [bold()](/documentation/swiftui/text/bold()) or [italic()](/documentation/swiftui/text/italic()) to further adjust the formatting.

To apply styling within specific portions of the text, you can create the text view from an [Attributed String](/documentation/Foundation/AttributedString), which in turn allows you to use Markdown to style runs of text. You can mix string attributes and SwiftUI modifiers, with the string attributes taking priority.

A text view always uses exactly the amount of space it needs to display its rendered contents, but you can affect the view’s layout. For example, you can use the [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:)) modifier to propose specific dimensions to the view. If the view accepts the proposal but the text doesn’t fit into the available space, the view uses a combination of wrapping, tightening, scaling, and truncation to make it fit. With a width of `100` points but no constraint on the height, a text view might wrap a long string:

Use modifiers like [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)), [allowsTightening(_:)](/documentation/swiftui/view/allowstightening(_:)), [minimumScaleFactor(_:)](/documentation/swiftui/view/minimumscalefactor(_:)), and [truncationMode(_:)](/documentation/swiftui/view/truncationmode(_:)) to configure how the view handles space constraints. For example, combining a fixed width and a line limit of `1` results in truncation for text that doesn’t fit in that space:

If you initialize a text view with a string literal, the view uses the [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) initializer, which interprets the string as a localization key and searches for the key in the table you specify, or in the default table if you don’t specify one.

For an app localized in both English and Spanish, the above view displays “pencil” and “lápiz” for English and Spanish users, respectively. If the view can’t perform localization, it displays the key instead. For example, if the same app lacks Danish localization, the view displays “pencil” for users in that locale. Similarly, an app that lacks any localization information displays “pencil” in any locale.

To explicitly bypass localization for a string literal, use the [init(verbatim:)](/documentation/swiftui/text/init(verbatim:)) initializer.

If you initialize a text view with a variable value, the view uses the [init(_:)](/documentation/swiftui/text/init(_:)-9d1g4) initializer, which doesn’t localize the string. However, you can request localization by creating a [Localized String Key](/documentation/swiftui/localizedstringkey) instance first, which triggers the [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) initializer instead:

When localizing a string variable, you can use the default table by omitting the optional initialization parameters — as in the above example — just like you might for a string literal.

When composing a complex string, where there is a need to assemble multiple pieces of text, use string interpolation:

This would look up the `"Hello, %@"` localization key in the localized string file and replace the format specifier `%@` with the value of `name` before rendering the text on screen.

Using string interpolation ensures that the text in your app can be localized correctly in all locales, especially in right-to-left languages.

If you desire to style only parts of interpolated text while ensuring that the content can still be localized correctly, interpolate `Text` or [Attributed String](/documentation/Foundation/AttributedString):

The example above uses [appendInterpolation(_:)](/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-4qyfo) and will look up the `"Hello, %@"` in the localized string file and interpolate a bold text rendering the value of  `name`.

Using [appendInterpolation(_:)](/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-5m52e) you can interpolate [Image](/documentation/swiftui/image) in text.

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) Creates a text view that displays localized content identified by a key.
- [init(_:)](/documentation/swiftui/text/init(_:)) Creates a text view that displays styled attributed content.
- [init(verbatim:)](/documentation/swiftui/text/init(verbatim:)) Creates a text view that displays a string literal without localization.
- [init(_:style:)](/documentation/swiftui/text/init(_:style:)) Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](/documentation/swiftui/text/init(_:format:)) Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](/documentation/swiftui/text/init(_:formatter:)) Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) Creates an instance that displays a timer counting within the provided interval.

- [font(_:)](/documentation/swiftui/text/font(_:)) Sets the default font for text in the view.
- [fontWeight(_:)](/documentation/swiftui/text/fontweight(_:)) Sets the font weight of the text.
- [fontDesign(_:)](/documentation/swiftui/text/fontdesign(_:)) Sets the font design of the text.
- [fontWidth(_:)](/documentation/swiftui/text/fontwidth(_:)) Sets the font width of the text.

- [foregroundStyle(_:)](/documentation/swiftui/text/foregroundstyle(_:)) Sets the style of the text displayed by this view.
- [bold()](/documentation/swiftui/text/bold()) Applies a bold or emphasized treatment to the fonts of the text.
- [bold(_:)](/documentation/swiftui/text/bold(_:)) Applies a bold font weight to the text.
- [italic()](/documentation/swiftui/text/italic()) Applies italics to the text.
- [italic(_:)](/documentation/swiftui/text/italic(_:)) Applies italics to the text.
- [strikethrough(_:color:)](/documentation/swiftui/text/strikethrough(_:color:)) Applies a strikethrough to the text.
- [strikethrough(_:pattern:color:)](/documentation/swiftui/text/strikethrough(_:pattern:color:)) Applies a strikethrough to the text.
- [underline(_:color:)](/documentation/swiftui/text/underline(_:color:)) Applies an underline to the text.
- [underline(_:pattern:color:)](/documentation/swiftui/text/underline(_:pattern:color:)) Applies an underline to the text.
- [monospaced(_:)](/documentation/swiftui/text/monospaced(_:)) Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](/documentation/swiftui/text/monospaceddigit()) Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [kerning(_:)](/documentation/swiftui/text/kerning(_:)) Sets the spacing, or kerning, between characters.
- [tracking(_:)](/documentation/swiftui/text/tracking(_:)) Sets the tracking for the text.
- [baselineOffset(_:)](/documentation/swiftui/text/baselineoffset(_:)) Sets the vertical offset for the text relative to its baseline.
- [Text.Case](/documentation/swiftui/text/case) A scheme for transforming the capitalization of characters within text.
- [Text.DateStyle](/documentation/swiftui/text/datestyle) A predefined style used to display a .
- [Text.LineStyle](/documentation/swiftui/text/linestyle) Description of the style used to draw the line for  and .

- [textScale(_:isEnabled:)](/documentation/swiftui/text/textscale(_:isenabled:)) Applies a text scale to the text.
- [Text.Scale](/documentation/swiftui/text/scale) Defines text scales
- [Text.TruncationMode](/documentation/swiftui/text/truncationmode) The type of truncation to apply to a line of text when it’s too long to fit in the available space.

- [typesettingLanguage(_:isEnabled:)](/documentation/swiftui/text/typesettinglanguage(_:isenabled:)) Specifies the language for typesetting.

- [speechAdjustedPitch(_:)](/documentation/swiftui/text/speechadjustedpitch(_:)) Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](/documentation/swiftui/text/speechalwaysincludespunctuation(_:)) Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](/documentation/swiftui/text/speechannouncementsqueued(_:)) Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](/documentation/swiftui/text/speechspellsoutcharacters(_:)) Sets whether VoiceOver should speak the contents of the text view character by character.

- [accessibilityHeading(_:)](/documentation/swiftui/text/accessibilityheading(_:)) Sets the accessibility level of this heading.
- [accessibilityLabel(_:)](/documentation/swiftui/text/accessibilitylabel(_:)) Adds a label to the view that describes its contents.
- [accessibilityTextContentType(_:)](/documentation/swiftui/text/accessibilitytextcontenttype(_:)) Sets an accessibility text content type.

- [+(_:_:)](/documentation/swiftui/text/+(_:_:)) Concatenates the text in two text views in a new text view.

- [foregroundColor(_:)](/documentation/swiftui/text/foregroundcolor(_:)) Sets the color of the text displayed by this view.

- [Text.AlignmentStrategy](/documentation/swiftui/text/alignmentstrategy) The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.
- [Text.Layout](/documentation/swiftui/text/layout) A value describing the layout and custom attributes of a tree of  views.
- [Text.LayoutKey](/documentation/swiftui/text/layoutkey) A preference key that provides the  values for all text views in the queried subtree.
- [Text.WritingDirectionStrategy](/documentation/swiftui/text/writingdirectionstrategy) The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.

- [customAttribute(_:)](/documentation/swiftui/text/customattribute(_:)) Adds a custom attribute to the text view.
- [textVariant(_:)](/documentation/swiftui/text/textvariant(_:)) Controls the way text size variants are chosen.

- [Label](/documentation/swiftui/label)
- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Text
```

Example 2 (swift):
```swift
Text("Hamlet")
    .font(.title)
```

Example 3 (swift):
```swift
Text("by William Shakespeare")
    .font(.system(size: 12, weight: .light, design: .serif))
    .italic()
```

Example 4 (swift):
```swift
let attributedString = try! AttributedString(
    markdown: "_Hamlet_ by William Shakespeare")

var body: some View {
    Text(attributedString)
        .font(.system(size: 12, weight: .light, design: .serif))
}
```

---

## Stepper

**URL:** https://sosumi.ai/documentation/swiftui/stepper?.md

**Contents:**
- Overview
- Conforms To
- Creating a stepper
- Creating a stepper over a range
- Creating a stepper with change behavior
- Deprecated initializers
- Getting numeric inputs

---
title: Stepper
description: A control that performs increment and decrement actions.
source: https://developer.apple.com/documentation/swiftui/stepper
timestamp: 2026-02-13T19:32:36.950Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 9.0+

> A control that performs increment and decrement actions.

Use a stepper control when you want the user to have granular control while incrementing or decrementing a value. For example, you can use a stepper to:

- Change a value up or down by `1`.
- Operate strictly over a prescribed range.
- Step by specific amounts over a stepper’s range of possible values.

The example below uses an array that holds a number of [Color](/documentation/swiftui/color) values, a local state variable, `value`, to set the control’s background color, and title label. When the user clicks or taps the stepper’s increment or decrement buttons, SwiftUI executes the relevant closure that updates `value`, wrapping the `value` to prevent overflow. SwiftUI then re-renders the view, updating the text and background color to match the current index:

The following example shows a stepper that displays the effect of incrementing or decrementing a value with the step size of `step` with the bounds defined by `range`:

- [View](/documentation/swiftui/view)

- [init(value:step:label:onEditingChanged:)](/documentation/swiftui/stepper/init(value:step:label:oneditingchanged:)) Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init(value:step:format:label:onEditingChanged:)](/documentation/swiftui/stepper/init(value:step:format:label:oneditingchanged:)) Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.
- [init(_:value:step:onEditingChanged:)](/documentation/swiftui/stepper/init(_:value:step:oneditingchanged:)) Creates a stepper with a title and configured to increment and decrement a binding to a value and step amount you provide.
- [init(_:value:step:format:onEditingChanged:)](/documentation/swiftui/stepper/init(_:value:step:format:oneditingchanged:)) Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.

- [init(value:in:step:label:onEditingChanged:)](/documentation/swiftui/stepper/init(value:in:step:label:oneditingchanged:)) Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init(value:in:step:format:label:onEditingChanged:)](/documentation/swiftui/stepper/init(value:in:step:format:label:oneditingchanged:)) Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:onEditingChanged:)](/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:)) Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.
- [init(_:value:in:step:format:onEditingChanged:)](/documentation/swiftui/stepper/init(_:value:in:step:format:oneditingchanged:)) Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.

- [init(label:onIncrement:onDecrement:onEditingChanged:)](/documentation/swiftui/stepper/init(label:onincrement:ondecrement:oneditingchanged:)) Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.
- [init(_:onIncrement:onDecrement:onEditingChanged:)](/documentation/swiftui/stepper/init(_:onincrement:ondecrement:oneditingchanged:)) Creates a stepper that uses a title key and executes the closures you provide when the user clicks or taps the stepper’s increment and decrement buttons.

- [init(value:step:onEditingChanged:label:)](/documentation/swiftui/stepper/init(value:step:oneditingchanged:label:)) Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init(value:in:step:onEditingChanged:label:)](/documentation/swiftui/stepper/init(value:in:step:oneditingchanged:label:)) Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init(onIncrement:onDecrement:onEditingChanged:label:)](/documentation/swiftui/stepper/init(onincrement:ondecrement:oneditingchanged:label:)) Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.

- [Slider](/documentation/swiftui/slider)
- [Toggle](/documentation/swiftui/toggle)
- [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Stepper<Label> where Label : View
```

Example 2 (swift):
```swift
struct StepperView: View {
    @State private var value = 0
    let colors: [Color] = [.orange, .red, .gray, .blue,
                           .green, .purple, .pink]

    func incrementStep() {
        value += 1
        if value >= colors.count { value = 0 }
    }

    func decrementStep() {
        value -= 1
        if value < 0 { value = colors.count - 1 }
    }

    var body: some View {
        Stepper {
            Text("Value: \(value) Color: \(colors[value].description)")
        } onIncrement: {
            incrementStep()
        } onDecrement: {
            decrementStep()
        }
        .padding(5)
        .background(colors[value])
    }
}
```

Example 3 (swift):
```swift
struct StepperView: View {
    @State private var value = 0
    let step = 5
    let range = 1...50

    var body: some View {
        Stepper(
            value: $value,
            in: range,
            step: step
        ) {
            Text("Current: \(value) in \(range.description) " +
                 "stepping by \(step)")
        }
        .padding(10)
    }
}
```

---

## Label

**URL:** https://sosumi.ai/documentation/swiftui/label?.md

**Contents:**
- Overview
- Conforms To
- Creating a label
- Displaying text

---
title: Label
description: A standard label for user interface items, consisting of an icon with a title.
source: https://developer.apple.com/documentation/swiftui/label
timestamp: 2026-02-13T19:32:25.519Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A standard label for user interface items, consisting of an icon with a title.

One of the most common and recognizable user interface components is the combination of an icon and a label. This idiom appears across many kinds of apps and shows up in collections, lists, menus of action items, and disclosable lists, just to name a few.

You create a label, in its simplest form, by providing a title and the name of an image, such as an icon from the [sf](/design/Human-Interface-Guidelines/sf-symbols) collection:

You can also apply styles to labels in several ways. In the case of dynamic changes to the view after device rotation or change to a window size you might want to show only the text portion of the label using the [title Only](/documentation/swiftui/labelstyle/titleonly) label style:

Conversely, there’s also an icon-only label style:

Some containers might apply a different default label style, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, you can apply the [title And Icon](/documentation/swiftui/labelstyle/titleandicon) label style:

You can also create a customized label style by modifying an existing style; this example adds a red border to the default label style:

For more extensive customization or to create a completely new label style, you’ll need to adopt the [Label Style](/documentation/swiftui/labelstyle) protocol and implement a [Label Style Configuration](/documentation/swiftui/labelstyleconfiguration) for the new style.

To apply a common label style to a group of labels, apply the style to the view hierarchy that contains the labels:

It’s also possible to make labels using views to compose the label’s icon programmatically, rather than using a pre-made image. In this example, the icon portion of the label uses a filled [Circle](/documentation/swiftui/circle) overlaid with the user’s initials:

- [View](/documentation/swiftui/view)

- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.
- [init(_:systemImage:)](/documentation/swiftui/label/init(_:systemimage:)) Creates a label with a system icon image and a title generated from a localized string.
- [init(title:icon:)](/documentation/swiftui/label/init(title:icon:)) Creates a label with a custom title and icon.
- [init(_:)](/documentation/swiftui/label/init(_:)) Creates a label representing a family activity application.
- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.

- [Text](/documentation/swiftui/text)
- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Label<Title, Icon> where Title : View, Icon : View
```

Example 2 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
```

Example 3 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.titleOnly)
```

Example 4 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.iconOnly)
```

---

## Menu

**URL:** https://sosumi.ai/documentation/swiftui/menu?.md

**Contents:**
- Overview
  - Primary action
  - Styling menus
- Conforms To
- Creating a menu from content
- Creating a menu with a primary action
- Creating a menu from a configuration
- Creating a menu

---
title: Menu
description: A control for presenting a menu of actions.
source: https://developer.apple.com/documentation/swiftui/menu
timestamp: 2026-02-13T19:32:53.049Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+

> A control for presenting a menu of actions.

The following example presents a menu of three buttons and a submenu, which contains three buttons of its own.

You can create the menu’s title with a [Localized String Key](/documentation/swiftui/localizedstringkey), as seen in the previous example, or with a view builder that creates multiple views, such as an image and a text view:

To support subtitles on menu items, initialize your `Button` with a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle. The same approach applies to other controls such as `Toggle`:

> [!NOTE]
> This behavior does not apply to buttons outside of a menu’s content.

Menus can be created with a custom primary action. The primary action will be performed when the user taps or clicks on the body of the control, and the menu presentation will happen on a secondary gesture, such as on long press or on click of the menu indicator. The following example creates a menu that adds bookmarks, with advanced options that are presented in a menu.

Use the [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)) modifier to change the style of all menus in a view. The following example shows how to apply a custom style:

- [View](/documentation/swiftui/view)

- [init(_:content:)](/documentation/swiftui/menu/init(_:content:)) Creates a menu that generates its label from a localized string key.
- [init(content:label:)](/documentation/swiftui/menu/init(content:label:)) Creates a menu with a custom label.
- [init(_:image:content:)](/documentation/swiftui/menu/init(_:image:content:)) Creates a menu that generates its label from a localized string key and image resource.
- [init(_:systemImage:content:)](/documentation/swiftui/menu/init(_:systemimage:content:)) Creates a menu that generates its label from a localized string key and system image.

- [init(_:content:primaryAction:)](/documentation/swiftui/menu/init(_:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(content:label:primaryAction:)](/documentation/swiftui/menu/init(content:label:primaryaction:)) Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](/documentation/swiftui/menu/init(_:image:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(_:systemImage:content:primaryAction:)](/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key and system image.

- [init(_:)](/documentation/swiftui/menu/init(_:)) Creates a menu based on a style configuration.

- [Populating SwiftUI menus with adaptive controls](/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls)
- [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Menu<Label, Content> where Label : View, Content : View
```

Example 2 (swift):
```swift
Menu("Actions") {
    Button("Duplicate", action: duplicate)
    Button("Rename", action: rename)
    Button("Delete…", action: delete)
    Menu("Copy") {
        Button("Copy", action: copy)
        Button("Copy Formatted", action: copyFormatted)
        Button("Copy Library Path", action: copyPath)
    }
}
```

Example 3 (swift):
```swift
Menu {
    Button("Open in Preview", action: openInPreview)
    Button("Save as PDF", action: saveAsPDF)
} label: {
    Label("PDF", systemImage: "doc.fill")
}
```

Example 4 (swift):
```swift
Menu {
    Button(action: openInPreview) {
        Text("Open in Preview")
        Text("View the document in Preview")
    }
    Button(action: saveAsPDF) {
        Text("Save as PDF")
        Text("Export the document as a PDF file")
    }
} label: {
    Label("PDF", systemImage: "doc.fill")
}
```

---

## Gauge

**URL:** https://sosumi.ai/documentation/swiftui/gauge?.md

**Contents:**
- Overview
- Conforms To
- Creating a gauge
- Indicating a value

---
title: Gauge
description: A view that shows a value within a range.
source: https://developer.apple.com/documentation/swiftui/gauge
timestamp: 2026-02-13T19:32:50.942Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+

> A view that shows a value within a range.

A gauge is a view that shows a current level of a value in relation to a specified finite capacity, very much like a fuel gauge in an automobile. Gauge displays are configurable; they can show any combination of the gauge’s current value, the range the gauge can display, and a label describing the purpose of the gauge itself.

In its most basic form, a gauge displays a single value along the path of the gauge mapped into a range from 0 to 100 percent. The example below sets the gauge’s indicator to a position 40 percent along the gauge’s path:

You can make a gauge more descriptive by describing its purpose, showing its current value and its start and end values. This example shows the gauge variant that accepts a range and adds labels using multiple trailing closures describing the current value and the minimum and maximum values of the gauge:

As shown above, the default style for gauges is a linear, continuous bar with an indicator showing the current value, and optional labels describing the gauge’s purpose, current, minimum, and maximum values.

> [!NOTE]
> Some visual presentations of `Gauge` don’t display all the labels required by the API. However, the accessibility system does use the label content and you should use these labels to fully describe the gauge for accessibility users.

To change the style of a gauge, use the [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:)) view modifier and supply an initializer for a specific gauge style. For example, to display the same gauge in a circular style, apply the [circular](/documentation/swiftui/gaugestyle/circular) style to the view:

To style elements of a gauge’s presentation, you apply view modifiers to the elements that you want to change. In the example below, the current value, minimum and maximum value labels have custom colors:

You can further style a gauge’s appearance by supplying a tint color or a gradient to the style’s initializer. The following example shows the effect of a gradient in the initialization of a [Circular Gauge Style](/documentation/swiftui/circulargaugestyle) gauge with a colorful gradient across the length of the gauge:

- [View](/documentation/swiftui/view)

- [init(value:in:label:)](/documentation/swiftui/gauge/init(value:in:label:)) Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init(value:in:label:currentValueLabel:)](/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:)) Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.
- [init(value:in:label:currentValueLabel:markedValueLabels:)](/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:markedvaluelabels:)) Creates a gauge representing a value within a range.
- [init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)](/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:)) Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
- [init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)](/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:)) Creates a gauge representing a value within a range.

- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:))
- [ProgressView](/documentation/swiftui/progressview)
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:))
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Gauge<Label, CurrentValueLabel, BoundsLabel, MarkedValueLabels> where Label : View, CurrentValueLabel : View, BoundsLabel : View, MarkedValueLabels : View
```

Example 2 (swift):
```swift
struct SimpleGauge: View {
    @State private var batteryLevel = 0.4

    var body: some View {
        Gauge(value: batteryLevel) {
            Text("Battery Level")
        }
    }
}
```

Example 3 (swift):
```swift
struct LabeledGauge: View {
    @State private var current = 67.0
    @State private var minValue = 0.0
    @State private var maxValue = 170.0

    var body: some View {
        Gauge(value: current, in: minValue...maxValue) {
            Text("BPM")
        } currentValueLabel: {
            Text("\(Int(current))")
        } minimumValueLabel: {
            Text("\(Int(minValue))")
        } maximumValueLabel: {
            Text("\(Int(maxValue))")
        }
    }
}
```

Example 4 (swift):
```swift
struct LabeledGauge: View {
    @State private var current = 67.0
    @State private var minValue = 0.0
    @State private var maxValue = 170.0

    var body: some View {
        Gauge(value: current, in: minValue...maxValue) {
            Text("BPM")
        } currentValueLabel: {
            Text("\(Int(current))")
        } minimumValueLabel: {
            Text("\(Int(minValue))")
        } maximumValueLabel: {
            Text("\(Int(maxValue))")
        }
        .gaugeStyle(.circular)
    }
}
```

---

## DatePicker

**URL:** https://sosumi.ai/documentation/swiftui/datepicker?.md

**Contents:**
- Overview
  - Styling date pickers
- Conforms To
- Creating a date picker for any date
- Creating a date picker for specific dates
- Setting date picker components
- Choosing dates

---
title: DatePicker
description: A control for selecting an absolute date.
source: https://developer.apple.com/documentation/swiftui/datepicker
timestamp: 2026-02-13T19:32:40.894Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+

> A control for selecting an absolute date.

Use a `DatePicker` when you want to provide a view that allows the user to select a calendar date, and optionally a time. The view binds to a [Date](/documentation/Foundation/Date) instance.

The following example creates a basic `DatePicker`, which appears on iOS as text representing the date. This example limits the display to only the calendar date, not the time. When the user taps or clicks the text, a calendar view animates in, from which the user can select a date. When the user dismisses the calendar view, the view updates the bound [Date](/documentation/Foundation/Date).

For cases where adding a subtitle to the label is desired, use a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle:

You can limit the `DatePicker` to specific ranges of dates, allowing selections only before or after a certain date, or between two dates. The following example shows a date-and-time picker that only permits selections within the year 2021 (in the `UTC` time zone).

To use a different style of date picker, use the [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:)) view modifier. The following example shows the graphical date picker style.

- [View](/documentation/swiftui/view)

- [init(_:selection:displayedComponents:)](/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:)) Creates an instance that selects a  with an unbounded range.
- [init(selection:displayedComponents:label:)](/documentation/swiftui/datepicker/init(selection:displayedcomponents:label:)) Creates an instance that selects a  with an unbounded range.

- [init(_:selection:in:displayedComponents:)](/documentation/swiftui/datepicker/init(_:selection:in:displayedcomponents:)) Creates an instance that selects a  in a closed range.
- [init(selection:in:displayedComponents:label:)](/documentation/swiftui/datepicker/init(selection:in:displayedcomponents:label:)) Creates an instance that selects a  in a closed range.

- [DatePicker.Components](/documentation/swiftui/datepicker/components)
- [DatePickerComponents](/documentation/swiftui/datepickercomponents)

- [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:))
- [MultiDatePicker](/documentation/swiftui/multidatepicker)
- [calendar](/documentation/swiftui/environmentvalues/calendar)
- [timeZone](/documentation/swiftui/environmentvalues/timezone)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct DatePicker<Label> where Label : View
```

Example 2 (swift):
```swift
@State private var date = Date()

var body: some View {
    DatePicker(
        "Start Date",
        selection: $date,
        displayedComponents: [.date]
    )
}
```

Example 3 (swift):
```swift
@State private var date = Date()

var body: some View {
    DatePicker(selection: $date) {
        Text("Start Date")
        Text("Select the starting date for the event")
    }
}
```

Example 4 (swift):
```swift
@State private var date = Date()
let dateRange: ClosedRange<Date> = {
    let calendar = Calendar.current
    let startComponents = DateComponents(year: 2021, month: 1, day: 1)
    let endComponents = DateComponents(year: 2021, month: 12, day: 31, hour: 23, minute: 59, second: 59)
    return calendar.date(from:startComponents)!
        ...
        calendar.date(from:endComponents)!
}()

var body: some View {
    DatePicker(
        "Start Date",
         selection: $date,
         in: dateRange,
         displayedComponents: [.date, .hourAndMinute]
    )
}
```

---

## GlassProminentButtonStyle

**URL:** https://sosumi.ai/documentation/swiftui/glassprominentbuttonstyle?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Instance Methods
- Styling views with Liquid Glass

---
title: GlassProminentButtonStyle
description: A button style that applies prominent glass border artwork based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle
timestamp: 2026-02-13T19:37:08.395Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies prominent glass border artwork based on the button’s context.

You can also use [glass Prominent](/documentation/swiftui/primitivebuttonstyle/glassprominent) to construct this style.

- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle)

- [init()](/documentation/swiftui/glassprominentbuttonstyle/init()) Creates a prominent glass button style.

- [makeBody(configuration:)](/documentation/swiftui/glassprominentbuttonstyle/makebody(configuration:)) Creates a view that represents the body of a button.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GlassProminentButtonStyle
```

---

## Link

**URL:** https://sosumi.ai/documentation/swiftui/link?.md

**Contents:**
- Overview
- Conforms To
- Creating a link
- Linking to other content

---
title: Link
description: A control for navigating to a URL.
source: https://developer.apple.com/documentation/swiftui/link
timestamp: 2026-02-13T19:32:55.057Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A control for navigating to a URL.

Create a link by providing a destination URL and a title. The title tells the user the purpose of the link, and can be a string, a title key that produces a localized string, or a view that acts as a label. The example below creates a link to `example.com` and displays the title string as a link-styled view:

When a user taps or clicks a `Link`, the default behavior depends on the contents of the URL. For example, SwiftUI opens a Universal Link in the associated app if possible, or in the user’s default web browser if not. Alternatively, you can override the default behavior by setting the [open URL](/documentation/swiftui/environmentvalues/openurl) environment value with a custom [Open URLAction](/documentation/swiftui/openurlaction):

As with other views, you can style links using standard view modifiers depending on the view type of the link’s label. For example, a [Text](/documentation/swiftui/text) label could be modified with a custom [font(_:)](/documentation/swiftui/view/font(_:)) or [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)) to customize the appearance of the link in your app’s UI.

- [View](/documentation/swiftui/view)

- [init(_:destination:)](/documentation/swiftui/link/init(_:destination:)) Creates a control, consisting of a URL and a title key, used to navigate to a URL.
- [init(destination:label:)](/documentation/swiftui/link/init(destination:label:)) Creates a control, consisting of a URL and a label, used to navigate to the given URL.

- [ShareLink](/documentation/swiftui/sharelink)
- [SharePreview](/documentation/swiftui/sharepreview)
- [TextFieldLink](/documentation/swiftui/textfieldlink)
- [HelpLink](/documentation/swiftui/helplink)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct Link<Label> where Label : View
```

Example 2 (swift):
```swift
Link("View Our Terms of Service",
      destination: URL(string: "https://www.example.com/TOS.html")!)
```

Example 3 (swift):
```swift
Link("Visit Our Site", destination: URL(string: "https://www.example.com")!)
    .environment(\.openURL, OpenURLAction { url in
        print("Open \(url)")
        return .handled
    })
```

---

## Toggle

**URL:** https://sosumi.ai/documentation/swiftui/toggle?.md

**Contents:**
- Overview
  - Styling toggles
- Conforms To
- Creating a toggle
- Creating a toggle for a collection
- Creating a toggle from a configuration
- Creating a toggle for an App Intent
- Getting numeric inputs

---
title: Toggle
description: A control that toggles between on and off states.
source: https://developer.apple.com/documentation/swiftui/toggle
timestamp: 2026-02-13T19:32:32.972Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control that toggles between on and off states.

You create a toggle by providing an `isOn` binding and a label. Bind `isOn` to a Boolean property that determines whether the toggle is on or off. Set the label to a view that visually describes the purpose of switching between toggle states. For example:

For the common case of [Label](/documentation/swiftui/label) based labels, you can use the convenience initializer that takes a title string (or localized string key) and the name of a system image:

For text-only labels, you can use the convenience initializer that takes a title string (or localized string key) as its first parameter, instead of a trailing closure:

For cases where adding a subtitle to the label is desired, use a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle:

> [!NOTE]
> This behavior does not apply to [button](/documentation/swiftui/togglestyle/button).

Toggles use a default style that varies based on both the platform and the context. For more information, read about the [automatic](/documentation/swiftui/togglestyle/automatic) toggle style.

You can customize the appearance and interaction of toggles by applying styles using the [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:)) modifier. You can apply built-in styles, like [switch](/documentation/swiftui/togglestyle/switch), to either a toggle, or to a view hierarchy that contains toggles:

You can also define custom styles by creating a type that conforms to the [Toggle Style](/documentation/swiftui/togglestyle) protocol.

- [View](/documentation/swiftui/view)

- [init(_:isOn:)](/documentation/swiftui/toggle/init(_:ison:)) Creates a toggle that generates its label from a localized string key.
- [init(isOn:label:)](/documentation/swiftui/toggle/init(ison:label:)) Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](/documentation/swiftui/toggle/init(_:image:ison:)) Creates a toggle that generates its label from a localized string key and image resource.
- [init(_:systemImage:isOn:)](/documentation/swiftui/toggle/init(_:systemimage:ison:)) Creates a toggle that generates its label from a localized string key and system image.

- [init(_:sources:isOn:)](/documentation/swiftui/toggle/init(_:sources:ison:)) Creates a toggle representing a collection of values that generates its label from a localized string key.
- [init(sources:isOn:label:)](/documentation/swiftui/toggle/init(sources:ison:label:)) Creates a toggle representing a collection of values with a custom label.
- [init(_:image:sources:isOn:)](/documentation/swiftui/toggle/init(_:image:sources:ison:)) Creates a toggle representing a collection of values that generates its label from a localized string key and image resource.
- [init(_:systemImage:sources:isOn:)](/documentation/swiftui/toggle/init(_:systemimage:sources:ison:)) Creates a toggle representing a collection of values that generates its label from a localized string key and system image.

- [init(_:)](/documentation/swiftui/toggle/init(_:)) Creates a toggle based on a toggle style configuration.

- [init(isOn:intent:label:)](/documentation/swiftui/toggle/init(ison:intent:label:)) Creates a toggle performing an .
- [init(_:isOn:intent:)](/documentation/swiftui/toggle/init(_:ison:intent:)) Creates a toggle performing an  and generates its label from a localized string key.

- [Slider](/documentation/swiftui/slider)
- [Stepper](/documentation/swiftui/stepper)
- [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Toggle<Label> where Label : View
```

Example 2 (swift):
```swift
@State private var vibrateOnRing = false

var body: some View {
    Toggle(isOn: $vibrateOnRing) {
        Text("Vibrate on Ring")
    }
}
```

Example 3 (swift):
```swift
@State private var vibrateOnRing = true

var body: some View {
    Toggle(
        "Vibrate on Ring",
        systemImage: "dot.radiowaves.left.and.right",
        isOn: $vibrateOnRing
    )
}
```

Example 4 (swift):
```swift
@State private var vibrateOnRing = true

var body: some View {
    Toggle("Vibrate on Ring", isOn: $vibrateOnRing)
}
```

---

## Form

**URL:** https://sosumi.ai/documentation/swiftui/form?.md

**Contents:**
- Overview
- Conforms To
- Creating a form
- Creating a form from a configuration
- Grouping inputs

---
title: Form
description: A container for grouping controls used for data entry, such as in settings or inspectors.
source: https://developer.apple.com/documentation/swiftui/form
timestamp: 2026-02-13T19:33:01.217Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container for grouping controls used for data entry, such as in settings or inspectors.

SwiftUI applies platform-appropriate styling to views contained inside a form, to group them together. Form-specific styling applies to things like buttons, toggles, labels, lists, and more. Keep in mind that these stylings may be platform-specific. For example, forms appear as grouped lists on iOS, and as aligned vertical stacks on macOS.

The following example shows a simple data entry form on iOS, grouped into two sections. The supporting types (`NotifyMeAboutType` and `ProfileImageSize`) and state variables (`notifyMeAbout`, `profileImageSize`, `playNotificationSounds`, and `sendReadReceipts`) are omitted for simplicity.

On macOS, a similar form renders as a vertical stack. To adhere to macOS platform conventions, this version doesn’t use sections, and uses colons at the end of its labels. It also sets the picker to use the [inline](/documentation/swiftui/pickerstyle/inline) style, which produces radio buttons on macOS.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/form/init(content:)) Creates a form with the provided content.

- [init(_:)](/documentation/swiftui/form/init(_:)) Creates a form based on a form style configuration.

- [formStyle(_:)](/documentation/swiftui/view/formstyle(_:))
- [LabeledContent](/documentation/swiftui/labeledcontent)
- [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Form<Content> where Content : View
```

Example 2 (swift):
```swift
var body: some View {
    NavigationView {
        Form {
            Section(header: Text("Notifications")) {
                Picker("Notify Me About", selection: $notifyMeAbout) {
                    Text("Direct Messages").tag(NotifyMeAboutType.directMessages)
                    Text("Mentions").tag(NotifyMeAboutType.mentions)
                    Text("Anything").tag(NotifyMeAboutType.anything)
                }
                Toggle("Play notification sounds", isOn: $playNotificationSounds)
                Toggle("Send read receipts", isOn: $sendReadReceipts)
            }
            Section(header: Text("User Profiles")) {
                Picker("Profile Image Size", selection: $profileImageSize) {
                    Text("Large").tag(ProfileImageSize.large)
                    Text("Medium").tag(ProfileImageSize.medium)
                    Text("Small").tag(ProfileImageSize.small)
                }
                Button("Clear Image Cache") {}
            }
        }
    }
}
```

Example 3 (swift):
```swift
var body: some View {
    Spacer()
    HStack {
        Spacer()
        Form {
            Picker("Notify Me About:", selection: $notifyMeAbout) {
                Text("Direct Messages").tag(NotifyMeAboutType.directMessages)
                Text("Mentions").tag(NotifyMeAboutType.mentions)
                Text("Anything").tag(NotifyMeAboutType.anything)
            }
            Toggle("Play notification sounds", isOn: $playNotificationSounds)
            Toggle("Send read receipts", isOn: $sendReadReceipts)

            Picker("Profile Image Size:", selection: $profileImageSize) {
                Text("Large").tag(ProfileImageSize.large)
                Text("Medium").tag(ProfileImageSize.medium)
                Text("Small").tag(ProfileImageSize.small)
            }
            .pickerStyle(.inline)

            Button("Clear Image Cache") {}
        }
        Spacer()
    }
    Spacer()
}
```

---

## GlassButtonStyle

**URL:** https://sosumi.ai/documentation/swiftui/glassbuttonstyle?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Instance Methods
- Styling views with Liquid Glass

---
title: GlassButtonStyle
description: A button style that applies glass border artwork based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/glassbuttonstyle
timestamp: 2026-02-13T19:37:06.323Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies glass border artwork based on the button’s context.

You can also use [glass](/documentation/swiftui/primitivebuttonstyle/glass) to construct this style.

- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle)

- [init()](/documentation/swiftui/glassbuttonstyle/init()) Creates a glass button style.
- [init(_:)](/documentation/swiftui/glassbuttonstyle/init(_:))

- [makeBody(configuration:)](/documentation/swiftui/glassbuttonstyle/makebody(configuration:)) Creates a view that represents the body of a button.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GlassButtonStyle
```

---

## Picker

**URL:** https://sosumi.ai/documentation/swiftui/picker?.md

**Contents:**
- Overview
  - Iterating over a picker’s options
  - Styling pickers
- Conforms To
- Creating a picker
- Creating a picker for a collection
- Creating a picker with an image label
- Deprecated initializers
- Initializers
- Choosing from a set of options

---
title: Picker
description: A control for selecting from a set of mutually exclusive values.
source: https://developer.apple.com/documentation/swiftui/picker
timestamp: 2026-02-13T19:32:38.911Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control for selecting from a set of mutually exclusive values.

You create a picker by providing a selection binding, a label, and the content for the picker to display. Set the `selection` parameter to a bound property that provides the value to display as the current selection. Set the label to a view that visually describes the purpose of selecting content in the picker, and then provide the content for the picker to display.

For example, consider an enumeration of ice cream flavors and a [State](/documentation/swiftui/state) variable to hold the selected flavor:

You can create a picker to select among the values by providing a label, a binding to the current selection, and a collection of views for the picker’s content. Append a tag to each of these content views using the `View/tag(_:)` view modifier so that the type of each selection matches the type of the bound state variable:

If you provide a string label for the picker, as the example above does, the picker uses it to initialize a [Text](/documentation/swiftui/text) view as a label. Alternatively, you can use the [init(selection:content:label:)](/documentation/swiftui/picker/init(selection:content:label:)) initializer to compose the label from other views. The exact appearance of the picker depends on the context. If you use a picker in a [List](/documentation/swiftui/list) in iOS, it appears in a row with the label and selected value, and a chevron to indicate that you can tap the row to select a new value:

For cases where adding a subtitle to the label is desired, use a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle:

To provide selection values for the `Picker` without explicitly listing each option, you can create the picker with a [For Each](/documentation/swiftui/foreach):

[For Each](/documentation/swiftui/foreach) automatically assigns a tag to the selection views using each option’s `id`. This is possible because `Flavor` conforms to the [Identifiable](/documentation/Swift/Identifiable) protocol.

The example above relies on the fact that `Flavor` defines the type of its `id` parameter to exactly match the selection type. If that’s not the case, you need to override the tag. For example, consider a `Topping` type and a suggested topping for each flavor:

The following example shows a picker that’s bound to a `Topping` type, while the options are all `Flavor` instances. Each option uses the tag modifier to associate the suggested topping with the flavor it displays:

When the user selects chocolate, the picker sets `suggestedTopping` to the value in the associated tag:

Another example of when the views in a picker’s [For Each](/documentation/swiftui/foreach) need an explicit tag modifier is when you select over the cases of an enumeration that conforms to the [Identifiable](/documentation/Swift/Identifiable) protocol by using anything besides `Self` as the `id` parameter type. For example, a string enumeration might use the case’s `rawValue` string as the `id`. That identifier type doesn’t match the selection type, which is the type of the enumeration itself.

You can customize the appearance and interaction of pickers using styles that conform to the [Picker Style](/documentation/swiftui/pickerstyle) protocol, like [segmented](/documentation/swiftui/pickerstyle/segmented) or [menu](/documentation/swiftui/pickerstyle/menu). To set a specific style for all picker instances within a view, use the [pickerStyle(_:)](/documentation/swiftui/view/pickerstyle(_:)) modifier. The following example applies the [segmented](/documentation/swiftui/pickerstyle/segmented) style to two pickers that independently select a flavor and a topping:

- [View](/documentation/swiftui/view)

- [init(_:selection:content:)](/documentation/swiftui/picker/init(_:selection:content:)) Creates a picker that generates its label from a localized string key.
- [init(selection:content:label:)](/documentation/swiftui/picker/init(selection:content:label:)) Creates a picker that displays a custom label.

- [init(_:sources:selection:content:)](/documentation/swiftui/picker/init(_:sources:selection:content:)) Creates a picker bound to a collection of bindings that generates its label from a string.
- [init(sources:selection:content:label:)](/documentation/swiftui/picker/init(sources:selection:content:label:)) Creates a picker that displays a custom label.

- [init(_:image:selection:content:)](/documentation/swiftui/picker/init(_:image:selection:content:)) Creates a picker that generates its label from a localized string key and image resource
- [init(_:image:sources:selection:content:)](/documentation/swiftui/picker/init(_:image:sources:selection:content:)) Creates a picker bound to a collection of bindings that generates its label from a string and image resource.
- [init(_:systemImage:selection:content:)](/documentation/swiftui/picker/init(_:systemimage:selection:content:)) Creates a picker that generates its label from a localized string key and system image.
- [init(_:systemImage:sources:selection:content:)](/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:)) Creates a picker bound to a collection of bindings that generates its label from a string.

- [init(selection:label:content:)](/documentation/swiftui/picker/init(selection:label:content:)) Creates a picker that displays a custom label.

- [init(_:image:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:image:selection:content:currentvaluelabel:)) Creates a picker that accepts a custom current value label and generates its label from a localized string key and image resource
- [init(_:image:sources:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:image:sources:selection:content:currentvaluelabel:)) Creates a picker bound to a collection of bindings that accepts a custom current value label and generates its label from a string and image resource.
- [init(_:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:selection:content:currentvaluelabel:)) Creates a picker that generates its label from a localized string key and accepts a custom current value label.
- [init(_:sources:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:sources:selection:content:currentvaluelabel:)) Creates a picker bound to a collection of bindings that generates its label from a string and accepts a custom current value label.
- [init(_:systemImage:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:systemimage:selection:content:currentvaluelabel:)) Creates a picker that accepts a custom current value label and generates its label from a localized string key and system image.
- [init(_:systemImage:sources:selection:content:currentValueLabel:)](/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:currentvaluelabel:)) Creates a picker bound to a collection of bindings that accepts a custom current value label and generates its label from a string.
- [init(selection:content:label:currentValueLabel:)](/documentation/swiftui/picker/init(selection:content:label:currentvaluelabel:)) Creates a picker that displays a custom label and a custom value label where applicable.
- [init(sources:selection:content:label:currentValueLabel:)](/documentation/swiftui/picker/init(sources:selection:content:label:currentvaluelabel:)) Creates a picker that displays a custom label and current value label where applicable.

- [pickerStyle(_:)](/documentation/swiftui/view/pickerstyle(_:))
- [horizontalRadioGroupLayout()](/documentation/swiftui/view/horizontalradiogrouplayout())
- [defaultWheelPickerItemHeight(_:)](/documentation/swiftui/view/defaultwheelpickeritemheight(_:))
- [defaultWheelPickerItemHeight](/documentation/swiftui/environmentvalues/defaultwheelpickeritemheight)
- [paletteSelectionEffect(_:)](/documentation/swiftui/view/paletteselectioneffect(_:))
- [PaletteSelectionEffect](/documentation/swiftui/paletteselectioneffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Picker<Label, SelectionValue, Content> where Label : View, SelectionValue : Hashable, Content : View
```

Example 2 (swift):
```swift
enum Flavor: String, CaseIterable, Identifiable {
    case chocolate, vanilla, strawberry
    var id: Self { self }
}

@State private var selectedFlavor: Flavor = .chocolate
```

Example 3 (swift):
```swift
List {
    Picker("Flavor", selection: $selectedFlavor) {
        Text("Chocolate").tag(Flavor.chocolate)
        Text("Vanilla").tag(Flavor.vanilla)
        Text("Strawberry").tag(Flavor.strawberry)
    }
}
```

Example 4 (swift):
```swift
List {
    Picker(selection: $selectedFlavor) {
        Text("Chocolate").tag(Flavor.chocolate)
        Text("Vanilla").tag(Flavor.vanilla)
        Text("Strawberry").tag(Flavor.strawberry)
    } label: {
        Text("Flavor")
        Text("Choose your favorite flavor")
    }
}
```

---

## TextEditor

**URL:** https://sosumi.ai/documentation/swiftui/texteditor?.md

**Contents:**
- Overview
- Conforms To
- Creating a text editor
- Initializers
- Getting text input

---
title: TextEditor
description: A view that can display and edit long-form text.
source: https://developer.apple.com/documentation/swiftui/texteditor
timestamp: 2026-02-13T19:32:44.900Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> A view that can display and edit long-form text.

A text editor view allows you to display and edit multiline, scrollable text in your app’s user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [font(_:)](/documentation/swiftui/view/font(_:)), [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)), and [multilineTextAlignment(_:)](/documentation/swiftui/view/multilinetextalignment(_:)).

You create a text editor by adding a `TextEditor` instance to the body of your view, and initialize it by passing in a [Binding](/documentation/swiftui/binding) to a string variable in your app:

To style the text, use the standard view modifiers to configure a system font, set a custom font, or change the color of the view’s text.

In this example, the view renders the editor’s text in gray with a custom font:

If you want to change the spacing or font scaling aspects of the text, you can use modifiers like [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)), [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)), and [minimumScaleFactor(_:)](/documentation/swiftui/view/minimumscalefactor(_:)) to configure how the view displays text depending on the space constraints. For example, here the [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)) modifier sets the spacing between lines to 5 points:

- [View](/documentation/swiftui/view)

- [init(text:)](/documentation/swiftui/texteditor/init(text:)) Creates a plain text editor.

- [init(text:selection:)](/documentation/swiftui/texteditor/init(text:selection:)) Creates a styled text editor.

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [TextField](/documentation/swiftui/textfield)
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:))
- [SecureField](/documentation/swiftui/securefield)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TextEditor
```

Example 2 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
    }
}
```

Example 3 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
    }
}
```

Example 4 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

---
