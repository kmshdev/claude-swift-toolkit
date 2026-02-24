# Swiftui-Components - Reference

**Pages:** 92

---

## progressViewStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/progressviewstyle(_:)?.md

**Contents:**
- Parameters
- Discussion
- Indicating a value

---
title: progressViewStyle(_:)
description: Sets the style for progress views in this view.
source: https://developer.apple.com/documentation/swiftui/view/progressviewstyle(_:)
timestamp: 2026-02-13T19:36:09.539Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Sets the style for progress views in this view.

The progress view style to use for this view.

For example, the following code creates a progress view that uses the “circular” style:

- [Gauge](/documentation/swiftui/gauge)
- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:))
- [ProgressView](/documentation/swiftui/progressview)
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle
```

Example 2 (swift):
```swift
ProgressView()
    .progressViewStyle(.circular)
```

---

## fullScreenCover(isPresented:onDismiss:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/fullscreencover(ispresented:ondismiss:content:)?.md

**Contents:**
- Parameters
- Discussion
- Showing a sheet, cover, or popover

---
title: fullScreenCover(isPresented:onDismiss:content:)
description: Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
source: https://developer.apple.com/documentation/swiftui/view/fullscreencover(ispresented:ondismiss:content:)
timestamp: 2026-02-13T19:36:25.027Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.

A binding to a Boolean value that determines whether to present the sheet.

The closure to execute when dismissing the modal view.

A closure that returns the content of the modal view.

Use this method to show a modal view that covers as much of the screen as possible. The example below displays a custom view when the user toggles the value of the `isPresenting` binding:

- [sheet(isPresented:onDismiss:content:)](/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
- [sheet(item:onDismiss:content:)](/documentation/swiftui/view/sheet(item:ondismiss:content:))
- [fullScreenCover(item:onDismiss:content:)](/documentation/swiftui/view/fullscreencover(item:ondismiss:content:))
- [popover(item:attachmentAnchor:arrowEdge:content:)](/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
- [PopoverAttachmentAnchor](/documentation/swiftui/popoverattachmentanchor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

Example 2 (swift):
```swift
struct FullScreenCoverPresentedOnDismiss: View {
    @State private var isPresenting = false
    var body: some View {
        Button("Present Full-Screen Cover") {
            isPresenting.toggle()
        }
        .fullScreenCover(isPresented: $isPresenting,
                         onDismiss: didDismiss) {
            VStack {
                Text("A full-screen modal view.")
                    .font(.title)
                Text("Tap to Dismiss")
            }
            .onTapGesture {
                isPresenting.toggle()
            }
            .foregroundColor(.white)
            .frame(maxWidth: .infinity,
                   maxHeight: .infinity)
            .background(Color.blue)
            .ignoresSafeArea(edges: .all)
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }
}
```

---

## sensoryFeedback(_:trigger:)

**URL:** https://sosumi.ai/documentation/swiftui/view/sensoryFeedback(_:trigger:)?.md

**Contents:**
- Parameters
- Discussion
- Providing haptic feedback

---
title: sensoryFeedback(_:trigger:)
description: Plays the specified  when the provided  value changes.
source: https://developer.apple.com/documentation/swiftui/view/sensoryFeedback(_:trigger:)
timestamp: 2026-02-13T19:35:30.646Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+

> Plays the specified  when the provided  value changes.

Which type of feedback to play.

A value to monitor for changes to determine when to play.

For example, you could play feedback when a state value changes:

- [sensoryFeedback(trigger:_:)](/documentation/swiftui/view/sensoryfeedback(trigger:_:))
- [sensoryFeedback(_:trigger:condition:)](/documentation/swiftui/view/sensoryfeedback(_:trigger:condition:))
- [SensoryFeedback](/documentation/swiftui/sensoryfeedback)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T) -> some View where T : Equatable
```

Example 2 (swift):
```swift
struct MyView: View {
    @State private var showAccessory = false

    var body: some View {
        ContentView()
            .sensoryFeedback(.selection, trigger: showAccessory)
            .onLongPressGesture {
                showAccessory.toggle()
            }

        if showAccessory {
            AccessoryView()
        }
    }
}
```

---

## TabView

**URL:** https://sosumi.ai/documentation/swiftui/tabview?.md

**Contents:**
- Overview
  - Using tab sections
  - Changing tab structure between horizontal and regular size classes
  - Adding support for customization
- Conforms To
- Creating a tab view
- Configuring search activation
- Presenting views in tabs

---
title: TabView
description: A view that switches between multiple child views using interactive user interface elements.
source: https://developer.apple.com/documentation/swiftui/tabview
timestamp: 2026-02-13T19:33:13.184Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 7.0+

> A view that switches between multiple child views using interactive user interface elements.

To create a user interface with tabs, place [Tab](/documentation/swiftui/tab)s  in a `TabView`. On iOS, you can also use one of the badge modifiers, like [badge(_:)](/documentation/swiftui/tabcontent/badge(_:)), to assign a badge to each of the tabs.

The following example creates a tab view with three tabs, each presenting a custom child view. The first tab has a numeric badge and the third has a string badge.

To programmatically select different tabs, use the [init(selection:content:)](/documentation/swiftui/tabview/init(selection:content:)) initializer. You can assign a selection value to each tab using a `Tab` initializer that takes a value. Each tab should have a unique selection value and all tabs should have the same selection value type. When people select a tab in the tab view, the tab view updates the selection binding to the value of the currently selected tab.

The following example creates a tab view that supports programatic selection and has 3 tabs.

You can use the [page](/documentation/swiftui/tabviewstyle/page) style to display a tab view with multiple scrolling pages of content.

The following example uses a `ForEach` to create a scrolling tab view that shows the temperatures of various cities.

The [sidebar Adaptable](/documentation/swiftui/tabviewstyle/sidebaradaptable) style supports declaring a secondary tab hierarchy by grouping tabs with a [Tab Section](/documentation/swiftui/tabsection).

On iPadOS, tab sections appear in both the sidebar and the tab bar. On iOS and the horizontally compact size class on iPadOS, secondary tabs appear in the tab bar. When secondary tabs appear in the tab bar, the section header doesn’t appear in the tab bar. Consider limiting the number of tabs on iOS and the iPadOS horizontal compact size class so all tabs fit in the tab bar.

The following example has 5 tabs, three of which are grouped within a [Tab Section](/documentation/swiftui/tabsection).

The following example shows a `TabView` with 4 tabs in compact and 5 tabs in regular. In compact, one of the tabs is a ‘Browse’ tab that displays a custom list view. This list view allows navigating to the destinations that are contained within the ‘Library’ and ‘Playlists’ sections in the horizontally regular size class. The navigation path and the selection state are updated when the number of tabs changes.

You can allow people to customize the tabs in a `TabView` by using `sidebarAdaptable` style with the [tabViewCustomization(_:)](/documentation/swiftui/view/tabviewcustomization(_:)) modifier. Customization allows people to drag tabs from the sidebar to the tab bar, hide tabs, and rearrange tabs in the sidebar.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [disabled](/documentation/swiftui/tabcustomizationbehavior/disabled) behavior in all adaptable tab bar placements using [customizationBehavior(_:for:)](/documentation/swiftui/tabcontent/customizationbehavior(_:for:)).

On macOS, a default interaction is provided for reordering sections but not for controlling the visibility of individual tabs. A custom experience should be provided if desired by setting the visibility of the tab on the customization.

You can use `@AppStorage` or `@SceneStorage` to automatically persist any visibility or section order customizations a person makes.

The following example supports customizing all 4 tabs in the tab view and uses `@AppStorage` to persist the customizations a person makes.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/tabview/init(content:)) Creates a tab view that uses a builder to create its tabs.
- [init(selection:content:)](/documentation/swiftui/tabview/init(selection:content:)) Creates a tab view that uses a builder to create and specify selection values for its tabs.

- [TabSearchActivation](/documentation/swiftui/tabsearchactivation) Configures the activation behavior of search in the search tab.

- [Enhancing your app’s content with tab navigation](/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)
- [Tab](/documentation/swiftui/tab)
- [TabRole](/documentation/swiftui/tabrole)
- [TabSection](/documentation/swiftui/tabsection)
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TabView<SelectionValue, Content> where SelectionValue : Hashable, Content : View
```

Example 2 (swift):
```swift
TabView {
    Tab("Received", systemImage: "tray.and.arrow.down.fill") {
        ReceivedView()
    }
    .badge(2)

    Tab("Sent", systemImage: "tray.and.arrow.up.fill") {
        SentView()
    }

    Tab("Account", systemImage: "person.crop.circle.fill") {
        AccountView()
    }
    .badge("!")
}
```

Example 3 (swift):
```swift
TabView(selection: $selection) {
    Tab("Received", systemImage: "tray.and.arrow.down.fill", value: 0) {
        ReceivedView()
    }

    Tab("Sent", systemImage: "tray.and.arrow.up.fill", value: 1) {
        SentView()
    }

    Tab("Account", systemImage: "person.crop.circle.fill", value: 2) {
        AccountView()
    }
}
```

Example 4 (swift):
```swift
TabView {
    ForEach(cities) { city in
        TemperatureView(city)
    }
}
.tabViewStyle(.page)
```

---

## ButtonStyleConfiguration

**URL:** https://sosumi.ai/documentation/swiftui/buttonstyleconfiguration?.md

**Contents:**
- Configuring a button’s label
- Configuring a button’s interaction state
- Defining the button’s purpose
- Styling buttons

---
title: ButtonStyleConfiguration
description: The properties of a button.
source: https://developer.apple.com/documentation/swiftui/buttonstyleconfiguration
timestamp: 2026-02-13T19:36:19.998Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> The properties of a button.

- [label](/documentation/swiftui/buttonstyleconfiguration/label-swift.property) A view that describes the effect of pressing the button.
- [ButtonStyleConfiguration.Label](/documentation/swiftui/buttonstyleconfiguration/label-swift.struct) A type-erased label of a button.

- [isPressed](/documentation/swiftui/buttonstyleconfiguration/ispressed) A Boolean that indicates whether the user is currently pressing the button.

- [role](/documentation/swiftui/buttonstyleconfiguration/role) An optional semantic role that describes the button’s purpose.

- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:))
- [ButtonStyle](/documentation/swiftui/buttonstyle)
- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle)
- [PrimitiveButtonStyleConfiguration](/documentation/swiftui/primitivebuttonstyleconfiguration)
- [signInWithAppleButtonStyle(_:)](/documentation/swiftui/view/signinwithapplebuttonstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ButtonStyleConfiguration
```

---

## fixedSize(horizontal:vertical:)

**URL:** https://sosumi.ai/documentation/swiftui/view/fixedsize(horizontal:vertical:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Influencing a view’s size

---
title: fixedSize(horizontal:vertical:)
description: Fixes this view at its ideal size in the specified dimensions.
source: https://developer.apple.com/documentation/swiftui/view/fixedsize(horizontal:vertical:)
timestamp: 2026-02-13T19:32:11.315Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Fixes this view at its ideal size in the specified dimensions.

A Boolean value that indicates whether to fix the width of the view.

A Boolean value that indicates whether to fix the height of the view.

A view that fixes this view at its ideal size in the dimensions specified by `horizontal` and `vertical`.

This function behaves like [fixedSize()](/documentation/swiftui/view/fixedsize()), except with `fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally specified in one or both dimensions. For example, if you horizontally fix a text view before wrapping it in the frame view, you’re telling the text view to maintain its ideal *width*. The view calculates this to be the space needed to represent the entire string.

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func fixedSize(horizontal: Bool, vertical: Bool) -> some View
```

Example 2 (swift):
```swift
Text("A single line of text, too long to fit in a box.")
    .fixedSize(horizontal: true, vertical: false)
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

---

## ContainerRelativeShape

**URL:** https://sosumi.ai/documentation/swiftui/containerrelativeshape?.md

**Contents:**
- Conforms To
- Creating the shape
- Setting a container shape

---
title: ContainerRelativeShape
description: A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
source: https://developer.apple.com/documentation/swiftui/containerrelativeshape
timestamp: 2026-02-13T19:34:11.989Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.

- [Animatable](/documentation/swiftui/animatable)
- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/containerrelativeshape/init())

- [containerShape(_:)](/documentation/swiftui/view/containershape(_:))
- [InsettableShape](/documentation/swiftui/insettableshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct ContainerRelativeShape
```

---

## textFieldStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/textfieldstyle(_:)?.md

**Contents:**
- Getting text input

---
title: textFieldStyle(_:)
description: Sets the style for text fields within this view.
source: https://developer.apple.com/documentation/swiftui/view/textfieldstyle(_:)
timestamp: 2026-02-13T19:36:05.581Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for text fields within this view.

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [TextField](/documentation/swiftui/textfield)
- [SecureField](/documentation/swiftui/securefield)
- [TextEditor](/documentation/swiftui/texteditor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func textFieldStyle<S>(_ style: S) -> some View where S : TextFieldStyle
```

---

## toolbar(content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbar(content:)?.md

**Contents:**
- Parameters
- Discussion
- Populating a toolbar

---
title: toolbar(content:)
description: Populates the toolbar or navigation bar with the specified items.
source: https://developer.apple.com/documentation/swiftui/view/toolbar(content:)
timestamp: 2026-02-13T19:36:35.583Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Populates the toolbar or navigation bar with the specified items.

The items representing the content of the toolbar.

Use this method to populate a toolbar with a collection of views that you provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can provide either by supplying a collection of views with each view wrapped in a [Toolbar Item](/documentation/swiftui/toolbaritem), or by providing a collection of views as a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup). The example below uses a collection of [Toolbar Item](/documentation/swiftui/toolbaritem) views to create a macOS toolbar that supports text editing features:

Although it’s not mandatory, wrapping a related group of toolbar items together in a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup) provides a one-to-one mapping between controls and toolbar items which results in the correct layout and spacing on each platform. For design guidance on toolbars, see [toolbars](/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

Example 2 (swift):
```swift
struct StructToolbarItemGroupView: View {
    @State private var text = ""
    @State private var bold = false
    @State private var italic = false
    @State private var fontSize = 12.0

    var displayFont: Font {
        let font = Font.system(size: CGFloat(fontSize),
                               weight: bold == true ? .bold : .regular)
        return italic == true ? font.italic() : font
    }

    var body: some View {
        TextEditor(text: $text)
            .font(displayFont)
            .toolbar {
                ToolbarItemGroup {
                    Slider(
                        value: $fontSize,
                        in: 8...120,
                        minimumValueLabel:
                            Text("A").font(.system(size: 8)),
                        maximumValueLabel:
                            Text("A").font(.system(size: 16))
                    ) {
                        Text("Font Size (\(Int(fontSize)))")
                    }
                    .frame(width: 150)
                    Toggle(isOn: $bold) {
                        Image(systemName: "bold")
                    }
                    Toggle(isOn: $italic) {
                        Image(systemName: "italic")
                    }
                }
            }
            .navigationTitle("My Note")
    }
}
```

---

## Rectangle

**URL:** https://sosumi.ai/documentation/swiftui/rectangle?.md

**Contents:**
- Conforms To
- Creating a rectangle
- Creating rectangular shapes

---
title: Rectangle
description: A rectangular shape aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/rectangle
timestamp: 2026-02-13T19:34:07.822Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A rectangular shape aligned inside the frame of the view containing it.

- [Animatable](/documentation/swiftui/animatable)
- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/rectangle/init()) Creates a new rectangle shape.

- [RoundedRectangle](/documentation/swiftui/roundedrectangle)
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii)
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Rectangle
```

---

## onAppear(perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onappear(perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to view life cycle updates

---
title: onAppear(perform:)
description: Adds an action to perform before this view appears.
source: https://developer.apple.com/documentation/swiftui/view/onappear(perform:)
timestamp: 2026-02-13T19:34:57.110Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform before this view appears.

The action to perform. If `action` is `nil`, the call has no effect.

A view that triggers `action` before it appears.

The exact moment that SwiftUI calls this method depends on the specific view type that you apply it to, but the `action` closure completes before the first rendered frame appears.

- [onDisappear(perform:)](/documentation/swiftui/view/ondisappear(perform:))
- [task(priority:_:)](/documentation/swiftui/view/task(priority:_:))
- [task(id:priority:_:)](/documentation/swiftui/view/task(id:priority:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onAppear(perform action: (() -> Void)? = nil) -> some View
```

---

## ProgressView

**URL:** https://sosumi.ai/documentation/swiftui/progressview?.md

**Contents:**
- Overview
  - Styling progress views
- Conforms To
- Creating an indeterminate progress view
- Creating a determinate progress view
- Create a progress view spanning a date range
- Initializers
- Indicating a value

---
title: ProgressView
description: A view that shows the progress toward completion of a task.
source: https://developer.apple.com/documentation/swiftui/progressview
timestamp: 2026-02-13T19:32:48.887Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that shows the progress toward completion of a task.

Use a progress view to show that a task is incomplete but advancing toward completion. A progress view can show both determinate (percentage complete) and indeterminate (progressing or not) types of progress.

Create a determinate progress view by initializing a `ProgressView` with a binding to a numeric value that indicates the progress, and a `total` value that represents completion of the task. By default, the progress is `0.0` and the total is `1.0`.

The example below uses the state property `progress` to show progress in a determinate `ProgressView`. The progress view uses its default total of `1.0`, and because `progress` starts with an initial value of `0.5`, the progress view begins half-complete. A “More” button below the progress view allows people to increment the progress in increments of five percent:

To create an indeterminate progress view, use an initializer that doesn’t take a progress value:

You can also create a progress view that covers a closed range of [Date](/documentation/Foundation/Date) values. As long as the current date is within the range, the progress view automatically updates, filling or depleting the progress view as it nears the end of the range. The following example shows a five-minute timer whose start time is that of the progress view’s initialization:

You can customize the appearance and interaction of progress views by creating styles that conform to the [Progress View Style](/documentation/swiftui/progressviewstyle) protocol. To set a specific style for all progress view instances within a view, use the [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)) modifier. In the following example, a custom style adds a rounded pink border to all progress views within the enclosing [VStack](/documentation/swiftui/vstack):

SwiftUI provides two built-in progress view styles, [linear](/documentation/swiftui/progressviewstyle/linear) and [circular](/documentation/swiftui/progressviewstyle/circular), as well as an automatic style that defaults to the most appropriate style in the current context. The following example shows a circular progress view that starts at 60 percent completed.

On platforms other than macOS, the circular style may appear as an indeterminate indicator instead.

- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/progressview/init()) Creates a progress view for showing indeterminate progress, without a label.
- [init(label:)](/documentation/swiftui/progressview/init(label:)) Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(_:)](/documentation/swiftui/progressview/init(_:)-6k5se) Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init(_:)](/documentation/swiftui/progressview/init(_:)-3q5nf) Creates a progress view for showing indeterminate progress that generates its label from a string.

- [init(_:)](/documentation/swiftui/progressview/init(_:)-l5vj) Creates a progress view for visualizing the given progress instance.
- [init(value:total:)](/documentation/swiftui/progressview/init(value:total:)) Creates a progress view for showing determinate progress.
- [init(_:value:total:)](/documentation/swiftui/progressview/init(_:value:total:)) Creates a progress view for showing determinate progress that generates its label from a string.
- [init(value:total:label:)](/documentation/swiftui/progressview/init(value:total:label:)) Creates a progress view for showing determinate progress, with a custom label.
- [init(value:total:label:currentValueLabel:)](/documentation/swiftui/progressview/init(value:total:label:currentvaluelabel:)) Creates a progress view for showing determinate progress, with a custom label.

- [init(timerInterval:countsDown:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:)) Creates a progress view for showing continuous progress as time passes.
- [init(timerInterval:countsDown:label:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:label:)) Creates a progress view for showing continuous progress as time passes, with a descriptive label.
- [init(timerInterval:countsDown:label:currentValueLabel:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:label:currentvaluelabel:)) Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.

- [init(_:)](/documentation/swiftui/progressview/init(_:)) Creates a progress view based on a style configuration.

- [Gauge](/documentation/swiftui/gauge)
- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:))
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:))
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ProgressView<Label, CurrentValueLabel> where Label : View, CurrentValueLabel : View
```

Example 2 (swift):
```swift
struct LinearProgressDemoView: View {
    @State private var progress = 0.5

    var body: some View {
        VStack {
            ProgressView(value: progress)
            Button("More") { progress += 0.05 }
        }
    }
}
```

Example 3 (swift):
```swift
var body: some View {
    ProgressView()
}
```

Example 4 (swift):
```swift
struct DateRelativeProgressDemoView: View {
    let workoutDateRange = Date()...Date().addingTimeInterval(5*60)

    var body: some View {
         ProgressView(timerInterval: workoutDateRange) {
             Text("Workout")
         }
    }
}
```

---

## Path

**URL:** https://sosumi.ai/documentation/swiftui/path?.md

**Contents:**
- Conforms To
- Creating a path
- Getting the path’s characteristics
- Drawing a path
- Transforming the path
- Performing operations on the path
- Operating over path elements
- Applying a style
- Instance Methods

---
title: Path
description: The outline of a 2D shape.
source: https://developer.apple.com/documentation/swiftui/path
timestamp: 2026-02-13T19:34:16.288Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> The outline of a 2D shape.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [LosslessStringConvertible](/documentation/Swift/LosslessStringConvertible)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/path/init()) Creates an empty path.
- [init(_:)](/documentation/swiftui/path/init(_:)) Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn:)](/documentation/swiftui/path/init(ellipsein:)) Creates a path as an ellipse within the given rectangle.
- [init(roundedRect:cornerRadius:style:)](/documentation/swiftui/path/init(roundedrect:cornerradius:style:)) Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerSize:style:)](/documentation/swiftui/path/init(roundedrect:cornersize:style:)) Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerRadii:style:)](/documentation/swiftui/path/init(roundedrect:cornerradii:style:)) Creates a path as the given rounded rectangle, which may have uneven corner radii.

- [boundingRect](/documentation/swiftui/path/boundingrect) A rectangle containing all path segments.
- [cgPath](/documentation/swiftui/path/cgpath) An immutable path representing the elements in the path.
- [contains(_:eoFill:)](/documentation/swiftui/path/contains(_:eofill:)) Returns true if the path contains a specified point.
- [currentPoint](/documentation/swiftui/path/currentpoint) Returns the last point in the path, or nil if the path contains no points.
- [description](/documentation/swiftui/path/description) A description of the path that may be used to recreate the path via .
- [isEmpty](/documentation/swiftui/path/isempty) A Boolean value indicating whether the path contains zero elements.

- [move(to:)](/documentation/swiftui/path/move(to:)) Begins a new subpath at the specified point.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](/documentation/swiftui/path/addarc(center:radius:startangle:endangle:clockwise:transform:)) Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](/documentation/swiftui/path/addarc(tangent1end:tangent2end:radius:transform:)) Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](/documentation/swiftui/path/addcurve(to:control1:control2:)) Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addEllipse(in:transform:)](/documentation/swiftui/path/addellipse(in:transform:)) Adds an ellipse that fits inside the specified rectangle to the path.
- [addLine(to:)](/documentation/swiftui/path/addline(to:)) Appends a straight line segment from the current point to the specified point.
- [addLines(_:)](/documentation/swiftui/path/addlines(_:)) Adds a sequence of connected straight-line segments to the path.
- [addPath(_:transform:)](/documentation/swiftui/path/addpath(_:transform:)) Appends another path value to this path.
- [addQuadCurve(to:control:)](/documentation/swiftui/path/addquadcurve(to:control:)) Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addRect(_:transform:)](/documentation/swiftui/path/addrect(_:transform:)) Adds a rectangular subpath to the path.
- [addRects(_:transform:)](/documentation/swiftui/path/addrects(_:transform:)) Adds a set of rectangular subpaths to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](/documentation/swiftui/path/addrelativearc(center:radius:startangle:delta:transform:)) Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addRoundedRect(in:cornerSize:style:transform:)](/documentation/swiftui/path/addroundedrect(in:cornersize:style:transform:)) Adds a rounded rectangle to the path.
- [closeSubpath()](/documentation/swiftui/path/closesubpath()) Closes and completes the current subpath.

- [applying(_:)](/documentation/swiftui/path/applying(_:)) Returns a path constructed by applying the transform to all points of the path.
- [offsetBy(dx:dy:)](/documentation/swiftui/path/offsetby(dx:dy:)) Returns a path constructed by translating all its points.
- [trimmedPath(from:to:)](/documentation/swiftui/path/trimmedpath(from:to:)) Returns a partial copy of the path.

- [addRoundedRect(in:cornerSize:style:transform:)](/documentation/swiftui/path/addroundedrect(in:cornersize:style:transform:)) Adds a rounded rectangle to the path.
- [intersection(_:eoFill:)](/documentation/swiftui/path/intersection(_:eofill:)) Returns a new path with filled regions common to both paths.
- [lineIntersection(_:eoFill:)](/documentation/swiftui/path/lineintersection(_:eofill:)) Returns a new path with a line from this path that overlaps the filled regions of the given path.
- [lineSubtraction(_:eoFill:)](/documentation/swiftui/path/linesubtraction(_:eofill:)) Returns a new path with a line from this path that does not overlap the filled region of the given path.
- [normalized(eoFill:)](/documentation/swiftui/path/normalized(eofill:)) Returns a new weakly-simple copy of this path.
- [subtracting(_:eoFill:)](/documentation/swiftui/path/subtracting(_:eofill:)) Returns a new path with filled regions from this path that are not in the given path.
- [symmetricDifference(_:eoFill:)](/documentation/swiftui/path/symmetricdifference(_:eofill:)) Returns a new path with filled regions either from this path or the given path, but not in both.
- [union(_:eoFill:)](/documentation/swiftui/path/union(_:eofill:)) Returns a new path with filled regions in either this path or the given path.

- [forEach(_:)](/documentation/swiftui/path/foreach(_:)) Calls  with each element in the path.
- [Path.Element](/documentation/swiftui/path/element) An element of a path.

- [strokedPath(_:)](/documentation/swiftui/path/strokedpath(_:)) Returns a stroked copy of the path using  to define how the stroked outline is created.

- [addRoundedRect(in:cornerRadii:style:transform:)](/documentation/swiftui/path/addroundedrect(in:cornerradii:style:transform:)) Adds a rounded rectangle with uneven corners to the path.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Path
```

---

## Animation

**URL:** https://sosumi.ai/documentation/swiftui/animation?.md

**Contents:**
- Overview
- Conforms To
- Getting the default animation
- Getting linear animations
- Getting eased animations
- Getting built-in spring animations
- Customizing spring animations
- Creating custom animations
- Configuring an animation
- Instance Properties

---
title: Animation
description: The way a view changes over time to create a smooth visual transition from one state to another.
source: https://developer.apple.com/documentation/swiftui/animation
timestamp: 2026-02-13T19:34:52.874Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> The way a view changes over time to create a smooth visual transition from one state to another.

An `Animation` provides a visual transition of a view when a state value changes from one value to another. The characteristics of this transition vary according to the animation type. For instance, a [linear](/documentation/swiftui/animation/linear) animation provides a mechanical feel to the animation because its speed is consistent from start to finish. In contrast, an animation that uses easing, like [ease Out](/documentation/swiftui/animation/easeout), offers a more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the [animation(_:value:)](/documentation/swiftui/view/animation(_:value:)) modifier, and specify both an animation type and the value to animate. For instance, the [Circle](/documentation/swiftui/circle) view in the following code performs an [ease In](/documentation/swiftui/animation/easein) animation each time the state variable `scale` changes:

When the value of `scale` changes, the modifier [scaleEffect(_:anchor:)](/documentation/swiftui/view/scaleeffect(_:anchor:)) resizes [Circle](/documentation/swiftui/circle) according to the new value. SwiftUI can animate the transition between sizes because [Circle](/documentation/swiftui/circle) conforms to the [Shape](/documentation/swiftui/shape) protocol. Shapes in SwiftUI conform to the [Animatable](/documentation/swiftui/animatable) protocol, which describes how to animate a property of a view.

In addition to adding an animation to a view, you can also configure the animation by applying animation modifiers to the animation type. For example, you can:

- Delay the start of the animation by using the [delay(_:)](/documentation/swiftui/animation/delay(_:)) modifier.
- Repeat the animation by using the [repeatCount(_:autoreverses:)](/documentation/swiftui/animation/repeatcount(_:autoreverses:)) or [repeatForever(autoreverses:)](/documentation/swiftui/animation/repeatforever(autoreverses:)) modifiers.
- Change the speed of the animation by using the [speed(_:)](/documentation/swiftui/animation/speed(_:)) modifier.

For example, the [Circle](/documentation/swiftui/circle) view in the following code repeats the [ease In](/documentation/swiftui/animation/easein) animation three times by using the [repeatCount(_:autoreverses:)](/documentation/swiftui/animation/repeatcount(_:autoreverses:)) modifier:

A view can also perform an animation when a binding value changes. To specify the animation type on a binding, call its [animation(_:)](/documentation/swiftui/binding/animation(_:)) method. For example, the view in the following code performs a [linear](/documentation/swiftui/animation/linear) animation, moving the box truck between the leading and trailing edges of the view. The truck moves each time a person clicks the [Toggle](/documentation/swiftui/toggle) control, which changes the value of the `$isTrailing` binding.

- [Copyable](/documentation/Swift/Copyable)
- [CustomDebugStringConvertible](/documentation/Swift/CustomDebugStringConvertible)
- [CustomReflectable](/documentation/Swift/CustomReflectable)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [default](/documentation/swiftui/animation/default) A default animation instance.

- [linear](/documentation/swiftui/animation/linear) An animation that moves at a constant speed.
- [linear(duration:)](/documentation/swiftui/animation/linear(duration:)) An animation that moves at a constant speed during a specified duration.

- [easeIn](/documentation/swiftui/animation/easein) An animation that starts slowly and then increases speed towards the end of the movement.
- [easeIn(duration:)](/documentation/swiftui/animation/easein(duration:)) An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [easeOut](/documentation/swiftui/animation/easeout) An animation that starts quickly and then slows towards the end of the movement.
- [easeOut(duration:)](/documentation/swiftui/animation/easeout(duration:)) An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [easeInOut](/documentation/swiftui/animation/easeinout) An animation that combines the behaviors of in and out easing animations.
- [easeInOut(duration:)](/documentation/swiftui/animation/easeinout(duration:)) An animation with a specified duration that combines the behaviors of in and out easing animations.

- [bouncy](/documentation/swiftui/animation/bouncy) A spring animation with a predefined duration and higher amount of bounce.
- [bouncy(duration:extraBounce:)](/documentation/swiftui/animation/bouncy(duration:extrabounce:)) A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [smooth](/documentation/swiftui/animation/smooth) A smooth spring animation with a predefined duration and no bounce.
- [smooth(duration:extraBounce:)](/documentation/swiftui/animation/smooth(duration:extrabounce:)) A smooth spring animation with a predefined duration and no bounce that can be tuned.
- [snappy](/documentation/swiftui/animation/snappy) A spring animation with a predefined duration and small amount of bounce that feels more snappy.
- [snappy(duration:extraBounce:)](/documentation/swiftui/animation/snappy(duration:extrabounce:)) A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.

- [spring](/documentation/swiftui/animation/spring) A persistent spring animation. When mixed with other  or  animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [spring(_:blendDuration:)](/documentation/swiftui/animation/spring(_:blendduration:)) A persistent spring animation.
- [spring(duration:bounce:blendDuration:)](/documentation/swiftui/animation/spring(duration:bounce:blendduration:)) A persistent spring animation. When mixed with other  or  animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [spring(response:dampingFraction:blendDuration:)](/documentation/swiftui/animation/spring(response:dampingfraction:blendduration:)) A persistent spring animation. When mixed with other  or  animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [interactiveSpring](/documentation/swiftui/animation/interactivespring) A convenience for a  animation with a lower  value, intended for driving interactive animations.
- [interactiveSpring(response:dampingFraction:blendDuration:)](/documentation/swiftui/animation/interactivespring(response:dampingfraction:blendduration:)) A convenience for a  animation with a lower  value, intended for driving interactive animations.
- [interpolatingSpring](/documentation/swiftui/animation/interpolatingspring) An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(_:initialVelocity:)](/documentation/swiftui/animation/interpolatingspring(_:initialvelocity:)) An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [interpolatingSpring(duration:bounce:initialVelocity:)](/documentation/swiftui/animation/interpolatingspring(duration:bounce:initialvelocity:)) An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(mass:stiffness:damping:initialVelocity:)](/documentation/swiftui/animation/interpolatingspring(mass:stiffness:damping:initialvelocity:)) An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.

- [init(_:)](/documentation/swiftui/animation/init(_:)) Create an  that contains the specified custom animation.
- [timingCurve(_:duration:)](/documentation/swiftui/animation/timingcurve(_:duration:)) Creates a new animation with speed controlled by the given curve.
- [timingCurve(_:_:_:_:duration:)](/documentation/swiftui/animation/timingcurve(_:_:_:_:duration:)) An animation created from a cubic Bézier timing curve.

- [delay(_:)](/documentation/swiftui/animation/delay(_:)) Delays the start of the animation by the specified number of seconds.
- [repeatCount(_:autoreverses:)](/documentation/swiftui/animation/repeatcount(_:autoreverses:)) Repeats the animation for a specific number of times.
- [repeatForever(autoreverses:)](/documentation/swiftui/animation/repeatforever(autoreverses:)) Repeats the animation for the lifespan of the view containing the animation.
- [speed(_:)](/documentation/swiftui/animation/speed(_:)) Changes the duration of an animation by adjusting its speed.

- [base](/documentation/swiftui/animation/base)

- [animate(value:time:context:)](/documentation/swiftui/animation/animate(value:time:context:)) Calculates the current value of the animation.
- [logicallyComplete(after:)](/documentation/swiftui/animation/logicallycomplete(after:)) Causes the animation to report logical completion after the specified duration, if it has not already logically completed.
- [shouldMerge(previous:value:time:context:)](/documentation/swiftui/animation/shouldmerge(previous:value:time:context:)) Returns a Boolean value that indicates whether the current animation should merge with a previous animation.
- [velocity(value:time:context:)](/documentation/swiftui/animation/velocity(value:time:context:)) Calculates the current velocity of the animation.

- [systemOverlayAppearance](/documentation/swiftui/animation/systemoverlayappearance) Animation used when system overlays appear.
- [systemOverlayDelayedDisappearance](/documentation/swiftui/animation/systemoverlaydelayeddisappearance) Animation used when system overlays disappear, with a delay equal to .
- [systemOverlayDisappearance](/documentation/swiftui/animation/systemoverlaydisappearance) Animation used when system overlays disappear.
- [systemOverlayDisappearanceDelay](/documentation/swiftui/animation/systemoverlaydisappearancedelay) The length of time system overlays remain visible before disappearing.

- [interactiveSpring(duration:extraBounce:blendDuration:)](/documentation/swiftui/animation/interactivespring(duration:extrabounce:blendduration:)) A convenience for a  animation with a lower  value, intended for driving interactive animations.

- [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:))
- [withAnimation(_:completionCriteria:_:completion:)](/documentation/swiftui/withanimation(_:completioncriteria:_:completion:))
- [AnimationCompletionCriteria](/documentation/swiftui/animationcompletioncriteria)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Animation
```

Example 2 (swift):
```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
```

Example 3 (swift):
```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn.repeatCount(3), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
}
```

Example 4 (swift):
```swift
struct ContentView: View {
    @State private var isTrailing = false

    var body: some View {
       VStack(alignment: isTrailing ? .trailing : .leading) {
            Image(systemName: "box.truck")
                .font(.system(size: 64))

            Toggle("Move to trailing edge",
                   isOn: $isTrailing.animation(.linear))
        }
    }
}
```

---

## shadow(color:radius:x:y:)

**URL:** https://sosumi.ai/documentation/swiftui/view/shadow(color:radius:x:y:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Applying blur and shadows

---
title: shadow(color:radius:x:y:)
description: Adds a shadow to this view.
source: https://developer.apple.com/documentation/swiftui/view/shadow(color:radius:x:y:)
timestamp: 2026-02-13T19:33:22.800Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a shadow to this view.

A measure of how much to blur the shadow. Larger values result in more blur.

An amount to offset the shadow horizontally from the view.

An amount to offset the shadow vertically from the view.

A view that adds a shadow to this view.

Use this modifier to add a shadow of a specified color behind a view. You can offset the shadow from its view independently in the horizontal and vertical dimensions using the `x` and `y` parameters. You can also blur the edges of the shadow using the `radius` parameter. Use a radius of zero to create a sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each box displays its radius and offset values for reference.

The example above uses [primary](/documentation/swiftui/color/primary) as the color to make the shadow easy to see for the purpose of illustration. In practice, you might prefer something more subtle, like [gray](/documentation/swiftui/color/gray). If you don’t specify a color, the method uses a semi-transparent black.

- [blur(radius:opaque:)](/documentation/swiftui/view/blur(radius:opaque:))
- [ColorMatrix](/documentation/swiftui/colormatrix)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some View
```

Example 2 (swift):
```swift
struct Shadow: View {
    let steps = [0, 5, 10]

    var body: some View {
        VStack(spacing: 50) {
            ForEach(steps, id: \.self) { offset in
                HStack(spacing: 50) {
                    ForEach(steps, id: \.self) { radius in
                        Color.blue
                            .shadow(
                                color: .primary,
                                radius: CGFloat(radius),
                                x: CGFloat(offset), y: CGFloat(offset))
                            .overlay {
                                VStack {
                                    Text("\(radius)")
                                    Text("(\(offset), \(offset))")
                                }
                            }
                    }
                }
            }
        }
    }
}
```

---

## onSubmit(of:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onsubmit(of:_:)?.md

**Contents:**
- Parameters
- Discussion
- Responding to submission events

---
title: onSubmit(of:_:)
description: Adds an action to perform when the user submits a value to this view.
source: https://developer.apple.com/documentation/swiftui/view/onsubmit(of:_:)
timestamp: 2026-02-13T19:35:26.498Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Adds an action to perform when the user submits a value to this view.

The triggers that should invoke the provided action.

The action to perform on submission of a value.

Different views may have different triggers for the provided action. A [Text Field](/documentation/swiftui/textfield), or [Secure Field](/documentation/swiftui/securefield) will trigger this action when the user hits the hardware or software return key. This modifier may also bind this action to a default action keyboard shortcut. You may set this action on an individual view or an entire view hierarchy.

You can use the [submitScope(_:)](/documentation/swiftui/view/submitscope(_:)) modifier to stop a submit trigger from a control from propagating higher up in the view hierarchy to higher `View.onSubmit(of:_:)` modifiers.

You can use different submit triggers to filter the types of triggers that should invoke the provided submission action. For example, you may provide a value of [search](/documentation/swiftui/submittriggers/search) to only hear submission triggers that originate from search fields vended by searchable modifiers.

- [submitScope(_:)](/documentation/swiftui/view/submitscope(_:))
- [SubmitTriggers](/documentation/swiftui/submittriggers)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onSubmit(of triggers: SubmitTriggers = .text, _ action: @escaping () -> Void) -> some View
```

Example 2 (swift):
```swift
TextField("Username", text: $username)
    .onSubmit {
        guard viewModel.validate() else { return }
        viewModel.login()
    }
```

Example 3 (swift):
```swift
Form {
    TextField("Username", text: $viewModel.userName)
    SecureField("Password", text: $viewModel.password)

    TextField("Tags", text: $viewModel.tags)
        .submitScope()
}
.onSubmit {
    guard viewModel.validate() else { return }
    viewModel.login()
}
```

Example 4 (swift):
```swift
@StateObject private var viewModel = ViewModel()

NavigationView {
    SidebarView()
    DetailView()
}
.searchable(
    text: $viewModel.searchText,
    placement: .sidebar
) {
    SuggestionsView()
}
.onSubmit(of: .search) {
    viewModel.submitCurrentSearchQuery()
}
```

---

## environment(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/environment(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Modifying the environment of a view

---
title: environment(_:_:)
description: Sets the environment value of the specified key path to the given value.
source: https://developer.apple.com/documentation/swiftui/view/environment(_:_:)
timestamp: 2026-02-13T19:35:51.217Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the environment value of the specified key path to the given value.

A key path that indicates the property of the [Environment Values](/documentation/swiftui/environmentvalues) structure to update.

The new value to set for the item specified by `keyPath`.

A view that has the given value set in its environment.

Use this modifier to set one of the writable properties of the [Environment Values](/documentation/swiftui/environmentvalues) structure, including custom values that you create. For example, you can set the value associated with the [truncation Mode](/documentation/swiftui/environmentvalues/truncationmode) key:

You then read the value inside `MyView` or one of its descendants using the [Environment](/documentation/swiftui/environment) property wrapper:

SwiftUI provides dedicated view modifiers for setting most environment values, like the [truncationMode(_:)](/documentation/swiftui/view/truncationmode(_:)) modifier which sets the [truncation Mode](/documentation/swiftui/environmentvalues/truncationmode) value:

Prefer the dedicated modifier when available, and offer your own when defining custom environment values, as described in [Entry()](/documentation/swiftui/entry()).

This modifier affects the given view, as well as that view’s descendant views. It has no effect outside the view hierarchy on which you call it.

- [environment(_:)](/documentation/swiftui/view/environment(_:))
- [transformEnvironment(_:transform:)](/documentation/swiftui/view/transformenvironment(_:transform:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some View
```

Example 2 (swift):
```swift
MyView()
    .environment(\.truncationMode, .head)
```

Example 3 (swift):
```swift
struct MyView: View {
    @Environment(\.truncationMode) var truncationMode: Text.TruncationMode

    var body: some View { ... }
}
```

Example 4 (swift):
```swift
MyView()
    .truncationMode(.head)
```

---

## accessibilityLabel(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/accessibilitylabel(_:)?.md

**Contents:**
- Discussion
- Applying labels

---
title: accessibilityLabel(_:)
description: Adds a label to the view that describes its contents.
source: https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)
timestamp: 2026-02-13T19:33:55.967Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Adds a label to the view that describes its contents.

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.

- [accessibilityLabel(_:isEnabled:)](/documentation/swiftui/view/accessibilitylabel(_:isenabled:))
- [accessibilityLabel(content:)](/documentation/swiftui/view/accessibilitylabel(content:))
- [accessibilityInputLabels(_:)](/documentation/swiftui/view/accessibilityinputlabels(_:))
- [accessibilityInputLabels(_:isEnabled:)](/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:))
- [accessibilityLabeledPair(role:id:in:)](/documentation/swiftui/view/accessibilitylabeledpair(role:id:in:))
- [AccessibilityLabeledPairRole](/documentation/swiftui/accessibilitylabeledpairrole)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func accessibilityLabel(_ label: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

---

## onDrop(of:isTargeted:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ondrop(of:istargeted:perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving items using item providers

---
title: onDrop(of:isTargeted:perform:)
description: Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
source: https://developer.apple.com/documentation/swiftui/view/ondrop(of:istargeted:perform:)
timestamp: 2026-02-13T19:35:18.165Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.

**supportedContentTypes**

The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag-and-drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.

A binding that updates when a drag and drop operation enters or exits the drop target area. The binding’s value is `true` when the cursor is inside the area, and `false` when the cursor is outside.

A closure that takes the dropped content and responds appropriately. The parameter to `action` contains the dropped items, with types specified by `supportedContentTypes`. Return `true` if the drop operation was successful; otherwise, return `false`.

A view that provides a drop destination for a drag operation of the specified types.

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:))
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:))
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:))
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:))
- [DropDelegate](/documentation/swiftui/dropdelegate)
- [DropProposal](/documentation/swiftui/dropproposal)
- [DropOperation](/documentation/swiftui/dropoperation)
- [DropInfo](/documentation/swiftui/dropinfo)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

---

## tint(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/tint(_:)?.md

**Contents:**
- Parameters
- Discussion
- Setting a color

---
title: tint(_:)
description: Sets the tint color within this view.
source: https://developer.apple.com/documentation/swiftui/view/tint(_:)
timestamp: 2026-02-13T19:33:43.323Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the tint color within this view.

The tint [Color](/documentation/swiftui/color) to apply.

Use this method to override the default accent color for this view. Unlike an app’s accent color, which can be overridden by user preference, the tint color is always respected and should be used as a way to provide additional meaning to the control.

This example shows Answer and Decline buttons with [green](/documentation/swiftui/shapestyle/green) and [red](/documentation/swiftui/shapestyle/red) tint colors, respectively.

Some controls adapt to the tint color differently based on their style, the current platform, and the surrounding context. For example, in macOS, a button with the [bordered](/documentation/swiftui/primitivebuttonstyle/bordered) style doesn’t tint its background, but one with the [bordered Prominent](/documentation/swiftui/primitivebuttonstyle/borderedprominent) style does. In macOS, neither of these button styles tint their label, but they do in other platforms.

- [Color](/documentation/swiftui/color)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func tint(_ tint: Color?) -> some View
```

Example 2 (swift):
```swift
struct ControlTint: View {
    var body: some View {
        HStack {
            Button {
                // Answer the call
            } label: {
                Label("Answer", systemImage: "phone")
            }
            .tint(.green)
            Button {
                // Decline the call
            } label: {
                Label("Decline", systemImage: "phone.down")
            }
            .tint(.red)
        }
        .buttonStyle(.borderedProminent)
        .padding()
    }
}
```

---

## keyframeAnimator(initialValue:repeating:content:keyframes:)

**URL:** https://sosumi.ai/documentation/swiftui/view/keyframeanimator(initialvalue:repeating:content:keyframes:)?.md

**Contents:**
- Parameters
- Discussion
- Creating keyframe-based animation

---
title: keyframeAnimator(initialValue:repeating:content:keyframes:)
description: Loops the given keyframes continuously, updating the view using the modifiers you apply in .
source: https://developer.apple.com/documentation/swiftui/view/keyframeanimator(initialvalue:repeating:content:keyframes:)
timestamp: 2026-02-13T19:34:50.651Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Loops the given keyframes continuously, updating the view using the modifiers you apply in .

The initial value that the keyframes will animate from.

Whether the keyframes are currently repeating. If false, the value at the beginning of the keyframe timeline will be provided to the content closure.

A view builder closure that takes two parameters. The first parameter is a proxy value representing the modified view. The second parameter is the interpolated value generated by the keyframes.

Keyframes defining how the value changes over time. The current value of the animator is the single argument, which is equal to `initialValue` when the view first appears, then is equal to the end value of the previous keyframe animation on subsequent calls.

Note that the `content` closure will be updated on every frame while animating, so avoid performing any expensive operations directly within `content`.

- [keyframeAnimator(initialValue:trigger:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:trigger:content:keyframes:))
- [KeyframeAnimator](/documentation/swiftui/keyframeanimator)
- [Keyframes](/documentation/swiftui/keyframes)
- [KeyframeTimeline](/documentation/swiftui/keyframetimeline)
- [KeyframeTrack](/documentation/swiftui/keyframetrack)
- [KeyframeTrackContentBuilder](/documentation/swiftui/keyframetrackcontentbuilder)
- [KeyframesBuilder](/documentation/swiftui/keyframesbuilder)
- [KeyframeTrackContent](/documentation/swiftui/keyframetrackcontent)
- [CubicKeyframe](/documentation/swiftui/cubickeyframe)
- [LinearKeyframe](/documentation/swiftui/linearkeyframe)
- [MoveKeyframe](/documentation/swiftui/movekeyframe)
- [SpringKeyframe](/documentation/swiftui/springkeyframe)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func keyframeAnimator<Value>(initialValue: Value, repeating: Bool = true, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View, @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes) -> some View
```

---

## opacity(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/opacity(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Hiding views

---
title: opacity(_:)
description: Sets the transparency of this view.
source: https://developer.apple.com/documentation/swiftui/view/opacity(_:)
timestamp: 2026-02-13T19:33:29.033Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the transparency of this view.

A value between 0 (fully transparent) and 1 (fully opaque).

A view that sets the transparency of this view.

Apply opacity to reveal views that are behind another view or to de-emphasize a view.

When applying the `opacity(_:)` modifier to a view that has already had its opacity transformed, the modifier multiplies the effect of the underlying opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The top yellow rectangle has its opacity set to 50%, allowing the occluded portion of the bottom rectangle to be visible:

- [hidden()](/documentation/swiftui/view/hidden())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func opacity(_ opacity: Double) -> some View
```

Example 2 (swift):
```swift
struct Opacity: View {
    var body: some View {
        VStack {
            Color.yellow.frame(width: 100, height: 100, alignment: .center)
                .zIndex(1)
                .opacity(0.5)

            Color.red.frame(width: 100, height: 100, alignment: .center)
                .padding(-40)
        }
    }
}
```

---

## DefaultGlassEffectShape

**URL:** https://sosumi.ai/documentation/swiftui/defaultglasseffectshape?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Styling views with Liquid Glass

---
title: DefaultGlassEffectShape
description: The default shape applied by glass effects, a capsule.
source: https://developer.apple.com/documentation/swiftui/defaultglasseffectshape
timestamp: 2026-02-13T19:37:10.394Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> The default shape applied by glass effects, a capsule.

You do not use this type directly. Instead, SwiftUI creates this shape on your behalf as the default parameter of the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier.

- [Animatable](/documentation/swiftui/animatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/defaultglasseffectshape/init())

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct DefaultGlassEffectShape
```

---

## pickerStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/pickerStyle(_:)?.md

**Contents:**
- Choosing from a set of options

---
title: pickerStyle(_:)
description: Sets the style for pickers within this view.
source: https://developer.apple.com/documentation/swiftui/view/pickerStyle(_:)
timestamp: 2026-02-13T19:36:07.606Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for pickers within this view.

- [Picker](/documentation/swiftui/picker)
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
nonisolated func pickerStyle<S>(_ style: S) -> some View where S : PickerStyle
```

---

## mask(alignment:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/mask(alignment:_:)?.md

**Contents:**
- Parameters
- Discussion
- Masking and clipping

---
title: mask(alignment:_:)
description: Masks this view using the alpha channel of the given view.
source: https://developer.apple.com/documentation/swiftui/view/mask(alignment:_:)
timestamp: 2026-02-13T19:33:21.204Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Masks this view using the alpha channel of the given view.

The alignment for `mask` in relation to this view.

The view whose alpha the rendering system applies to the specified view.

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

- [clipped(antialiased:)](/documentation/swiftui/view/clipped(antialiased:))
- [clipShape(_:style:)](/documentation/swiftui/view/clipshape(_:style:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func mask<Mask>(alignment: Alignment = .center, @ViewBuilder _ mask: () -> Mask) -> some View where Mask : View
```

Example 2 (swift):
```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask {
        Rectangle().opacity(0.1)
    }
```

---

## safeAreaInset(edge:alignment:spacing:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Staying in the safe areas

---
title: safeAreaInset(edge:alignment:spacing:content:)
description: Shows the specified content beside the modified view.
source: https://developer.apple.com/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)
timestamp: 2026-02-13T19:36:41.942Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Shows the specified content beside the modified view.

The horizontal edge of the view to inset by the width of `content`, to make space for `content`.

The alignment guide used to position `content` vertically.

Extra distance placed between the two views, or nil to use the default amount of spacing.

A view builder function providing the view to display in the inset space of the modified view.

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view.

The `content` view is anchored to the specified horizontal edge in the parent view, aligning its vertical axis to the specified alignment guide. The modified view is inset by the width of `content`, from `edge`, with its safe area increased by the same amount.

- [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:))
- [safeAreaPadding(_:)](/documentation/swiftui/view/safeareapadding(_:))
- [safeAreaPadding(_:_:)](/documentation/swiftui/view/safeareapadding(_:_:))
- [SafeAreaRegions](/documentation/swiftui/safearearegions)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
struct ScrollableViewWithSideBar: View {
    var body: some View {
        ScrollView {
            ScrolledContent()
        }
        .safeAreaInset(edge: .leading, spacing: 0) {
            SideBarContent()
        }
    }
}
```

---

## rotationEffect(_:anchor:)

**URL:** https://sosumi.ai/documentation/swiftui/view/rotationeffect(_:anchor:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Scaling, rotating, or transforming a view

---
title: rotationEffect(_:anchor:)
description: Rotates a view’s rendered output in two dimensions around the specified point.
source: https://developer.apple.com/documentation/swiftui/view/rotationeffect(_:anchor:)
timestamp: 2026-02-13T19:33:35.269Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Rotates a view’s rendered output in two dimensions around the specified point.

The angle by which to rotate the view.

A unit point within the view about which to perform the rotation. The default value is [center](/documentation/swiftui/unitpoint/center).

A view with rotated content.

This modifier rotates the view’s content around the axis that points out of the xy-plane. It has no effect on the view’s frame. The following code rotates text by 22˚ and then draws a border around the modified view to show that the frame remains unchanged by the rotation modifier:

- [scaledToFill()](/documentation/swiftui/view/scaledtofill())
- [scaledToFit()](/documentation/swiftui/view/scaledtofit())
- [scaleEffect(_:anchor:)](/documentation/swiftui/view/scaleeffect(_:anchor:))
- [scaleEffect(_:anchor:)](/documentation/swiftui/view/scaleeffect(_:anchor:))
- [scaleEffect(x:y:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:anchor:))
- [scaleEffect(x:y:z:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:z:anchor:))
- [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:))
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:anchorz:perspective:))
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:))
- [rotation3DEffect(_:anchor:)](/documentation/swiftui/view/rotation3deffect(_:anchor:))
- [rotation3DEffect(_:axis:anchor:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:))
- [transformEffect(_:)](/documentation/swiftui/view/transformeffect(_:))
- [transform3DEffect(_:)](/documentation/swiftui/view/transform3deffect(_:))
- [projectionEffect(_:)](/documentation/swiftui/view/projectioneffect(_:))
- [ProjectionTransform](/documentation/swiftui/projectiontransform)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some View
```

Example 2 (swift):
```swift
Text("Rotation by passing an angle in degrees")
    .rotationEffect(.degrees(22))
    .border(Color.gray)
```

---

## inspector(isPresented:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/inspector(ispresented:content:)?.md

**Contents:**
- Parameters
- Discussion
- Presenting an inspector

---
title: inspector(isPresented:content:)
description: Inserts an inspector at the applied position in the view hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/inspector(ispresented:content:)
timestamp: 2026-02-13T19:36:33.483Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+

> Inserts an inspector at the applied position in the view hierarchy.

A binding to `Bool` controlling the presented state.

The inspector content.

Apply this modifier to declare an inspector with a context-dependent presentation. For example, an inspector can present as a trailing column in a horizontally regular size class, but adapt to a sheet in a horizontally compact size class.

> [!NOTE]
> Trailing column inspectors have their presentation state restored by the framework.

> [!NOTE]
> [Inspector Commands](/documentation/swiftui/inspectorcommands) for including the default inspector commands and keyboard shortcuts.

- [inspectorColumnWidth(_:)](/documentation/swiftui/view/inspectorcolumnwidth(_:))
- [inspectorColumnWidth(min:ideal:max:)](/documentation/swiftui/view/inspectorcolumnwidth(min:ideal:max:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func inspector<V>(isPresented: Binding<Bool>, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
struct ShapeEditor: View {
    @State var presented: Bool = false
    var body: some View {
        MyEditorView()
            .inspector(isPresented: $presented) {
                TextTraitsInspectorView()
            }
    }
}
```

---

## View

**URL:** https://sosumi.ai/documentation/swiftui/view?.md

**Contents:**
- Overview
- Inherited By
- Conforming Types
- Implementing a custom view
- Configuring view elements
- Drawing views
- Providing interactivity
- Deprecated modifiers
- Instance Methods
- Creating a view

---
title: View
description: A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
source: https://developer.apple.com/documentation/swiftui/view
timestamp: 2026-02-13T19:31:17.895Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A type that represents part of your app’s user interface and provides modifiers that you use to configure views.

You create custom views by declaring types that conform to the `View` protocol. Implement the required [body](/documentation/swiftui/view/body-8kl5o) computed property to provide the content for your custom view.

Assemble the view’s body by combining one or more of the built-in views provided by SwiftUI, like the [Text](/documentation/swiftui/text) instance in the example above, plus other custom views that you define, into a hierarchy of views. For more information about creating custom views, see [Declaring-a-Custom](/documentation/swiftui/declaring-a-custom-view).

The `View` protocol provides a set of modifiers — protocol methods with default implementations — that you use to configure views in the layout of your app. Modifiers work by wrapping the view instance on which you call them in another view with the specified characteristics, as described in [Configuring](/documentation/swiftui/configuring-views). For example, adding the [opacity(_:)](/documentation/swiftui/view/opacity(_:)) modifier to a text view returns a new view with some amount of transparency:

The complete list of default modifiers provides a large set of controls for managing views. For example, you can fine tune [View](/documentation/swiftui/view-layout), add [View](/documentation/swiftui/view-accessibility) information, and respond to [View-Input-and](/documentation/swiftui/view-input-and-events). You can also collect groups of default modifiers into new, custom view modifiers for easy reuse.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is declared in its original declaration. Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt-out the isolation.

- [DynamicViewContent](/documentation/swiftui/dynamicviewcontent)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [NSViewControllerRepresentable](/documentation/swiftui/nsviewcontrollerrepresentable)
- [NSViewRepresentable](/documentation/swiftui/nsviewrepresentable)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Shape](/documentation/swiftui/shape)
- [ShapeView](/documentation/swiftui/shapeview)
- [UIViewControllerRepresentable](/documentation/swiftui/uiviewcontrollerrepresentable)
- [UIViewRepresentable](/documentation/swiftui/uiviewrepresentable)
- [WKInterfaceObjectRepresentable](/documentation/swiftui/wkinterfaceobjectrepresentable)

- [AngularGradient](/documentation/swiftui/angulargradient)
- [AnyShape](/documentation/swiftui/anyshape)
- [AnyView](/documentation/swiftui/anyview)
- [AsyncImage](/documentation/swiftui/asyncimage)
- [Button](/documentation/swiftui/button)
- [ButtonBorderShape](/documentation/swiftui/buttonbordershape)
- [ButtonStyleConfiguration.Label](/documentation/swiftui/buttonstyleconfiguration/label-swift.struct)
- [Canvas](/documentation/swiftui/canvas)
- [Capsule](/documentation/swiftui/capsule)
- [Circle](/documentation/swiftui/circle)
- [Color](/documentation/swiftui/color)
- [ColorPicker](/documentation/swiftui/colorpicker)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)
- [ContainerRelativeShape](/documentation/swiftui/containerrelativeshape)
- [ContentUnavailableView](/documentation/swiftui/contentunavailableview)
- [ControlGroup](/documentation/swiftui/controlgroup)
- [ControlGroupStyleConfiguration.Content](/documentation/swiftui/controlgroupstyleconfiguration/content-swift.struct)
- [ControlGroupStyleConfiguration.Label](/documentation/swiftui/controlgroupstyleconfiguration/label-swift.struct)
- [DatePicker](/documentation/swiftui/datepicker)
- [DatePickerStyleConfiguration.Label](/documentation/swiftui/datepickerstyleconfiguration/label-swift.struct)
- [DebugReplaceableView](/documentation/swiftui/debugreplaceableview)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultDocumentGroupLaunchActions](/documentation/swiftui/defaultdocumentgrouplaunchactions)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)
- [DefaultSettingsLinkLabel](/documentation/swiftui/defaultsettingslinklabel)
- [DefaultShareLinkLabel](/documentation/swiftui/defaultsharelinklabel)
- [DefaultTabLabel](/documentation/swiftui/defaulttablabel)
- [DefaultWindowVisibilityToggleLabel](/documentation/swiftui/defaultwindowvisibilitytogglelabel)
- [DisclosureGroup](/documentation/swiftui/disclosuregroup)
- [DisclosureGroupStyleConfiguration.Content](/documentation/swiftui/disclosuregroupstyleconfiguration/content-swift.struct)
- [DisclosureGroupStyleConfiguration.Label](/documentation/swiftui/disclosuregroupstyleconfiguration/label-swift.struct)
- [Divider](/documentation/swiftui/divider)
- [DocumentLaunchView](/documentation/swiftui/documentlaunchview)
- [EditButton](/documentation/swiftui/editbutton)
- [EditableCollectionContent](/documentation/swiftui/editablecollectioncontent)
- [Ellipse](/documentation/swiftui/ellipse)
- [EllipticalGradient](/documentation/swiftui/ellipticalgradient)
- [EmptyView](/documentation/swiftui/emptyview)
- [EquatableView](/documentation/swiftui/equatableview)
- [FillShapeView](/documentation/swiftui/fillshapeview)
- [ForEach](/documentation/swiftui/foreach)
- [Form](/documentation/swiftui/form)
- [FormStyleConfiguration.Content](/documentation/swiftui/formstyleconfiguration/content-swift.struct)
- [Gauge](/documentation/swiftui/gauge)
- [GaugeStyleConfiguration.CurrentValueLabel](/documentation/swiftui/gaugestyleconfiguration/currentvaluelabel-swift.struct)
- [GaugeStyleConfiguration.Label](/documentation/swiftui/gaugestyleconfiguration/label-swift.struct)
- [GaugeStyleConfiguration.MarkedValueLabel](/documentation/swiftui/gaugestyleconfiguration/markedvaluelabel)
- [GaugeStyleConfiguration.MaximumValueLabel](/documentation/swiftui/gaugestyleconfiguration/maximumvaluelabel-swift.struct)
- [GaugeStyleConfiguration.MinimumValueLabel](/documentation/swiftui/gaugestyleconfiguration/minimumvaluelabel-swift.struct)
- [GeometryReader](/documentation/swiftui/geometryreader)
- [GeometryReader3D](/documentation/swiftui/geometryreader3d)
- [GlassBackgroundEffectConfiguration.Content](/documentation/swiftui/glassbackgroundeffectconfiguration/content-swift.struct)
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [Grid](/documentation/swiftui/grid)
- [GridRow](/documentation/swiftui/gridrow)
- [Group](/documentation/swiftui/group)
- [GroupBox](/documentation/swiftui/groupbox)
- [GroupBoxStyleConfiguration.Content](/documentation/swiftui/groupboxstyleconfiguration/content-swift.struct)
- [GroupBoxStyleConfiguration.Label](/documentation/swiftui/groupboxstyleconfiguration/label-swift.struct)
- [GroupElementsOfContent](/documentation/swiftui/groupelementsofcontent)
- [GroupSectionsOfContent](/documentation/swiftui/groupsectionsofcontent)
- [HSplitView](/documentation/swiftui/hsplitview)
- [HStack](/documentation/swiftui/hstack)
- [HelpLink](/documentation/swiftui/helplink)
- [Image](/documentation/swiftui/image)
- [KeyframeAnimator](/documentation/swiftui/keyframeanimator)
- [Label](/documentation/swiftui/label)
- [LabelStyleConfiguration.Icon](/documentation/swiftui/labelstyleconfiguration/icon-swift.struct)
- [LabelStyleConfiguration.Title](/documentation/swiftui/labelstyleconfiguration/title-swift.struct)
- [LabeledContent](/documentation/swiftui/labeledcontent)
- [LabeledContentStyleConfiguration.Content](/documentation/swiftui/labeledcontentstyleconfiguration/content-swift.struct)
- [LabeledContentStyleConfiguration.Label](/documentation/swiftui/labeledcontentstyleconfiguration/label-swift.struct)
- [LabeledControlGroupContent](/documentation/swiftui/labeledcontrolgroupcontent)
- [LabeledToolbarItemGroupContent](/documentation/swiftui/labeledtoolbaritemgroupcontent)
- [LazyHGrid](/documentation/swiftui/lazyhgrid)
- [LazyHStack](/documentation/swiftui/lazyhstack)
- [LazyVGrid](/documentation/swiftui/lazyvgrid)
- [LazyVStack](/documentation/swiftui/lazyvstack)
- [LinearGradient](/documentation/swiftui/lineargradient)
- [Link](/documentation/swiftui/link)
- [List](/documentation/swiftui/list)
- [Menu](/documentation/swiftui/menu)
- [MenuButton](/documentation/swiftui/menubutton)
- [MenuStyleConfiguration.Content](/documentation/swiftui/menustyleconfiguration/content)
- [MenuStyleConfiguration.Label](/documentation/swiftui/menustyleconfiguration/label)
- [MeshGradient](/documentation/swiftui/meshgradient)
- [ModifiedContent](/documentation/swiftui/modifiedcontent)
- [MultiDatePicker](/documentation/swiftui/multidatepicker)
- [NavigationLink](/documentation/swiftui/navigationlink)
- [NavigationSplitView](/documentation/swiftui/navigationsplitview)
- [NavigationStack](/documentation/swiftui/navigationstack)
- [NavigationView](/documentation/swiftui/navigationview)
- [NewDocumentButton](/documentation/swiftui/newdocumentbutton)
- [OffsetShape](/documentation/swiftui/offsetshape)
- [OutlineGroup](/documentation/swiftui/outlinegroup)
- [OutlineSubgroupChildren](/documentation/swiftui/outlinesubgroupchildren)
- [PasteButton](/documentation/swiftui/pastebutton)
- [Path](/documentation/swiftui/path)
- [PhaseAnimator](/documentation/swiftui/phaseanimator)
- [Picker](/documentation/swiftui/picker)
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview)
- [PresentedWindowContent](/documentation/swiftui/presentedwindowcontent)
- [PreviewModifierContent](/documentation/swiftui/previewmodifiercontent)
- [PrimitiveButtonStyleConfiguration.Label](/documentation/swiftui/primitivebuttonstyleconfiguration/label-swift.struct)
- [ProgressView](/documentation/swiftui/progressview)
- [ProgressViewStyleConfiguration.CurrentValueLabel](/documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.struct)
- [ProgressViewStyleConfiguration.Label](/documentation/swiftui/progressviewstyleconfiguration/label-swift.struct)
- [RadialGradient](/documentation/swiftui/radialgradient)
- [Rectangle](/documentation/swiftui/rectangle)
- [RenameButton](/documentation/swiftui/renamebutton)
- [RotatedShape](/documentation/swiftui/rotatedshape)
- [RoundedRectangle](/documentation/swiftui/roundedrectangle)
- [ScaledShape](/documentation/swiftui/scaledshape)
- [ScrollView](/documentation/swiftui/scrollview)
- [ScrollViewReader](/documentation/swiftui/scrollviewreader)
- [SearchUnavailableContent.Actions](/documentation/swiftui/searchunavailablecontent/actions)
- [SearchUnavailableContent.Description](/documentation/swiftui/searchunavailablecontent/description)
- [SearchUnavailableContent.Label](/documentation/swiftui/searchunavailablecontent/label)
- [Section](/documentation/swiftui/section)
- [SectionConfiguration.Actions](/documentation/swiftui/sectionconfiguration/actions-swift.struct)
- [SecureField](/documentation/swiftui/securefield)
- [SettingsLink](/documentation/swiftui/settingslink)
- [ShareLink](/documentation/swiftui/sharelink)
- [Slider](/documentation/swiftui/slider)
- [Spacer](/documentation/swiftui/spacer)
- [Stepper](/documentation/swiftui/stepper)
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview)
- [StrokeShapeView](/documentation/swiftui/strokeshapeview)
- [SubscriptionView](/documentation/swiftui/subscriptionview)
- [Subview](/documentation/swiftui/subview)
- [SubviewsCollection](/documentation/swiftui/subviewscollection)
- [SubviewsCollectionSlice](/documentation/swiftui/subviewscollectionslice)
- [TabContentBuilder.Content](/documentation/swiftui/tabcontentbuilder/content)
- [TabView](/documentation/swiftui/tabview)
- [Table](/documentation/swiftui/table)
- [Text](/documentation/swiftui/text)
- [TextEditor](/documentation/swiftui/texteditor)
- [TextField](/documentation/swiftui/textfield)
- [TextFieldLink](/documentation/swiftui/textfieldlink)
- [TimelineView](/documentation/swiftui/timelineview)
- [Toggle](/documentation/swiftui/toggle)
- [ToggleStyleConfiguration.Label](/documentation/swiftui/togglestyleconfiguration/label-swift.struct)
- [TransformedShape](/documentation/swiftui/transformedshape)
- [TupleView](/documentation/swiftui/tupleview)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [VSplitView](/documentation/swiftui/vsplitview)
- [VStack](/documentation/swiftui/vstack)
- [ViewThatFits](/documentation/swiftui/viewthatfits)
- [WindowVisibilityToggle](/documentation/swiftui/windowvisibilitytoggle)
- [ZStack](/documentation/swiftui/zstack)
- [ZStackContent3D](/documentation/swiftui/zstackcontent3d)

- [body](/documentation/swiftui/view/body-8kl5o) The content and behavior of the view.
- [Body](/documentation/swiftui/view/body-swift.associatedtype) The type of view representing the body of this view.
- [modifier(_:)](/documentation/swiftui/view/modifier(_:)) Applies a modifier to a view and returns a new view.
- [Previews in Xcode](/documentation/swiftui/previews-in-xcode) Generate dynamic, interactive previews of your custom views.

- [Accessibility modifiers](/documentation/swiftui/view-accessibility) Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](/documentation/swiftui/view-appearance) Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](/documentation/swiftui/view-text-and-symbols) Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](/documentation/swiftui/view-auxiliary-views) Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](/documentation/swiftui/view-chart-view) Configure charts that you declare with Swift Charts.

- [Style modifiers](/documentation/swiftui/view-style-modifiers) Apply built-in styles to different types of views.
- [Layout modifiers](/documentation/swiftui/view-layout) Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.
- [Graphics and rendering modifiers](/documentation/swiftui/view-graphics-and-rendering) Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.

- [Input and event modifiers](/documentation/swiftui/view-input-and-events) Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](/documentation/swiftui/view-search) Enable people to search for content in your app.
- [Presentation modifiers](/documentation/swiftui/view-presentation) Define additional views for the view to present under specified conditions.
- [State modifiers](/documentation/swiftui/view-state) Access storage and provide child views with configuration data.

- [Deprecated modifiers](/documentation/swiftui/view-deprecated) Review unsupported modifiers and their replacements.

- [accessibilityActions(category:_:)](/documentation/swiftui/view/accessibilityactions(category:_:)) Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [accessibilityDefaultFocus(_:_:)](/documentation/swiftui/view/accessibilitydefaultfocus(_:_:)) Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [accessibilityScrollStatus(_:isEnabled:)](/documentation/swiftui/view/accessibilityscrollstatus(_:isenabled:)) Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [addOrderToWalletButtonStyle(_:)](/documentation/swiftui/view/addordertowalletbuttonstyle(_:)) Sets the button’s style.
- [addPassToWalletButtonStyle(_:)](/documentation/swiftui/view/addpasstowalletbuttonstyle(_:)) Sets the style to be used by the button. (see ).
- [allowsWindowActivationEvents()](/documentation/swiftui/view/allowswindowactivationevents()) Configures gestures in this view hierarchy to handle events that activate the containing window.
- [appStoreMerchandising(isPresented:kind:onDismiss:)](/documentation/swiftui/view/appstoremerchandising(ispresented:kind:ondismiss:))
- [aspectRatio3D(_:contentMode:)](/documentation/swiftui/view/aspectratio3d(_:contentmode:)) Constrains this view’s dimensions to the specified 3D aspect ratio.
- [assistiveAccessNavigationIcon(_:)](/documentation/swiftui/view/assistiveaccessnavigationicon(_:)) Configures the view’s icon for purposes of navigation.
- [assistiveAccessNavigationIcon(systemImage:)](/documentation/swiftui/view/assistiveaccessnavigationicon(systemimage:)) Configures the view’s icon for purposes of navigation.
- [attributedTextFormattingDefinition(_:)](/documentation/swiftui/view/attributedtextformattingdefinition(_:)) Apply a text formatting definition to nested views.
- [automatedDeviceEnrollmentAddition(isPresented:)](/documentation/swiftui/view/automateddeviceenrollmentaddition(ispresented:)) Presents a modal view that enables users to add devices to their organization.
- [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [backgroundExtensionEffect(isEnabled:)](/documentation/swiftui/view/backgroundextensioneffect(isenabled:)) Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [breakthroughEffect(_:)](/documentation/swiftui/view/breakthrougheffect(_:)) Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [buttonSizing(_:)](/documentation/swiftui/view/buttonsizing(_:)) The preferred sizing behavior of buttons in the view hierarchy.
- [certificateSheet(trust:title:message:help:)](/documentation/swiftui/view/certificatesheet(trust:title:message:help:)) Displays a certificate sheet using the provided certificate trust.
- [chart3DCameraProjection(_:)](/documentation/swiftui/view/chart3dcameraprojection(_:))
- [chart3DPose(_:)](/documentation/swiftui/view/chart3dpose(_:)) Associates a binding to be updated when the 3D chart’s pose is changed by an interaction.
- [chart3DRenderingStyle(_:)](/documentation/swiftui/view/chart3drenderingstyle(_:))
- [chartZAxis(_:)](/documentation/swiftui/view/chartzaxis(_:)) Sets the visibility of the z axis.
- [chartZAxis(content:)](/documentation/swiftui/view/chartzaxis(content:)) Configures the z-axis for 3D charts in the view.
- [chartZAxisLabel(_:position:alignment:spacing:)](/documentation/swiftui/view/chartzaxislabel(_:position:alignment:spacing:)) Adds z axis label for charts in the view. It effects 3D charts only.
- [chartZScale(domain:range:type:)](/documentation/swiftui/view/chartzscale(domain:range:type:)) Configures the z scale for 3D charts.
- [chartZScale(domain:type:)](/documentation/swiftui/view/chartzscale(domain:type:)) Configures the z scale for 3D charts.
- [chartZScale(range:type:)](/documentation/swiftui/view/chartzscale(range:type:)) Configures the z scale for 3D charts.
- [chartZSelection(range:)](/documentation/swiftui/view/chartzselection(range:))
- [chartZSelection(value:)](/documentation/swiftui/view/chartzselection(value:))
- [contactAccessButtonCaption(_:)](/documentation/swiftui/view/contactaccessbuttoncaption(_:))
- [contactAccessButtonStyle(_:)](/documentation/swiftui/view/contactaccessbuttonstyle(_:))
- [contactAccessPicker(isPresented:completionHandler:)](/documentation/swiftui/view/contactaccesspicker(ispresented:completionhandler:)) Modally present UI which allows the user to select which contacts your app has access to.
- [containerCornerOffset(_:sizeToFit:)](/documentation/swiftui/view/containercorneroffset(_:sizetofit:)) Adjusts the view’s layout to avoid the container view’s corner insets for the specified edges.
- [containerValue(_:_:)](/documentation/swiftui/view/containervalue(_:_:)) Sets a particular container value of a view.
- [contentCaptureProtected(_:)](/documentation/swiftui/view/contentcaptureprotected(_:))
- [contentToolbar(for:content:)](/documentation/swiftui/view/contenttoolbar(for:content:)) Populates the toolbar of the specified content view type with the views you provide.
- [continuityDevicePicker(isPresented:onDidConnect:)](/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:)) A  should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of  as possible when a given condition is true.
- [controlWidgetActionHint(_:)](/documentation/swiftui/view/controlwidgetactionhint(_:)) The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](/documentation/swiftui/view/controlwidgetstatus(_:)) The status of the control described by the modified label.
- [currentEntitlementTask(for:priority:action:)](/documentation/swiftui/view/currententitlementtask(for:priority:action:)) Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [dialogPreventsAppTermination(_:)](/documentation/swiftui/view/dialogpreventsapptermination(_:)) Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
- [documentBrowserContextMenu(_:)](/documentation/swiftui/view/documentbrowsercontextmenu(_:)) Adds to a  actions that accept a list of selected files as their parameter.
- [dragConfiguration(_:)](/documentation/swiftui/view/dragconfiguration(_:)) Configures a drag session.
- [dragContainer(for:in:_:)](/documentation/swiftui/view/dragcontainer(for:in:_:)) A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](/documentation/swiftui/view/dragcontainer(for:itemid:in:_:)) A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](/documentation/swiftui/view/dragcontainerselection(_:containernamespace:)) Provides multiple item selection support for drag containers.
- [dragPreviewsFormation(_:)](/documentation/swiftui/view/dragpreviewsformation(_:)) Describes the way dragged previews are visually composed.
- [draggable(_:containerNamespace:_:)](/documentation/swiftui/view/draggable(_:containernamespace:_:)) Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](/documentation/swiftui/view/draggable(_:id:containernamespace:_:)) Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](/documentation/swiftui/view/draggable(_:id:item:containernamespace:)) Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](/documentation/swiftui/view/draggable(_:item:containernamespace:)) Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](/documentation/swiftui/view/draggable(containeritemid:containernamespace:)) Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [dropConfiguration(_:)](/documentation/swiftui/view/dropconfiguration(_:)) Configures a drop session.
- [dropDestination(for:isEnabled:action:)](/documentation/swiftui/view/dropdestination(for:isenabled:action:)) Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [dropPreviewsFormation(_:)](/documentation/swiftui/view/droppreviewsformation(_:)) Describes the way previews for a drop are composed.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](/documentation/swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:)) Present an activity picker sheet for selecting apps and websites to manage.
- [formStyle(_:)](/documentation/swiftui/view/formstyle(_:)) Sets the style for forms in a view hierarchy.
- [gameSaveSyncingAlert(directory:finishedLoading:)](/documentation/swiftui/view/gamesavesyncingalert(directory:finishedloading:)) Presents a modal view while the game synced directory loads.
- [glassBackgroundEffect(_:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(_:displaymode:)) Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(_:in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(_:in:displaymode:)) Fills the view’s background with a custom glass background effect and a shape that you specify.
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)) Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectTransition(_:)](/documentation/swiftui/view/glasseffecttransition(_:)) Associates a glass effect transition with any glass effects defined within this view.
- [glassEffectUnion(id:namespace:)](/documentation/swiftui/view/glasseffectunion(id:namespace:)) Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [groupActivityAssociation(_:)](/documentation/swiftui/view/groupactivityassociation(_:)) Specifies how a view should be associated with the current SharePlay group activity.
- [handGestureShortcut(_:isEnabled:)](/documentation/swiftui/view/handgestureshortcut(_:isenabled:)) Assigns a hand gesture shortcut to the modified control.
- [handPointerBehavior(_:)](/documentation/swiftui/view/handpointerbehavior(_:)) Sets the behavior of the hand pointer while the user is interacting with the view.
- [handlesGameControllerEvents(matching:)](/documentation/swiftui/view/handlesgamecontrollerevents(matching:)) Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
- [handlesGameControllerEvents(matching:withOptions:)](/documentation/swiftui/view/handlesgamecontrollerevents(matching:withoptions:)) Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.
- [healthDataAccessRequest(store:objectType:predicate:trigger:completion:)](/documentation/swiftui/view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:)) Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [healthDataAccessRequest(store:readTypes:trigger:completion:)](/documentation/swiftui/view/healthdataaccessrequest(store:readtypes:trigger:completion:)) Requests permission to read the specified HealthKit data types.
- [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](/documentation/swiftui/view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:)) Requests permission to save and read the specified HealthKit data types.
- [imagePlaygroundGenerationStyle(_:in:)](/documentation/swiftui/view/imageplaygroundgenerationstyle(_:in:)) Sets the generation style for an image playground.
- [imagePlaygroundPersonalizationPolicy(_:)](/documentation/swiftui/view/imageplaygroundpersonalizationpolicy(_:)) Policy determining whether to support the usage of people in the playground or not.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimage:oncompletion:oncancellation:)) Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)](/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:)) Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](/documentation/swiftui/view/imageplaygroundsheet(ispresented:concepts:sourceimage:oncompletion:oncancellation:)) Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](/documentation/swiftui/view/imageplaygroundsheet(ispresented:concepts:sourceimageurl:oncompletion:oncancellation:)) Presents the system sheet to create images from the specified input.
- [immersiveEnvironmentPicker(content:)](/documentation/swiftui/view/immersiveenvironmentpicker(content:)) Add menu items to open immersive spaces from a media player’s environment picker.
- [inAppPurchaseOptions(_:)](/documentation/swiftui/view/inapppurchaseoptions(_:)) Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)](/documentation/swiftui/view/journalingsuggestionspicker(ispresented:journalingsuggestiontoken:oncompletion:)) Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [journalingSuggestionsPicker(isPresented:onCompletion:)](/documentation/swiftui/view/journalingsuggestionspicker(ispresented:oncompletion:)) Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [labelIconToTitleSpacing(_:)](/documentation/swiftui/view/labelicontotitlespacing(_:)) Set the spacing between the icon and title in labels.
- [labelReservedIconWidth(_:)](/documentation/swiftui/view/labelreservediconwidth(_:)) Set the width reserved for icons in labels.
- [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:)) Sets a style for labeled content.
- [labelsVisibility(_:)](/documentation/swiftui/view/labelsvisibility(_:)) Controls the visibility of labels of any controls contained within this view.
- [lineHeight(_:)](/documentation/swiftui/view/lineheight(_:)) A modifier for the default line height in the view hierarchy.
- [listRowInsets(_:_:)](/documentation/swiftui/view/listrowinsets(_:_:)) Sets the insets of rows in a list on the specified edges.
- [listSectionIndexVisibility(_:)](/documentation/swiftui/view/listsectionindexvisibility(_:)) Changes the visibility of the list section index.
- [listSectionMargins(_:_:)](/documentation/swiftui/view/listsectionmargins(_:_:)) Set the section margins for the specific edges.
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](/documentation/swiftui/view/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:))
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](/documentation/swiftui/view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:))
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](/documentation/swiftui/view/managesubscriptionssheet(ispresented:subscriptiongroupid:))
- [managedContentStyle(_:)](/documentation/swiftui/view/managedcontentstyle(_:)) Applies a managed content style to the view.
- [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](/documentation/swiftui/view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:)) Allows this view to be manipulated using common hand gestures.
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](/documentation/swiftui/view/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:)) Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [manipulable(using:)](/documentation/swiftui/view/manipulable(using:)) Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](/documentation/swiftui/view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:)) Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
- [mapCameraKeyframeAnimator(trigger:keyframes:)](/documentation/swiftui/view/mapcamerakeyframeanimator(trigger:keyframes:)) Uses the given keyframes to animate the camera of a  when the given trigger value changes.
- [mapControlVisibility(_:)](/documentation/swiftui/view/mapcontrolvisibility(_:)) Configures all Map controls in the environment to have the specified visibility
- [mapControls(_:)](/documentation/swiftui/view/mapcontrols(_:)) Configures all  views in the associated environment to have standard size and position controls
- [mapFeatureSelectionAccessory(_:)](/documentation/swiftui/view/mapfeatureselectionaccessory(_:)) Specifies the selection accessory to display for a 
- [mapFeatureSelectionContent(content:)](/documentation/swiftui/view/mapfeatureselectioncontent(content:)) Specifies a custom presentation for the currently selected feature.
- [mapFeatureSelectionDisabled(_:)](/documentation/swiftui/view/mapfeatureselectiondisabled(_:)) Specifies which map features should have selection disabled.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](/documentation/swiftui/view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:)) Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](/documentation/swiftui/view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:)) Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](/documentation/swiftui/view/mapitemdetailpopover(item:displaysmap:attachmentanchor:)) Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)](/documentation/swiftui/view/mapitemdetailpopover(item:displaysmap:attachmentanchor:arrowedge:)) Presents a map item detail popover.
- [mapItemDetailSheet(isPresented:item:displaysMap:)](/documentation/swiftui/view/mapitemdetailsheet(ispresented:item:displaysmap:)) Presents a map item detail sheet.
- [mapItemDetailSheet(item:displaysMap:)](/documentation/swiftui/view/mapitemdetailsheet(item:displaysmap:)) Presents a map item detail sheet.
- [mapScope(_:)](/documentation/swiftui/view/mapscope(_:)) Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [mapStyle(_:)](/documentation/swiftui/view/mapstyle(_:)) Specifies the map style to be used.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:)) Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)) Identifies this view as the source of a navigation transition, such as a zoom transition.
- [materialActiveAppearance(_:)](/documentation/swiftui/view/materialactiveappearance(_:)) Sets an explicit active appearance for materials in this view.
- [multilineTextAlignment(strategy:)](/documentation/swiftui/view/multilinetextalignment(strategy:)) A modifier for the default text alignment strategy in the view hierarchy.
- [navigationLinkIndicatorVisibility(_:)](/documentation/swiftui/view/navigationlinkindicatorvisibility(_:)) Configures whether navigation links show a disclosure indicator.
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:)) Sets the navigation transition style for this view.
- [onAppIntentExecution(_:perform:)](/documentation/swiftui/view/onappintentexecution(_:perform:)) Registers a handler to invoke in response to the specified app intent that your app receives.
- [onApplePayCouponCodeChange(perform:)](/documentation/swiftui/view/onapplepaycouponcodechange(perform:)) Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [onApplePayPaymentMethodChange(perform:)](/documentation/swiftui/view/onapplepaypaymentmethodchange(perform:)) Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [onApplePayShippingContactChange(perform:)](/documentation/swiftui/view/onapplepayshippingcontactchange(perform:)) Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [onApplePayShippingMethodChange(perform:)](/documentation/swiftui/view/onapplepayshippingmethodchange(perform:)) Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:action:)) Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:primaryaction:secondaryaction:)) Used to register actions triggered by system capture events.
- [onDragSessionUpdated(_:)](/documentation/swiftui/view/ondragsessionupdated(_:)) Specifies an action to perform on each update of an ongoing dragging operation activated by  or anther drag modifiers.
- [onDropSessionUpdated(_:)](/documentation/swiftui/view/ondropsessionupdated(_:)) Specifies an action to perform on each update of an ongoing drop operation activated by  or other drop modifiers.
- [onGeometryChange3D(for:of:action:)](/documentation/swiftui/view/ongeometrychange3d(for:of:action:)) Returns a new view that arranges to call  whenever the value computed by  changes, where  provides access to the view’s 3D geometry properties.
- [onInAppPurchaseCompletion(perform:)](/documentation/swiftui/view/oninapppurchasecompletion(perform:)) Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](/documentation/swiftui/view/oninapppurchasestart(perform:)) Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [onInteractiveResizeChange(_:)](/documentation/swiftui/view/oninteractiveresizechange(_:)) Adds an action to perform when the enclosing window is being interactively resized.
- [onMapCameraChange(frequency:_:)](/documentation/swiftui/view/onmapcamerachange(frequency:_:)) Performs an action when Map camera framing changes
- [onOpenURL(prefersInApp:)](/documentation/swiftui/view/onopenurl(prefersinapp:)) Sets an  that prefers opening URL with an in-app browser. It’s equivalent to calling 
- [onWorldRecenter(action:)](/documentation/swiftui/view/onworldrecenter(action:)) Adds an action to perform when recentering the view with the digital crown.
- [payLaterViewAction(_:)](/documentation/swiftui/view/paylaterviewaction(_:)) Sets the action on the PayLaterView. See .
- [payLaterViewDisplayStyle(_:)](/documentation/swiftui/view/paylaterviewdisplaystyle(_:)) Sets the display style on the PayLaterView. See .
- [payWithApplePayButtonDisableCardArt()](/documentation/swiftui/view/paywithapplepaybuttondisablecardart()) Sets the features that should be allowed to show on the payment buttons.
- [payWithApplePayButtonStyle(_:)](/documentation/swiftui/view/paywithapplepaybuttonstyle(_:)) Sets the style to be used by the button. (see ).
- [popoverTip(_:arrowEdge:action:)](/documentation/swiftui/view/popovertip(_:arrowedge:action:)) Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:)) Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedges:action:)) Presents a popover tip on the modified view.
- [postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](/documentation/swiftui/view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:)) Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [preferredSubscriptionOffer(_:)](/documentation/swiftui/view/preferredsubscriptionoffer(_:)) Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [preferredWindowClippingMargins(_:_:)](/documentation/swiftui/view/preferredwindowclippingmargins(_:_:)) Requests additional margins for drawing beyond the bounds of the window.
- [presentationBreakthroughEffect(_:)](/documentation/swiftui/view/presentationbreakthrougheffect(_:)) Changes the way the enclosing presentation breaks through content occluding it.
- [presentationPreventsAppTermination(_:)](/documentation/swiftui/view/presentationpreventsapptermination(_:)) Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [productDescription(_:)](/documentation/swiftui/view/productdescription(_:)) Configure the visibility of labels displaying an in-app purchase product description within the view.
- [productIconBorder()](/documentation/swiftui/view/producticonborder()) Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](/documentation/swiftui/view/productviewstyle(_:)) Sets the style for In-App Purchase product views within a view.
- [realityViewCameraControls(_:)](/documentation/swiftui/view/realityviewcameracontrols(_:)) Adds gestures that control the position and direction of a virtual camera.
- [realityViewLayoutBehavior(_:)](/documentation/swiftui/view/realityviewlayoutbehavior(_:)) A view modifier that controls the frame sizing and content alignment behavior for 
- [rotation3DLayout(_:)](/documentation/swiftui/view/rotation3dlayout(_:)) Rotates a view with impacts to its frame in a containing layout
- [rotation3DLayout(_:axis:)](/documentation/swiftui/view/rotation3dlayout(_:axis:)) Rotates a view with impacts to its frame in a containing layout
- [safeAreaBar(edge:alignment:spacing:content:)](/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)) Shows the specified content as a custom bar beside the modified view.
- [scaledToFill3D()](/documentation/swiftui/view/scaledtofill3d()) Scales this view to fill its parent.
- [scaledToFit3D()](/documentation/swiftui/view/scaledtofit3d()) Scales this view to fit its parent.
- [scrollEdgeEffectHidden(_:for:)](/documentation/swiftui/view/scrolledgeeffecthidden(_:for:)) Hides any scroll edge effects for scroll views within this hierarchy.
- [scrollEdgeEffectStyle(_:for:)](/documentation/swiftui/view/scrolledgeeffectstyle(_:for:)) Configures the scroll edge effect style for scroll views within this hierarchy.
- [scrollInputBehavior(_:for:)](/documentation/swiftui/view/scrollinputbehavior(_:for:)) Enables or disables scrolling in scrollable views when using particular inputs.
- [searchSelection(_:)](/documentation/swiftui/view/searchselection(_:)) Binds the selection of the search field associated with the nearest searchable modifier to the given  value.
- [searchToolbarBehavior(_:)](/documentation/swiftui/view/searchtoolbarbehavior(_:)) Configures the behavior for search in the toolbar.
- [sectionIndexLabel(_:)](/documentation/swiftui/view/sectionindexlabel(_:)) Sets the label that is used in a section index to point to this section, typically only a single character long.
- [signInWithAppleButtonStyle(_:)](/documentation/swiftui/view/signinwithapplebuttonstyle(_:)) Sets the style used for displaying the control (see ).
- [sliderThumbVisibility(_:)](/documentation/swiftui/view/sliderthumbvisibility(_:)) Sets the thumb visibility for s within this view.
- [spatialOverlay(alignment:content:)](/documentation/swiftui/view/spatialoverlay(alignment:content:)) Adds secondary views within the 3D bounds of this view.
- [spatialOverlayPreferenceValue(_:alignment:_:)](/documentation/swiftui/view/spatialoverlaypreferencevalue(_:alignment:_:)) Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
- [storeButton(_:for:)](/documentation/swiftui/view/storebutton(_:for:)) Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](/documentation/swiftui/view/storeproducttask(for:priority:action:)) Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [storeProductsTask(for:priority:action:)](/documentation/swiftui/view/storeproductstask(for:priority:action:)) Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [subscriptionIntroductoryOffer(applyOffer:compactJWS:)](/documentation/swiftui/view/subscriptionintroductoryoffer(applyoffer:compactjws:)) Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.
- [subscriptionOfferViewButtonVisibility(_:for:)](/documentation/swiftui/view/subscriptionofferviewbuttonvisibility(_:for:))
- [subscriptionOfferViewDetailAction(_:)](/documentation/swiftui/view/subscriptionofferviewdetailaction(_:))
- [subscriptionOfferViewStyle(_:)](/documentation/swiftui/view/subscriptionofferviewstyle(_:))
- [subscriptionPromotionalOffer(offer:compactJWS:)](/documentation/swiftui/view/subscriptionpromotionaloffer(offer:compactjws:)) Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [subscriptionPromotionalOffer(offer:signature:)](/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:)) Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [subscriptionStatusTask(for:priority:action:)](/documentation/swiftui/view/subscriptionstatustask(for:priority:action:)) Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [subscriptionStoreButtonLabel(_:)](/documentation/swiftui/view/subscriptionstorebuttonlabel(_:)) Configures subscription store view instances within a view to use the provided button label.
- [subscriptionStoreControlBackground(_:)](/documentation/swiftui/view/subscriptionstorecontrolbackground(_:)) Set a standard effect to use for the background of subscription store view controls within the view.
- [subscriptionStoreControlIcon(icon:)](/documentation/swiftui/view/subscriptionstorecontrolicon(icon:)) Sets a view to use to decorate individual subscription options within a subscription store view.
- [subscriptionStoreControlStyle(_:)](/documentation/swiftui/view/subscriptionstorecontrolstyle(_:)) Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](/documentation/swiftui/view/subscriptionstorecontrolstyle(_:placement:)) Sets the control style and control placement for subscription store views within a view.
- [subscriptionStoreOptionGroupStyle(_:)](/documentation/swiftui/view/subscriptionstoreoptiongroupstyle(_:)) Sets the style subscription store views within this view use to display groups of subscription options.
- [subscriptionStorePickerItemBackground(_:)](/documentation/swiftui/view/subscriptionstorepickeritembackground(_:)) Sets the background style for picker items of the subscription store view instances within a view.
- [subscriptionStorePickerItemBackground(_:in:)](/documentation/swiftui/view/subscriptionstorepickeritembackground(_:in:)) Sets the background shape and style for subscription store view picker items within a view.
- [subscriptionStorePolicyDestination(for:destination:)](/documentation/swiftui/view/subscriptionstorepolicydestination(for:destination:)) Configures a view as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyDestination(url:for:)](/documentation/swiftui/view/subscriptionstorepolicydestination(url:for:)) Configures a URL as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyForegroundStyle(_:)](/documentation/swiftui/view/subscriptionstorepolicyforegroundstyle(_:)) Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStorePolicyForegroundStyle(_:_:)](/documentation/swiftui/view/subscriptionstorepolicyforegroundstyle(_:_:)) Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStoreSignInAction(_:)](/documentation/swiftui/view/subscriptionstoresigninaction(_:)) Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [symbolColorRenderingMode(_:)](/documentation/swiftui/view/symbolcolorrenderingmode(_:)) Sets the color rendering mode for symbol images.
- [symbolVariableValueMode(_:)](/documentation/swiftui/view/symbolvariablevaluemode(_:)) Sets the variable value mode mode for symbol images within this view.
- [tabBarMinimizeBehavior(_:)](/documentation/swiftui/view/tabbarminimizebehavior(_:)) Sets the behavior for tab bar minimization.
- [tabViewBottomAccessory(content:)](/documentation/swiftui/view/tabviewbottomaccessory(content:)) Places a view as the bottom accessory of the tab view.
- [tabViewBottomAccessory(isEnabled:content:)](/documentation/swiftui/view/tabviewbottomaccessory(isenabled:content:)) Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [tabViewSearchActivation(_:)](/documentation/swiftui/view/tabviewsearchactivation(_:)) Configures the activation and deactivation behavior of search in the search tab.
- [tabletopGame(_:parent:automaticUpdate:)](/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:)) Adds a tabletop game to a view.
- [tabletopGame(_:parent:automaticUpdate:interaction:)](/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:interaction:)) Supplies a closure which returns a new interaction whenever needed.
- [task(id:name:executorPreference:priority:file:line:_:)](/documentation/swiftui/view/task(id:name:executorpreference:priority:file:line:_:)) Adds a task to perform before this view appears or when a specified value changes.
- [textContentType(_:)](/documentation/swiftui/view/textcontenttype(_:)) Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputFormattingControlVisibility(_:for:)](/documentation/swiftui/view/textinputformattingcontrolvisibility(_:for:)) Define which system text formatting controls are available.
- [textRenderer(_:)](/documentation/swiftui/view/textrenderer(_:)) Returns a new view such that any text views within it will use  to draw themselves.
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)) Sets the direction of a selection or cursor relative to a text character.
- [tipAnchor(_:)](/documentation/swiftui/view/tipanchor(_:)) Sets a value for the specified tip anchor to be used to anchor a tip view to the  of the view.
- [tipBackground(_:)](/documentation/swiftui/view/tipbackground(_:)) Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips.
- [tipBackgroundInteraction(_:)](/documentation/swiftui/view/tipbackgroundinteraction(_:)) Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](/documentation/swiftui/view/tipcornerradius(_:antialiased:)) Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](/documentation/swiftui/view/tipimagesize(_:)) Sets the size for a tip’s image.
- [tipImageStyle(_:)](/documentation/swiftui/view/tipimagestyle(_:)) Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](/documentation/swiftui/view/tipimagestyle(_:_:)) Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](/documentation/swiftui/view/tipimagestyle(_:_:_:)) Sets the style for a tip’s image.
- [tipViewStyle(_:)](/documentation/swiftui/view/tipviewstyle(_:)) Sets the given style for TipView within the view hierarchy.
- [toolbarItemHidden(_:)](/documentation/swiftui/view/toolbaritemhidden(_:)) Hides an individual view within a control group toolbar item.
- [transactionPicker(isPresented:selection:)](/documentation/swiftui/view/transactionpicker(ispresented:selection:)) Presents a picker that selects a collection of transactions.
- [transactionTask(_:action:)](/documentation/swiftui/view/transactiontask(_:action:)) Provides a task to perform before this view appears
- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](/documentation/swiftui/view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:)) Presents a translation popover when a given condition is true.
- [translationTask(_:action:)](/documentation/swiftui/view/translationtask(_:action:)) Adds a task to perform before this view appears or when the translation configuration changes.
- [translationTask(source:target:action:)](/documentation/swiftui/view/translationtask(source:target:action:)) Adds a task to perform before this view appears or when the specified source or target languages change.
- [verifyIdentityWithWalletButtonStyle(_:)](/documentation/swiftui/view/verifyidentitywithwalletbuttonstyle(_:)) Sets the style to be used by the button. (see ).
- [webViewBackForwardNavigationGestures(_:)](/documentation/swiftui/view/webviewbackforwardnavigationgestures(_:)) Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [webViewContentBackground(_:)](/documentation/swiftui/view/webviewcontentbackground(_:)) Specifies the visibility of the webpage’s natural background color within this view.
- [webViewContextMenu(menu:)](/documentation/swiftui/view/webviewcontextmenu(menu:)) Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [webViewElementFullscreenBehavior(_:)](/documentation/swiftui/view/webviewelementfullscreenbehavior(_:)) Determines whether a web view can display content full screen.
- [webViewLinkPreviews(_:)](/documentation/swiftui/view/webviewlinkpreviews(_:)) Determines whether pressing a link displays a preview of the destination for the link.
- [webViewMagnificationGestures(_:)](/documentation/swiftui/view/webviewmagnificationgestures(_:)) Determines whether magnify gestures change the view’s magnification.
- [webViewOnScrollGeometryChange(for:of:action:)](/documentation/swiftui/view/webviewonscrollgeometrychange(for:of:action:)) Adds an action to be performed when a value, created from a scroll geometry, changes.
- [webViewScrollInputBehavior(_:for:)](/documentation/swiftui/view/webviewscrollinputbehavior(_:for:)) Enables or disables scrolling in web views when using particular inputs.
- [webViewScrollPosition(_:)](/documentation/swiftui/view/webviewscrollposition(_:)) Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](/documentation/swiftui/view/webviewtextselection(_:)) Determines whether to allow people to select or otherwise interact with text.
- [windowResizeAnchor(_:)](/documentation/swiftui/view/windowresizeanchor(_:)) Sets the window anchor point used when the size of the view changes such that the window must resize.
- [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)) Configures the visibility of the window toolbar when the window enters full screen mode.
- [workoutPreview(_:isPresented:)](/documentation/swiftui/view/workoutpreview(_:ispresented:)) Presents a preview of the workout contents as a modal sheet
- [writingDirection(strategy:)](/documentation/swiftui/view/writingdirection(strategy:)) A modifier for the default text writing direction strategy in the view hierarchy.
- [writingToolsAffordanceVisibility(_:)](/documentation/swiftui/view/writingtoolsaffordancevisibility(_:)) Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [writingToolsBehavior(_:)](/documentation/swiftui/view/writingtoolsbehavior(_:)) Specifies the Writing Tools behavior for text and text input in the environment.

- [Declaring a custom view](/documentation/swiftui/declaring-a-custom-view)
- [ViewBuilder](/documentation/swiftui/viewbuilder)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol View
```

Example 2 (swift):
```swift
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

Example 3 (swift):
```swift
Text("Hello, World!")
    .opacity(0.5) // Display partially transparent text.
```

---

## onReceive(_:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onreceive(_:perform:)?.md

**Contents:**
- Parameters
- Return Value
- Responding to data changes

---
title: onReceive(_:perform:)
description: Adds an action to perform when this view detects data emitted by the given publisher.
source: https://developer.apple.com/documentation/swiftui/view/onreceive(_:perform:)
timestamp: 2026-02-13T19:35:10.673Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform when this view detects data emitted by the given publisher.

The publisher to subscribe to.

The action to perform when an event is emitted by `publisher`. The event emitted by publisher is passed as a parameter to `action`.

A view that triggers `action` when `publisher` emits an event.

- [onChange(of:initial:_:)](/documentation/swiftui/view/onchange(of:initial:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onReceive<P>(_ publisher: P, perform action: @escaping (P.Output) -> Void) -> some View where P : Publisher, P.Failure == Never
```

---

## background(_:in:fillStyle:)

**URL:** https://sosumi.ai/documentation/swiftui/view/background(_:in:fillstyle:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: background(_:in:fillStyle:)
description: Sets the view’s background to an insettable shape filled with a style.
source: https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:)
timestamp: 2026-02-13T19:33:15.245Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the view’s background to an insettable shape filled with a style.

A [Shape Style](/documentation/swiftui/shapestyle) that SwiftUI uses to the fill the shape that you specify.

An instance of a type that conforms to [Insettable Shape](/documentation/swiftui/insettableshape) that SwiftUI draws behind the view.

The [Fill Style](/documentation/swiftui/fillstyle) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.

A view with the specified insettable shape drawn behind it.

Use this modifier to layer a type that conforms to the [Insettable Shape](/documentation/swiftui/insettableshape) protocol — like a [Rectangle](/documentation/swiftui/rectangle), [Circle](/documentation/swiftui/circle), or [Capsule](/documentation/swiftui/capsule) — behind a view. Specify the [Shape Style](/documentation/swiftui/shapestyle) that’s used to fill the shape. For example, you can place a [Rounded Rectangle](/documentation/swiftui/roundedrectangle) behind a [Label](/documentation/swiftui/label):

The [teal](/documentation/swiftui/shapestyle/teal) color fills the shape:

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [View](/documentation/swiftui/view) types — or with a stack of views — use [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)) instead. To add a [Shape Style](/documentation/swiftui/shapestyle) as a background, use [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:))
- [overlay(alignment:content:)](/documentation/swiftui/view/overlay(alignment:content:))
- [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:))
- [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:))
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial)
- [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:))
- [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:))
- [ContainerBackgroundPlacement](/documentation/swiftui/containerbackgroundplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape
```

Example 2 (swift):
```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: RoundedRectangle(cornerRadius: 8))
```

---

## toggleStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/togglestyle(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
  - Styling toggles in a hierarchy
  - Automatic styling
- Getting numeric inputs

---
title: toggleStyle(_:)
description: Sets the style for toggles in a view hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/togglestyle(_:)
timestamp: 2026-02-13T19:36:03.601Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for toggles in a view hierarchy.

The toggle style to set. Use one of the built-in values, like [switch](/documentation/swiftui/togglestyle/switch) or [button](/documentation/swiftui/togglestyle/button), or a custom style that you define by creating a type that conforms to the [Toggle Style](/documentation/swiftui/togglestyle) protocol.

A view that uses the specified toggle style for itself and its child views.

Use this modifier on a [Toggle](/documentation/swiftui/toggle) instance to set a style that defines the control’s appearance and behavior. For example, you can choose the [switch](/documentation/swiftui/togglestyle/switch) style:

Built-in styles typically have a similar appearance across platforms, tailored to the platform’s overall style:

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS |  |
| macOS |  |

You can set a style for all toggle instances within a view hierarchy by applying the style modifier to a container view. For example, you can apply the [button](/documentation/swiftui/togglestyle/button) style to an [HStack](/documentation/swiftui/hstack):

The example above has the following appearance when `isFlagged` is `true` and `isMuted` is `false`:

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS |  |
| macOS |  |

If you don’t set a style, SwiftUI assumes a value of [automatic](/documentation/swiftui/togglestyle/automatic), which corresponds to a context-specific default. Specify the automatic style explicitly to override a container’s style and revert to the default:

The style that SwiftUI uses as the default depends on both the platform and the context. In macOS, the default in most contexts is a [checkbox](/documentation/swiftui/togglestyle/checkbox), while in iOS, the default toggle style is a [switch](/documentation/swiftui/togglestyle/switch):

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS |  |
| macOS |  |

> [!NOTE]
> Like toggle style does for toggles, the [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:)) modifier sets the style for [Label](/documentation/swiftui/label) instances in the hierarchy. The example above demostrates the compact [icon Only](/documentation/swiftui/labelstyle/icononly) style, which is useful for button toggles in space-constrained contexts. Always include a descriptive title for better accessibility.

For more information about how SwiftUI chooses a default toggle style, see the [automatic](/documentation/swiftui/togglestyle/automatic) style.

- [Slider](/documentation/swiftui/slider)
- [Stepper](/documentation/swiftui/stepper)
- [Toggle](/documentation/swiftui/toggle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toggleStyle<S>(_ style: S) -> some View where S : ToggleStyle
```

Example 2 (swift):
```swift
Toggle("Vibrate on Ring", isOn: $vibrateOnRing)
    .toggleStyle(.switch)
```

Example 3 (swift):
```swift
HStack {
    Toggle(isOn: $isFlagged) {
        Label("Flag", systemImage: "flag.fill")
    }
    Toggle(isOn: $isMuted) {
        Label("Mute", systemImage: "speaker.slash.fill")
    }
}
.toggleStyle(.button)
```

Example 4 (swift):
```swift
HStack {
    Toggle(isOn: $isShuffling) {
        Label("Shuffle", systemImage: "shuffle")
    }
    Toggle(isOn: $isRepeating) {
        Label("Repeat", systemImage: "repeat")
    }

    Divider()

    Toggle("Enhance Sound", isOn: $isEnhanced)
        .toggleStyle(.automatic) // Revert to the default style.
}
.toggleStyle(.button) // Use button style for toggles in the stack.
.labelStyle(.iconOnly) // Omit the title from any labels.
```

---

## Grid

**URL:** https://sosumi.ai/documentation/swiftui/grid?.md

**Contents:**
- Overview
  - Multicolumn cells
  - Column count
  - Cell spacing and alignment
  - Performance considerations
- Conforms To
- Creating a grid
- Statically arranging views in two dimensions

---
title: Grid
description: A container view that arranges other views in a two dimensional layout.
source: https://developer.apple.com/documentation/swiftui/grid
timestamp: 2026-02-13T19:31:53.123Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A container view that arranges other views in a two dimensional layout.

Create a two dimensional layout by initializing a `Grid` with a collection of [Grid Row](/documentation/swiftui/gridrow) structures. The first view in each grid row appears in the grid’s first column, the second view in the second column, and so on. The following example creates a grid with two rows and two columns:

A grid and its rows behave something like a collection of [HStack](/documentation/swiftui/hstack) instances wrapped in a [VStack](/documentation/swiftui/vstack). However, the grid handles row and column creation as a single operation, which applies alignment and spacing to cells, rather than first to rows and then to a column of unrelated rows. The grid produced by the example above demonstrates this:

> [!NOTE]
> If you need a grid that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [Any Layout](/documentation/swiftui/anylayout), use [Grid Layout](/documentation/swiftui/gridlayout) instead.

If you provide a view rather than a [Grid Row](/documentation/swiftui/gridrow) as an element in the grid’s content, the grid uses the view to create a row that spans all of the grid’s columns. For example, you can add a [Divider](/documentation/swiftui/divider) between the rows of the previous example:

Because a divider takes as much horizontal space as its parent offers, the entire grid widens to fill the width offered by its parent view.

To prevent a flexible view from taking more space on a given axis than the other cells in a row or column require, add the [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:)) view modifier to the view:

This restores the grid to the width that the text and images require:

To make a cell span a specific number of columns rather than the whole grid, use the [gridCellColumns(_:)](/documentation/swiftui/view/gridcellcolumns(_:)) modifier on a view that’s contained inside a [Grid Row](/documentation/swiftui/gridrow).

The grid’s column count grows to handle the row with the largest number of columns. If you create rows with different numbers of columns, the grid adds empty cells to the trailing edge of rows that have fewer columns. The example below creates three rows with different column counts:

The resulting grid has as many columns as the widest row, adding empty cells to rows that don’t specify enough views:

The grid sets the width of all the cells in a column to match the needs of column’s widest cell. In the example above, the width of the first column depends on the width of the widest [Text](/documentation/swiftui/text) view that the column contains. The other columns, which contain flexible [Color](/documentation/swiftui/color) views, share the remaining horizontal space offered by the grid’s parent view equally.

Similarly, the tallest cell in a row sets the height of the entire row. The cells in the first column of the grid above need only the height required for each string, but the [Color](/documentation/swiftui/color) cells expand to equally share the total height available to the grid. As a result, the color cells determine the row heights.

You can control the spacing between cells in both the horizontal and vertical dimensions and set a default alignment for the content in all the grid cells when you initialize the grid using the [init(alignment:horizontalSpacing:verticalSpacing:content:)](/documentation/swiftui/grid/init(alignment:horizontalspacing:verticalspacing:content:)) initializer. Consider a modified version of the previous example:

This configuration causes all of the cells to use [bottom](/documentation/swiftui/alignment/bottom) alignment — which only affects the text cells because the colors fill their cells completely — and it reduces the spacing between cells:

You can override the alignment of specific cells or groups of cells. For example, you can change the horizontal alignment of the cells in a column by adding the [gridColumnAlignment(_:)](/documentation/swiftui/view/gridcolumnalignment(_:)) modifier, or the vertical alignment of the cells in a row by configuring the row’s [init(alignment:content:)](/documentation/swiftui/gridrow/init(alignment:content:)) initializer. You can also align a single cell with the [gridCellAnchor(_:)](/documentation/swiftui/view/gridcellanchor(_:)) modifier.

A grid can size its rows and columns correctly because it renders all of its child views immediately. If your app exhibits poor performance when it first displays a large grid that appears inside a [Scroll View](/documentation/swiftui/scrollview), consider switching to a [Lazy VGrid](/documentation/swiftui/lazyvgrid) or [Lazy HGrid](/documentation/swiftui/lazyhgrid) instead.

Lazy grids render their cells when SwiftUI needs to display them, rather than all at once. This reduces the initial cost of displaying a large scrollable grid that’s never fully visible, but also reduces the grid’s ability to optimally lay out cells. Switch to a lazy grid only if profiling your code shows a worthwhile performance improvement.

- [Copyable](/documentation/Swift/Copyable)
- [View](/documentation/swiftui/view)

- [init(alignment:horizontalSpacing:verticalSpacing:content:)](/documentation/swiftui/grid/init(alignment:horizontalspacing:verticalspacing:content:)) Creates a grid with the specified spacing, alignment, and child views.

- [GridRow](/documentation/swiftui/gridrow)
- [gridCellColumns(_:)](/documentation/swiftui/view/gridcellcolumns(_:))
- [gridCellAnchor(_:)](/documentation/swiftui/view/gridcellanchor(_:))
- [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:))
- [gridColumnAlignment(_:)](/documentation/swiftui/view/gridcolumnalignment(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Grid<Content> where Content : View
```

Example 2 (swift):
```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

Example 3 (swift):
```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    Divider()
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

Example 4 (swift):
```swift
Divider()
    .gridCellUnsizedAxes(.horizontal)
```

---

## phaseAnimator(_:content:animation:)

**URL:** https://sosumi.ai/documentation/swiftui/view/phaseanimator(_:content:animation:)?.md

**Contents:**
- Parameters
- Discussion
- Creating phase-based animation

---
title: phaseAnimator(_:content:animation:)
description: Animates effects that you apply to a view over a sequence of phases that change continuously.
source: https://developer.apple.com/documentation/swiftui/view/phaseanimator(_:content:animation:)
timestamp: 2026-02-13T19:34:48.574Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Animates effects that you apply to a view over a sequence of phases that change continuously.

The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

A view builder closure that takes two parameters: a proxy value representing the modified view and the current phase. You can apply effects to the proxy based on the current phase.

A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. As soon as the animation completes, the procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

- [Controlling the timing and movements of your animations](/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations)
- [phaseAnimator(_:trigger:content:animation:)](/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:))
- [PhaseAnimator](/documentation/swiftui/phaseanimator)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func phaseAnimator<Phase>(_ phases: some Sequence, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```

---

## contentTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contenttransition(_:)?.md

**Contents:**
- Parameters
- Discussion
- Defining transitions

---
title: contentTransition(_:)
description: Modifies the view to use a given transition as its method of animating changes to the contents of its views.
source: https://developer.apple.com/documentation/swiftui/view/contenttransition(_:)
timestamp: 2026-02-13T19:34:34.389Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Modifies the view to use a given transition as its method of animating changes to the contents of its views.

The transition to apply when animating the content change.

This modifier allows you to perform a transition that animates a change within a single view. The provided [Content Transition](/documentation/swiftui/contenttransition) can present an opacity animation for content changes, an interpolated animation of the content’s paths as they change, or perform no animation at all.

> [!TIP]
> The `contentTransition(_:)` modifier only has an effect within the context of an [Animation](/documentation/swiftui/animation).

In the following example, a [Button](/documentation/swiftui/button) changes the color and font size of a [Text](/documentation/swiftui/text) view. Since both of these properties apply to the paths of the text, the [interpolate](/documentation/swiftui/contenttransition/interpolate) transition can animate a gradual change to these properties through the entire transition. By contrast, the [opacity](/documentation/swiftui/contenttransition/opacity) transition would simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to make it easier to see the effect of the interpolation. The figure below shows the `Text` at the beginning of the animation, halfway through, and at the end.

| Time | Display |
| --- | --- |
| Start |  |
| Middle |  |
| End |  |

To control whether content transitions use GPU-accelerated rendering, set the value of the [content Transition Adds Drawing Group](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup) environment variable.

- [transition(_:)](/documentation/swiftui/view/transition(_:))
- [Transition](/documentation/swiftui/transition)
- [TransitionProperties](/documentation/swiftui/transitionproperties)
- [TransitionPhase](/documentation/swiftui/transitionphase)
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition)
- [AnyTransition](/documentation/swiftui/anytransition)
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition)
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup)
- [ContentTransition](/documentation/swiftui/contenttransition)
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview)
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:))
- [NavigationTransition](/documentation/swiftui/navigationtransition)
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:))
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:))
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func contentTransition(_ transition: ContentTransition) -> some View
```

Example 2 (swift):
```swift
private static let font1 = Font.system(size: 20)
private static let font2 = Font.system(size: 45)

@State private var color = Color.red
@State private var currentFont = font1

var body: some View {
    VStack {
        Text("Content transition")
            .foregroundColor(color)
            .font(currentFont)
            .contentTransition(.interpolate)
        Spacer()
        Button("Change") {
            withAnimation(Animation.easeInOut(duration: 5.0)) {
                color = (color == .red) ? .green : .red
                currentFont = (currentFont == font1) ? font2 : font1
            }
        }
    }
}
```

---

## frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

**URL:** https://sosumi.ai/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Influencing a view’s size

---
title: frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)
description: Positions this view within an invisible frame having the specified size constraints.
source: https://developer.apple.com/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)
timestamp: 2026-02-13T19:32:15.181Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Positions this view within an invisible frame having the specified size constraints.

The minimum width of the resulting frame.

The ideal width of the resulting frame.

The maximum width of the resulting frame.

The minimum height of the resulting frame.

The ideal height of the resulting frame.

The maximum height of the resulting frame.

The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

A view with flexible dimensions given by the call’s non-`nil` parameters.

Always specify at least one size characteristic when calling this method. Pass `nil` or leave out a characteristic to indicate that the frame should adopt this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by any constraints specified, and with any ideal dimensions specified replacing any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the frame adopts the sizing behavior of its child in that dimension. If both constraints are specified in a dimension, the frame unconditionally adopts the size proposed for it, clamped to the constraints. Otherwise, the size of the frame in either dimension is:

- If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.
- If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.
- Otherwise, the size of this view.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func frame(minWidth: CGFloat? = nil, idealWidth: CGFloat? = nil, maxWidth: CGFloat? = nil, minHeight: CGFloat? = nil, idealHeight: CGFloat? = nil, maxHeight: CGFloat? = nil, alignment: Alignment = .center) -> some View
```

---

## blur(radius:opaque:)

**URL:** https://sosumi.ai/documentation/swiftui/view/blur(radius:opaque:)?.md

**Contents:**
- Parameters
- Discussion
- Applying blur and shadows

---
title: blur(radius:opaque:)
description: Applies a Gaussian blur to this view.
source: https://developer.apple.com/documentation/swiftui/view/blur(radius:opaque:)
timestamp: 2026-02-13T19:33:31.124Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Applies a Gaussian blur to this view.

The radial size of the blur. A blur is more diffuse when its radius is large.

A Boolean value that indicates whether the blur renderer permits transparency in the blur output. Set to `true` to create an opaque blur, or set to `false` to permit transparency.

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of this view.

The example below shows two [Text](/documentation/swiftui/text) views, the first with no blur effects, the second with `blur(radius:opaque:)` applied with the `radius` set to `2`. The larger the radius, the more diffuse the effect.

- [shadow(color:radius:x:y:)](/documentation/swiftui/view/shadow(color:radius:x:y:))
- [ColorMatrix](/documentation/swiftui/colormatrix)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func blur(radius: CGFloat, opaque: Bool = false) -> some View
```

Example 2 (swift):
```swift
struct Blur: View {
    var body: some View {
        VStack {
            Text("This is some text.")
                .padding()
            Text("This is some blurry text.")
                .blur(radius: 2.0)
        }
    }
}
```

---

## redacted(reason:)

**URL:** https://sosumi.ai/documentation/swiftui/view/redacted(reason:)?.md

**Contents:**
- Discussion
- Redacting private content

---
title: redacted(reason:)
description: Adds a reason to apply a redaction to this view hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/redacted(reason:)
timestamp: 2026-02-13T19:33:53.867Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Adds a reason to apply a redaction to this view hierarchy.

Adding a redaction is an additive process: any redaction provided will be added to the reasons provided by the parent.

- [Designing your app for the Always On state](/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state)
- [privacySensitive(_:)](/documentation/swiftui/view/privacysensitive(_:))
- [unredacted()](/documentation/swiftui/view/unredacted())
- [redactionReasons](/documentation/swiftui/environmentvalues/redactionreasons)
- [isSceneCaptured](/documentation/swiftui/environmentvalues/isscenecaptured)
- [RedactionReasons](/documentation/swiftui/redactionreasons)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func redacted(reason: RedactionReasons) -> some View
```

---

## AnyView

**URL:** https://sosumi.ai/documentation/swiftui/anyview?.md

**Contents:**
- Overview
- Conforms To
- Creating a view
- Supporting view types

---
title: AnyView
description: A type-erased view.
source: https://developer.apple.com/documentation/swiftui/anyview
timestamp: 2026-02-13T19:31:32.437Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A type-erased view.

An `AnyView` allows changing the type of view used in a given view hierarchy. Whenever the type of view used with an `AnyView` changes, the old hierarchy is destroyed and a new hierarchy is created for the new type.

- [View](/documentation/swiftui/view)

- [init(_:)](/documentation/swiftui/anyview/init(_:)) Create an instance that type-erases .
- [init(erasing:)](/documentation/swiftui/anyview/init(erasing:))

- [EmptyView](/documentation/swiftui/emptyview)
- [EquatableView](/documentation/swiftui/equatableview)
- [SubscriptionView](/documentation/swiftui/subscriptionview)
- [TupleView](/documentation/swiftui/tupleview)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnyView
```

---

## popover(isPresented:attachmentAnchor:arrowEdge:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)?.md

**Contents:**
- Parameters
- Discussion
  - Breakthrough effect
- Showing a sheet, cover, or popover

---
title: popover(isPresented:attachmentAnchor:arrowEdge:content:)
description: Presents a popover when a given condition is true.
source: https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)
timestamp: 2026-02-13T19:36:31.340Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+

> Presents a popover when a given condition is true.

A binding to a Boolean value that determines whether to present the popover content that you return from the modifier’s `content` closure.

The positioning anchor that defines the attachment point of the popover. The default is [bounds](/documentation/swiftui/anchor/source/bounds).

The edge of the `attachmentAnchor` that defines the location of the popover’s arrow. The default is `nil`, which results in the system allowing any arrow edge.

A closure returning the content of the popover.

Use this method to show a popover whose contents are a SwiftUI view that you provide when a bound Boolean variable is `true`. In the example below, a popover displays whenever the user toggles the `isShowingPopover` state variable by pressing the “Show Popover” button:

> [!IMPORTANT]
> Prior to iOS 18.1, the popover arrow edge was not respected. Apps that are re-compiled with the iOS 18.1 or later SDK or visionOS 2.1 or later SDK and run on iOS 18.1 or later or visionOS 2.1 or later have the arrow edge respected. On macOS, arrow edge has always been respected. Alternatively, to allow the system to choose the best orientation of the popover’s arrow, use the `View/popover(isPresented:attachmentAnchor:content:)` variant.

In visionOS, most system presentations appear with a breakthrough effect by default. To change how the enclosing presentation breaks through content occluding it, use [presentationBreakthroughEffect(_:)](/documentation/swiftui/view/presentationbreakthrougheffect(_:)), like in the following example:

- [sheet(isPresented:onDismiss:content:)](/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
- [sheet(item:onDismiss:content:)](/documentation/swiftui/view/sheet(item:ondismiss:content:))
- [fullScreenCover(isPresented:onDismiss:content:)](/documentation/swiftui/view/fullscreencover(ispresented:ondismiss:content:))
- [fullScreenCover(item:onDismiss:content:)](/documentation/swiftui/view/fullscreencover(item:ondismiss:content:))
- [popover(item:attachmentAnchor:arrowEdge:content:)](/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))
- [PopoverAttachmentAnchor](/documentation/swiftui/popoverattachmentanchor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

Example 2 (swift):
```swift
struct PopoverExample: View {
    @State private var isShowingPopover = false

    var body: some View {
        Button("Show Popover") {
            self.isShowingPopover = true
        }
        .popover(
            isPresented: $isShowingPopover, arrowEdge: .bottom
        ) {
            Text("Popover Content")
                .padding()
        }
    }
}
```

Example 3 (swift):
```swift
.popover(isPresented: $isShowingPopover) {
    Text("Popover Content")
        .padding()
        .presentationBreakthroughEffect(.prominent)
}
```

---

## Namespace

**URL:** https://sosumi.ai/documentation/swiftui/namespace?.md

**Contents:**
- Conforms To
- Creating a namespace
- Getting the namespace
- Synchronizing geometries

---
title: Namespace
description: A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
source: https://developer.apple.com/documentation/swiftui/namespace
timestamp: 2026-02-13T19:34:46.461Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).

- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init()](/documentation/swiftui/namespace/init())

- [wrappedValue](/documentation/swiftui/namespace/wrappedvalue)
- [Namespace.ID](/documentation/swiftui/namespace/id) A namespace defined by the persistent identity of an  dynamic property.

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:))
- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties)
- [GeometryEffect](/documentation/swiftui/geometryeffect)
- [geometryGroup()](/documentation/swiftui/view/geometrygroup())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper struct Namespace
```

---

## offset(x:y:)

**URL:** https://sosumi.ai/documentation/swiftui/view/offset(x:y:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Adjusting a view’s position

---
title: offset(x:y:)
description: Offset this view by the specified horizontal and vertical distances.
source: https://developer.apple.com/documentation/swiftui/view/offset(x:y:)
timestamp: 2026-02-13T19:33:37.380Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Offset this view by the specified horizontal and vertical distances.

The horizontal distance to offset this view.

The vertical distance to offset this view.

A view that offsets this view by `x` and `y`.

Use `offset(x:y:)` to shift the displayed contents by the amount specified in the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

- [Making fine adjustments to a view’s position](/documentation/swiftui/making-fine-adjustments-to-a-view-s-position)
- [position(_:)](/documentation/swiftui/view/position(_:))
- [position(x:y:)](/documentation/swiftui/view/position(x:y:))
- [offset(_:)](/documentation/swiftui/view/offset(_:))
- [offset(z:)](/documentation/swiftui/view/offset(z:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func offset(x: CGFloat = 0, y: CGFloat = 0) -> some View
```

Example 2 (swift):
```swift
Text("Offset by passing horizontal & vertical distance")
    .border(Color.green)
    .offset(x: 20, y: 50)
    .border(Color.gray)
```

---

## glassEffect(_:in:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffect(_:in:)?.md

**Contents:**
- Discussion
- Styling views with Liquid Glass

---
title: glassEffect(_:in:)
description: Applies the Liquid Glass effect to a view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)
timestamp: 2026-02-13T19:37:12.301Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Applies the Liquid Glass effect to a view.

When you use this effect, the system:

- Renders a shape anchored behind a view with the Liquid Glass material.
- Applies the foreground effects of Liquid Glass over a view.

For example, to add this effect to a [Text](/documentation/swiftui/text):

SwiftUI uses the [regular](/documentation/swiftui/glass/regular) variant by default along with a [Capsule](/documentation/swiftui/capsule) shape.

SwiftUI anchors the Liquid Glass to a view’s bounds. For the example above, the material fills the entirety of the `Text` frame, which includes the padding.

You typically use this modifier with a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) to combine multiple Liquid Glass shapes into a single shape that can morph into one another.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func glassEffect(_ glass: Glass = .regular, in shape: some Shape = DefaultGlassEffectShape()) -> some View
```

Example 2 (swift):
```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

---

## transition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transition(_:)?.md

**Contents:**
- Discussion
- Defining transitions

---
title: transition(_:)
description: Associates a transition with the view.
source: https://developer.apple.com/documentation/swiftui/view/transition(_:)
timestamp: 2026-02-13T19:34:30.199Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Associates a transition with the view.

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a slide transition to show it.

- [Transition](/documentation/swiftui/transition)
- [TransitionProperties](/documentation/swiftui/transitionproperties)
- [TransitionPhase](/documentation/swiftui/transitionphase)
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition)
- [AnyTransition](/documentation/swiftui/anytransition)
- [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:))
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition)
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup)
- [ContentTransition](/documentation/swiftui/contenttransition)
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview)
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:))
- [NavigationTransition](/documentation/swiftui/navigationtransition)
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:))
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:))
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transition(_ t: AnyTransition) -> some View
```

Example 2 (swift):
```swift
if isActive {
    MyView()
        .transition(.slide)
}
Button("Toggle") {
    withAnimation {
        isActive.toggle()
    }
}
```

---

## font(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/font(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Setting a font

---
title: font(_:)
description: Sets the default font for text in this view.
source: https://developer.apple.com/documentation/swiftui/view/font(_:)
timestamp: 2026-02-13T19:33:39.529Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the default font for text in this view.

The default font to use in this view.

A view with the default font set to the value you supply.

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and to view hierarchies. Font information flows down the view hierarchy as part of the environment, and remains in effect unless overridden at the level of an individual view or view container.

Here, the outermost [VStack](/documentation/swiftui/vstack) applies a 16-point system font as a default font to views contained in that [VStack](/documentation/swiftui/vstack). Inside that stack, the example applies a [large Title](/documentation/swiftui/font/largetitle) font to just the first text view; this explicitly overrides the default. The remaining stack and the views contained with it continue to use the 16-point system font set by their containing view:

- [Applying custom fonts to text](/documentation/swiftui/applying-custom-fonts-to-text)
- [fontDesign(_:)](/documentation/swiftui/view/fontdesign(_:))
- [fontWeight(_:)](/documentation/swiftui/view/fontweight(_:))
- [fontWidth(_:)](/documentation/swiftui/view/fontwidth(_:))
- [font](/documentation/swiftui/environmentvalues/font)
- [Font](/documentation/swiftui/font)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func font(_ font: Font?) -> some View
```

Example 2 (swift):
```swift
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These 2 text views have the same font")
        Text("applied to their parent hierarchy")
    }
}
.font(.system(size: 16, weight: .light, design: .default))
```

---

## animation(_:value:)

**URL:** https://sosumi.ai/documentation/swiftui/view/animation(_:value:)?.md

**Contents:**
- Parameters
- Return Value
- Adding state-based animation to a view

---
title: animation(_:value:)
description: Applies the given animation to this view when the specified value changes.
source: https://developer.apple.com/documentation/swiftui/view/animation(_:value:)
timestamp: 2026-02-13T19:34:28.094Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Applies the given animation to this view when the specified value changes.

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

A value to monitor for changes.

A view that applies `animation` to this view whenever `value` changes.

- [animation(_:)](/documentation/swiftui/view/animation(_:))
- [animation(_:body:)](/documentation/swiftui/view/animation(_:body:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

---

## withAnimation(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/withanimation(_:_:)?.md

**Contents:**
- Discussion
- Adding state-based animation to an action

---
title: withAnimation(_:_:)
description: Returns the result of recomputing the view’s body with the provided animation.
source: https://developer.apple.com/documentation/swiftui/withanimation(_:_:)
timestamp: 2026-02-13T19:34:44.285Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Returns the result of recomputing the view’s body with the provided animation.

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction).

- [withAnimation(_:completionCriteria:_:completion:)](/documentation/swiftui/withanimation(_:completioncriteria:_:completion:))
- [AnimationCompletionCriteria](/documentation/swiftui/animationcompletioncriteria)
- [Animation](/documentation/swiftui/animation)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

---

## buttonStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/buttonstyle(_:)?.md

**Contents:**
- Discussion
- Creating buttons

---
title: buttonStyle(_:)
description: Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
source: https://developer.apple.com/documentation/swiftui/view/buttonstyle(_:)
timestamp: 2026-02-13T19:36:01.395Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.

Use this modifier to set a specific style for all button instances within a view:

You can also use this modifier to set the style for controls that acquire a button style through composition, like the [Menu](/documentation/swiftui/menu) and [Toggle](/documentation/swiftui/toggle) views in the following example:

The [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)) modifier causes the Terms and Conditions menu to render as a button. Similarly, the [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:)) modifier causes the two toggles to render as buttons. The button style modifier then causes not only the explicit Sign In [Button](/documentation/swiftui/button), but also the menu and toggles with button styling, to render with the bordered button style.

- [Button](/documentation/swiftui/button)
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
nonisolated func buttonStyle<S>(_ style: S) -> some View where S : ButtonStyle
```

Example 2 (swift):
```swift
HStack {
    Button("Sign In", action: signIn)
    Button("Register", action: register)
}
.buttonStyle(.bordered)
```

Example 3 (swift):
```swift
VStack {
    Menu("Terms and Conditions") {
        Button("Open in Preview", action: openInPreview)
        Button("Save as PDF", action: saveAsPDF)
    }
    Toggle("Remember Password", isOn: $isToggleOn)
    Toggle("Flag", isOn: $flagged)
    Button("Sign In", action: signIn)
}
.menuStyle(.button)
.toggleStyle(.button)
.buttonStyle(.bordered)
```

---

## matchedGeometryEffect(id:in:properties:anchor:isSource:)

**URL:** https://sosumi.ai/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Synchronizing geometries

---
title: matchedGeometryEffect(id:in:properties:anchor:isSource:)
description: Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
source: https://developer.apple.com/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)
timestamp: 2026-02-13T19:34:32.281Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Defines a group of views with synchronized geometry using an identifier and namespace that you provide.

The identifier, often derived from the identifier of the data being displayed by the view.

The namespace in which defines the `id`. New namespaces are created by adding an `@Namespace` variable to a [View](/documentation/swiftui/view) type and reading its value in the view’s body method.

The properties to copy from the source view.

The relative location in the view used to produce its shared position value.

True if the view should be used as the source of geometry for other views in the group.

A new view that defines an entry in the global database of views synchronizing their geometry.

This method sets the geometry of each view in the group from the inserted view with `isSource = true` (known as the “source” view), updating the values marked by `properties`.

If inserting a view in the same transaction that another view with the same key is removed, the system will interpolate their frame rectangles in window space to make it appear that there is a single view moving from its old position to its new position. The usual transition mechanisms define how each of the two views is rendered during the transition (e.g. fade in/out, scale, etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true` is not exactly one results are undefined, due to it not being clear which is the source view.

- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties)
- [GeometryEffect](/documentation/swiftui/geometryeffect)
- [Namespace](/documentation/swiftui/namespace)
- [geometryGroup()](/documentation/swiftui/view/geometrygroup())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func matchedGeometryEffect<ID>(id: ID, in namespace: Namespace.ID, properties: MatchedGeometryProperties = .frame, anchor: UnitPoint = .center, isSource: Bool = true) -> some View where ID : Hashable
```

---

## task(priority:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/task(priority:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to view life cycle updates

---
title: task(priority:_:)
description: Adds an asynchronous task to perform before this view appears.
source: https://developer.apple.com/documentation/swiftui/view/task(priority:_:)
timestamp: 2026-02-13T19:35:06.413Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Adds an asynchronous task to perform before this view appears.

The task priority to use when creating the asynchronous task. The default priority is [user Initiated](/documentation/Swift/TaskPriority/userInitiated).

A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI will automatically cancel the task at some point after the view disappears before the action completes.

A view that runs the specified action asynchronously before the view appears.

Use this modifier to perform an asynchronous task with a lifetime that matches that of the modified view. If the task doesn’t finish before SwiftUI removes the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to complete, or to wait on the values of an [Async Sequence](/documentation/Swift/AsyncSequence) instance. For example, you can modify a [Text](/documentation/swiftui/text) view to start a task that loads content from a remote resource:

This example uses the [lines](/documentation/Foundation/URL/lines) method to get the content stored at the specified [URL](/documentation/Foundation/URL) as an asynchronous sequence of strings. When each new line arrives, the body of the `for`-`await`-`in` loop stores the line in an array of strings and updates the content of the text view to report the latest line count.

- [onAppear(perform:)](/documentation/swiftui/view/onappear(perform:))
- [onDisappear(perform:)](/documentation/swiftui/view/ondisappear(perform:))
- [task(id:priority:_:)](/documentation/swiftui/view/task(id:priority:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func task(priority: TaskPriority = .userInitiated, _ action: @escaping () async -> Void) -> some View
```

Example 2 (swift):
```swift
let url = URL(string: "https://example.com")!
@State private var message = "Loading..."

var body: some View {
    Text(message)
        .task {
            do {
                var receivedLines = [String]()
                for try await line in url.lines {
                    receivedLines.append(line)
                    message = "Received \(receivedLines.count) lines"
                }
            } catch {
                message = "Failed to load"
            }
        }
}
```

---

## AnyTransition

**URL:** https://sosumi.ai/documentation/swiftui/anytransition?.md

**Contents:**
- Overview
- Getting built-in transitions
- Combining and configuring transitions
- Creating a custom transition
- Defining transitions

---
title: AnyTransition
description: A type-erased transition.
source: https://developer.apple.com/documentation/swiftui/anytransition
timestamp: 2026-02-13T19:34:55.028Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A type-erased transition.

- See Also: `Transition`

- [identity](/documentation/swiftui/anytransition/identity) A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](/documentation/swiftui/anytransition/move(edge:)) Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](/documentation/swiftui/anytransition/offset(_:))
- [offset(x:y:)](/documentation/swiftui/anytransition/offset(x:y:))
- [opacity](/documentation/swiftui/anytransition/opacity) A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [push(from:)](/documentation/swiftui/anytransition/push(from:)) Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [scale](/documentation/swiftui/anytransition/scale) Returns a transition that scales the view.
- [scale(scale:anchor:)](/documentation/swiftui/anytransition/scale(scale:anchor:)) Returns a transition that scales the view by the specified amount.
- [slide](/documentation/swiftui/anytransition/slide) A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.

- [animation(_:)](/documentation/swiftui/anytransition/animation(_:)) Attaches an animation to this transition.
- [asymmetric(insertion:removal:)](/documentation/swiftui/anytransition/asymmetric(insertion:removal:)) Provides a composite transition that uses a different transition for insertion versus removal.
- [combined(with:)](/documentation/swiftui/anytransition/combined(with:)) Combines this transition with another, returning a new transition that is the result of both transitions being applied.

- [init(_:)](/documentation/swiftui/anytransition/init(_:)) Create an instance that type-erases .
- [modifier(active:identity:)](/documentation/swiftui/anytransition/modifier(active:identity:)) Returns a transition defined between an active modifier and an identity modifier.

- [transition(_:)](/documentation/swiftui/view/transition(_:))
- [Transition](/documentation/swiftui/transition)
- [TransitionProperties](/documentation/swiftui/transitionproperties)
- [TransitionPhase](/documentation/swiftui/transitionphase)
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition)
- [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:))
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition)
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup)
- [ContentTransition](/documentation/swiftui/contenttransition)
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview)
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:))
- [NavigationTransition](/documentation/swiftui/navigationtransition)
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:))
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:))
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnyTransition
```

---

## accessibilityAddTraits(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/accessibilityaddtraits(_:)?.md

**Contents:**
- Assigning traits to content

---
title: accessibilityAddTraits(_:)
description: Adds the given traits to the view.
source: https://developer.apple.com/documentation/swiftui/view/accessibilityaddtraits(_:)
timestamp: 2026-02-13T19:34:00.120Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Adds the given traits to the view.

- [accessibilityRemoveTraits(_:)](/documentation/swiftui/view/accessibilityremovetraits(_:))
- [AccessibilityTraits](/documentation/swiftui/accessibilitytraits)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func accessibilityAddTraits(_ traits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

---

## confirmationDialog(_:isPresented:titleVisibility:actions:)

**URL:** https://sosumi.ai/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)?.md

**Contents:**
- Parameters
- Discussion
- Getting confirmation for an action

---
title: confirmationDialog(_:isPresented:titleVisibility:actions:)
description: Presents a confirmation dialog when a given condition is true, using a text view for the title.
source: https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)
timestamp: 2026-02-13T19:36:29.237Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Presents a confirmation dialog when a given condition is true, using a text view for the title.

The title of the dialog.

A binding to a Boolean value that determines whether to present the dialog. When the user presses or taps the dialog’s default action button, the system sets this value to `false`, dismissing the dialog.

The visibility of the dialog’s title. The default value is [automatic](/documentation/swiftui/visibility/automatic).

A view builder returning the dialog’s actions.

In the example below, a button conditionally presents a confirmation dialog depending upon the value of a bound Boolean variable. When the Boolean value is set to `true`, the system displays a confirmation dialog with a cancel action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [default Action](/documentation/swiftui/keyboardshortcut/defaultaction) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of [cancel](/documentation/swiftui/buttonrole/cancel), that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> [!NOTE]
> In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:))
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](/documentation/swiftui/view/dismissalconfirmationdialog(_:shouldpresent:actions:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func confirmationDialog<A>(_ title: Text, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ViewBuilder actions: () -> A) -> some View where A : View
```

Example 2 (swift):
```swift
struct ConfirmEraseItems: View {
    @State private var isShowingDialog = false
    var body: some View {
        Button("Empty Trash") {
            isShowingDialog = true
        }
        .confirmationDialog(
            Text("Permanently erase the items in the trash?"),
            isPresented: $isShowingDialog
        ) {
            Button("Empty Trash", role: .destructive) {
                // Handle empty trash action.
            }
        }
    }
}
```

---

## Shape

**URL:** https://sosumi.ai/documentation/swiftui/shape?.md

**Contents:**
- Overview
- Inherits From
- Inherited By
- Conforming Types
- Getting standard shapes
- Defining a shape’s size and path
- Transforming a shape
- Setting the stroke characteristics
- Filling a shape
- Setting the role

---
title: Shape
description: A 2D shape that you can use when drawing a view.
source: https://developer.apple.com/documentation/swiftui/shape
timestamp: 2026-02-13T19:34:14.119Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A 2D shape that you can use when drawing a view.

Shapes without an explicit fill or stroke get a default fill based on the foreground color.

You can define shapes in relation to an implicit frame of reference, such as the natural size of the view that contains it. Alternatively, you can define shapes in terms of absolute coordinates.

- [Animatable](/documentation/swiftui/animatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)

- [AnyShape](/documentation/swiftui/anyshape)
- [ButtonBorderShape](/documentation/swiftui/buttonbordershape)
- [Capsule](/documentation/swiftui/capsule)
- [Circle](/documentation/swiftui/circle)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)
- [ContainerRelativeShape](/documentation/swiftui/containerrelativeshape)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)
- [Ellipse](/documentation/swiftui/ellipse)
- [OffsetShape](/documentation/swiftui/offsetshape)
- [Path](/documentation/swiftui/path)
- [Rectangle](/documentation/swiftui/rectangle)
- [RotatedShape](/documentation/swiftui/rotatedshape)
- [RoundedRectangle](/documentation/swiftui/roundedrectangle)
- [ScaledShape](/documentation/swiftui/scaledshape)
- [TransformedShape](/documentation/swiftui/transformedshape)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)

- [buttonBorder](/documentation/swiftui/shape/buttonborder) A shape that defers to the environment to determine the resolved button border shape.
- [capsule](/documentation/swiftui/shape/capsule) A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](/documentation/swiftui/shape/capsule(style:)) A capsule shape aligned inside the frame of the view containing it.
- [circle](/documentation/swiftui/shape/circle) A circle centered on the frame of the view containing it.
- [containerRelative](/documentation/swiftui/shape/containerrelative) A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](/documentation/swiftui/shape/ellipse) An ellipse aligned inside the frame of the view containing it.
- [rect](/documentation/swiftui/shape/rect) A rectangular shape aligned inside the frame of the view containing it.
- [rect(cornerRadii:style:)](/documentation/swiftui/shape/rect(cornerradii:style:)) A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [rect(cornerRadius:style:)](/documentation/swiftui/shape/rect(cornerradius:style:)) A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [rect(cornerSize:style:)](/documentation/swiftui/shape/rect(cornersize:style:)) A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)](/documentation/swiftui/shape/rect(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:)) A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.

- [sizeThatFits(_:)](/documentation/swiftui/shape/sizethatfits(_:)) Returns the size of the view that will render the shape, given a proposed size.
- [path(in:)](/documentation/swiftui/shape/path(in:)) Describes this shape as a path within a rectangular frame of reference.

- [trim(from:to:)](/documentation/swiftui/shape/trim(from:to:)) Trims this shape by a fractional amount based on its representation as a path.
- [transform(_:)](/documentation/swiftui/shape/transform(_:)) Applies an affine transform to this shape.
- [size(_:)](/documentation/swiftui/shape/size(_:)) Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of . This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(width:height:)](/documentation/swiftui/shape/size(width:height:)) Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size . This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [scale(_:anchor:)](/documentation/swiftui/shape/scale(_:anchor:)) Scales this shape without changing its bounding frame.
- [scale(x:y:anchor:)](/documentation/swiftui/shape/scale(x:y:anchor:)) Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](/documentation/swiftui/shape/rotation(_:anchor:)) Rotates this shape around an anchor point at the angle you specify.
- [offset(_:)](/documentation/swiftui/shape/offset(_:)) Changes the relative position of this shape using the specified point.
- [offset(x:y:)](/documentation/swiftui/shape/offset(x:y:)) Changes the relative position of this shape using the specified point.

- [stroke(_:lineWidth:)](/documentation/swiftui/shape/stroke(_:linewidth:)) Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](/documentation/swiftui/shape/stroke(_:linewidth:antialiased:)) Traces the outline of this shape with a color or gradient.
- [stroke(lineWidth:)](/documentation/swiftui/shape/stroke(linewidth:)) Returns a new shape that is a stroked copy of  with line-width defined by  and all other properties of  having their default values.
- [stroke(_:style:)](/documentation/swiftui/shape/stroke(_:style:)) Traces the outline of this shape with a color or gradient.
- [stroke(_:style:antialiased:)](/documentation/swiftui/shape/stroke(_:style:antialiased:)) Traces the outline of this shape with a color or gradient.
- [stroke(style:)](/documentation/swiftui/shape/stroke(style:)) Returns a new shape that is a stroked copy of , using the contents of  to define the stroke characteristics.

- [fill(_:style:)](/documentation/swiftui/shape/fill(_:style:)) Fills this shape with a color or gradient.
- [fill(style:)](/documentation/swiftui/shape/fill(style:)) Fills this shape with the foreground color.

- [role](/documentation/swiftui/shape/role) An indication of how to style a shape.

- [layoutDirectionBehavior](/documentation/swiftui/shape/layoutdirectionbehavior) Returns the behavior this shape should use for different layout directions.

- [intersection(_:eoFill:)](/documentation/swiftui/shape/intersection(_:eofill:)) Returns a new shape with filled regions common to both shapes.
- [lineIntersection(_:eoFill:)](/documentation/swiftui/shape/lineintersection(_:eofill:)) Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [lineSubtraction(_:eoFill:)](/documentation/swiftui/shape/linesubtraction(_:eofill:)) Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [subtracting(_:eoFill:)](/documentation/swiftui/shape/subtracting(_:eofill:)) Returns a new shape with filled regions from this shape that are not in the given shape.
- [symmetricDifference(_:eoFill:)](/documentation/swiftui/shape/symmetricdifference(_:eofill:)) Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [union(_:eoFill:)](/documentation/swiftui/shape/union(_:eofill:)) Returns a new shape with filled regions in either this shape or the given shape.

- [size(_:anchor:)](/documentation/swiftui/shape/size(_:anchor:)) Returns a new version of self representing the same shape, but within a rect of  instead of the container size.
- [size(width:height:anchor:)](/documentation/swiftui/shape/size(width:height:anchor:)) Returns a new version of self representing the same shape, but within a rect of  instead of the container size.

- [rect(corners:isUniform:)](/documentation/swiftui/shape/rect(corners:isuniform:)) A rectangle shape that is aligned inside the frame of the view containing it. The same corner style will be set on four corners to be square, rounded, or concentric to the container shape.
- [rect(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:)) A rectangle shape that is aligned inside the frame of the view containing it. Each of the corners can be customized in style to be square, rounded, or concentric to the container shape.
- [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the bottom two corners, while the top two corners will each has an indivdual corner style.
- [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the leading two corners, while the trailing two corners will each has an indivdual corner style.
- [rect(uniformLeadingCorners:uniformTrailingCorners:)](/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the leading two corners, while another corner style will be uniformly applied to the trailing two.
- [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the top two corners, while the bottom two corners will each has an indivdual corner style.
- [rect(uniformTopCorners:uniformBottomCorners:)](/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the top two corners, while another corner style will be uniformly applied to the bottom two.
- [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)) A rectangle shape that is aligned inside the frame of the view containing it. A corner style will be uniformly applied to the trailing two corners, while the leading two corners will each has an indivdual corner style.

- [ShapeView](/documentation/swiftui/shapeview)
- [AnyShape](/documentation/swiftui/anyshape)
- [ShapeRole](/documentation/swiftui/shaperole)
- [StrokeStyle](/documentation/swiftui/strokestyle)
- [StrokeShapeView](/documentation/swiftui/strokeshapeview)
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview)
- [FillStyle](/documentation/swiftui/fillstyle)
- [FillShapeView](/documentation/swiftui/fillshapeview)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol Shape : Sendable, Animatable, View, _RemoveGlobalActorIsolation
```

---

## accessibilityHidden(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/accessibilityhidden(_:)?.md

**Contents:**
- Hiding elements

---
title: accessibilityHidden(_:)
description: Specifies whether to hide this view from system accessibility features.
source: https://developer.apple.com/documentation/swiftui/view/accessibilityhidden(_:)
timestamp: 2026-02-13T19:33:58.045Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Specifies whether to hide this view from system accessibility features.

- [accessibilityHidden(_:isEnabled:)](/documentation/swiftui/view/accessibilityhidden(_:isenabled:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func accessibilityHidden(_ hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

---

## ScrollView

**URL:** https://sosumi.ai/documentation/swiftui/scrollview?.md

**Contents:**
- Overview
  - Controlling Scroll Position
- Conforms To
- Creating a scroll view
- Configuring a scroll view
- Supporting types
- Creating a scroll view

---
title: ScrollView
description: A scrollable view.
source: https://developer.apple.com/documentation/swiftui/scrollview
timestamp: 2026-02-13T19:33:08.931Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The scroll view displays its content within the scrollable content region. As the user performs platform-appropriate scroll gestures, the scroll view adjusts what portion of the underlying content is visible. `ScrollView` can scroll horizontally, vertically, or both, but does not provide zooming functionality.

In the following example, a `ScrollView` allows the user to scroll through a [VStack](/documentation/swiftui/vstack) containing 100 [Text](/documentation/swiftui/text) views. The image after the listing shows the scroll view’s temporarily visible scrollbar at the right; you can disable it with the `showsIndicators` parameter of the `ScrollView` initializer.

You can influence where a scroll view is initially scrolled by using the [defaultScrollAnchor(_:)](/documentation/swiftui/view/defaultscrollanchor(_:)) view modifier.

Provide a value of `UnitPoint/center`` to have the scroll view start in the center of its content when a scroll view is scrollable in both axes.

Or provide an alignment of `UnitPoint/bottom`` to have the scroll view start at the bottom of its content when a scroll view is scrollable in its vertical axes.

After the scroll view initially renders, the user may scroll the content of the scroll view.

To perform programmatic scrolling, wrap one or more scroll views with a [Scroll View Reader](/documentation/swiftui/scrollviewreader).

- [View](/documentation/swiftui/view)

- [init(_:showsIndicators:content:)](/documentation/swiftui/scrollview/init(_:showsindicators:content:)) Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.
- [init(_:content:)](/documentation/swiftui/scrollview/init(_:content:)) Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.

- [content](/documentation/swiftui/scrollview/content) The scroll view’s content.
- [axes](/documentation/swiftui/scrollview/axes) The scrollable axes of the scroll view.
- [showsIndicators](/documentation/swiftui/scrollview/showsindicators) A value that indicates whether the scroll view displays the scrollable component of the content offset, in a way that’s suitable for the platform.

- [body](/documentation/swiftui/scrollview/body) The content and behavior of the scroll view.

- [ScrollViewReader](/documentation/swiftui/scrollviewreader)
- [ScrollViewProxy](/documentation/swiftui/scrollviewproxy)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ScrollView<Content> where Content : View
```

Example 2 (swift):
```swift
var body: some View {
    ScrollView {
        VStack(alignment: .leading) {
            ForEach(0..<100) {
                Text("Row \($0)")
            }
        }
    }
}
```

Example 3 (swift):
```swift
ScrollView([.horizontal, .vertical]) {
    // initially centered content
}
.defaultScrollAnchor(.center)
```

Example 4 (swift):
```swift
ScrollView {
    // initially bottom aligned content
}
.defaultScrollAnchor(.bottom)
```

---

## environmentObject(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/environmentobject(_:)?.md

**Contents:**
- Parameters
- Discussion
- Distributing model data throughout your app

---
title: environmentObject(_:)
description: Supplies an observable object to a view’s hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/environmentobject(_:)
timestamp: 2026-02-13T19:35:49.315Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Supplies an observable object to a view’s hierarchy.

The object to store and make available to the view’s hierarchy.

Use this modifier to add an observable object to a view’s environment. The object must conform to the [Observable Object](/documentation/Combine/ObservableObject) protocol.

Adding an object to a view’s environment makes the object available to subviews in the view’s hierarchy. To retrieve the object in a subview, use the [Environment Object](/documentation/swiftui/environmentobject) property wrapper.

> [!NOTE]
> If the observable object conforms to the [Observable](/documentation/Observation/Observable) protocol, use either [environment(_:)](/documentation/swiftui/view/environment(_:)) or the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifier to add the object to the view’s environment.

- [environmentObject(_:)](/documentation/swiftui/scene/environmentobject(_:))
- [EnvironmentObject](/documentation/swiftui/environmentobject)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func environmentObject<T>(_ object: T) -> some View where T : ObservableObject
```

---

## preferredColorScheme(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/preferredcolorscheme(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Detecting and requesting the light or dark appearance

---
title: preferredColorScheme(_:)
description: Sets the preferred color scheme for this presentation.
source: https://developer.apple.com/documentation/swiftui/view/preferredcolorscheme(_:)
timestamp: 2026-02-13T19:33:47.585Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the preferred color scheme for this presentation.

The preferred color scheme for this view, or `nil` to indicate no preference.

A view that sets the color scheme.

Use one of the values in [Color Scheme](/documentation/swiftui/colorscheme) with this modifier to set a preferred color scheme for the nearest enclosing presentation, like a popover, a sheet, or a window. The value that you set overrides the user’s Dark Mode selection for that presentation. In the example below, the [Toggle](/documentation/swiftui/toggle) controls an `isDarkMode` state variable, which in turn controls the color scheme of the sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this case are a [List](/documentation/swiftui/list) and a [Toggle](/documentation/swiftui/toggle) — the value that you set propagates up through the view hierarchy to the enclosing presentation, or until another color scheme modifier higher in the hierarchy overrides it. The value you set also flows down to all child views of the enclosing presentation.

Pass `nil` to indicate that there is no preferred color scheme for this view. This is useful in cases where a preferred color scheme should only be applied conditionally. In the previous example, the sheet will prefer dark mode when `isDarkMode` is set to `true`, but otherwise defer to the color scheme as determined by the system.

Multiple views in the same view hierarchy can set a preferred color scheme. Applying this modifier overrides any existing preferred color scheme set for the view, such as by one of its subviews. If there are conflicting, non-`nil` color scheme preferences set by parallel branches of the view hierarchy, the system will prioritize the first non-`nil` preference based on the order of the views. In the example below, the preferred color scheme for the entire view will resolve to `.dark`, from the second view:

A common use for this modifier is to create side-by-side previews of the same view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read the [color Scheme](/documentation/swiftui/environmentvalues/colorscheme) environment value:

- [colorScheme](/documentation/swiftui/environmentvalues/colorscheme)
- [ColorScheme](/documentation/swiftui/colorscheme)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
```

Example 2 (swift):
```swift
@State private var isPresented = false
@State private var isDarkMode = true

var body: some View {
    Button("Show Sheet") {
        isPresented = true
    }
    .sheet(isPresented: $isPresented) {
        List {
            Toggle("Dark Mode", isOn: $isDarkMode)
        }
        .preferredColorScheme(isDarkMode ? .dark : nil)
    }
}
```

Example 3 (swift):
```swift
VStack {
    Text("First")
        .preferredColorScheme(.light)
        .preferredColorScheme(nil) // overrides `.light`

    Text("Second")
        .preferredColorScheme(.dark)

    Text("Third")
        .preferredColorScheme(.light)
}
```

Example 4 (swift):
```swift
struct MyView_Previews: PreviewProvider {
    static var previews: some View {
        MyView().preferredColorScheme(.light)
        MyView().preferredColorScheme(.dark)
    }
}
```

---

## listStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/liststyle(_:)?.md

**Contents:**
- Creating a list

---
title: listStyle(_:)
description: Sets the style for lists within this view.
source: https://developer.apple.com/documentation/swiftui/view/liststyle(_:)
timestamp: 2026-02-13T19:36:11.568Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for lists within this view.

- [Displaying data in lists](/documentation/swiftui/displaying-data-in-lists)
- [List](/documentation/swiftui/list)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func listStyle<S>(_ style: S) -> some View where S : ListStyle
```

---

## clipShape(_:style:)

**URL:** https://sosumi.ai/documentation/swiftui/view/clipshape(_:style:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Masking and clipping

---
title: clipShape(_:style:)
description: Sets a clipping shape for this view.
source: https://developer.apple.com/documentation/swiftui/view/clipshape(_:style:)
timestamp: 2026-02-13T19:33:19.026Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets a clipping shape for this view.

The clipping shape to use for this view. The `shape` fills the view’s frame, while maintaining its aspect ratio.

The fill style to use when rasterizing `shape`.

A view that clips this view to `shape`, using `style` to define the shape’s rasterization.

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying a clipping shape to a view, you preserve the parts of the view covered by the shape, while eliminating other parts of the view. The clipping shape itself isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the bounds of the circle.

- [mask(alignment:_:)](/documentation/swiftui/view/mask(alignment:_:))
- [clipped(antialiased:)](/documentation/swiftui/view/clipped(antialiased:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func clipShape<S>(_ shape: S, style: FillStyle = FillStyle()) -> some View where S : Shape
```

Example 2 (swift):
```swift
Text("Clipped text in a circle")
    .frame(width: 175, height: 100)
    .foregroundColor(Color.white)
    .background(Color.black)
    .clipShape(Circle())
```

---

## safeAreaBar(edge:alignment:spacing:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Configuring scroll edge effects

---
title: safeAreaBar(edge:alignment:spacing:content:)
description: Shows the specified content as a custom bar beside the modified view.
source: https://developer.apple.com/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)
timestamp: 2026-02-13T19:36:44.168Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

> Shows the specified content as a custom bar beside the modified view.

The horizontal edge of the view on which `content` is placed.

The alignment guide used to position `content` vertically.

Extra distance placed between the two views, or nil to use the default amount of spacing.

A view builder function providing the view to display as a custom bar.

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view, adjusting the safe area and scroll edge effects to match.

Similar to the [safeAreaInset(edge:alignment:spacing:content:)](/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)-6gwby) modifier, the `content` view is anchored to the specified horizontal edge of the parent view and its width insets the safe area.

Additionally, it extends the edge effect of any scroll views affected by the inset safe area.

- [scrollEdgeEffectStyle(_:for:)](/documentation/swiftui/view/scrolledgeeffectstyle(_:for:))
- [scrollEdgeEffectHidden(_:for:)](/documentation/swiftui/view/scrolledgeeffecthidden(_:for:))
- [ScrollEdgeEffectStyle](/documentation/swiftui/scrolledgeeffectstyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> some View) -> some View
```

---

## Adopting Liquid Glass

**URL:** https://sosumi.ai/documentation/TechnologyOverviews/adopting-liquid-glass?.md

**Contents:**
- Overview
    - See your app with Liquid Glass
- Visual refresh
- App icons
- Controls
- Navigation
- Menus and toolbars
- Windows and modals
- Organization and layout
- Search

---
title: Adopting Liquid Glass
description: Find out how to bring the new material to your app.
source: https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass
timestamp: 2026-02-13T19:36:46.472Z
---

**Navigation:** [TechnologyOverviews](/documentation/TechnologyOverviews)

> Find out how to bring the new material to your app.

If you have an existing app, adopting Liquid Glass doesn’t mean reinventing your app from the ground up. Start by building your app in the latest version of Xcode to see the changes. As you review your app, use the following sections to understand the scope of changes and learn how you can adopt these best practices in your interface.

If your app uses standard components from SwiftUI, UIKit, or AppKit, your interface picks up the latest look and feel on the latest platform releases for iOS, iPadOS, macOS, tvOS, and watchOS. In Xcode, build your app with the latest SDKs, and run it on the latest platform releases to see the changes in your interface.

Interfaces across Apple platforms feature a new dynamic [materials](/design/Human-Interface-Guidelines/materials) called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. This material forms a distinct functional layer for controls and navigation elements. It affects how the interface looks, feels, and moves, adapting in response to a variety of factors to help bring focus to the underlying content.

**Leverage system frameworks to adopt Liquid Glass automatically.** In system frameworks, standard components like bars, sheets, popovers, and controls automatically adopt this material. System frameworks also dynamically adapt these components in response to factors like element overlap and focus state. Take advantage of this material with minimal code by using standard components from SwiftUI, UIKit, and AppKit.

**Reduce your use of custom backgrounds in controls and navigation elements.** Any custom backgrounds and appearances you use in these elements might overlay or interfere with Liquid Glass or other effects that the system provides, such as the scroll edge effect. Make sure to check any custom backgrounds in elements like split views, tab bars, and toolbars. Prefer to remove custom effects and let the system determine the background appearance, especially for the following elements:

**Test your interface with accessibility settings.** Translucency and fluid morphing animations contribute to the look and feel of Liquid Glass, but can adapt to people’s needs. For example, people might turn on accessibility settings that reduce transparency or motion in the interface, which can remove or modify certain effects. If you use standard components from system frameworks, this experience adapts automatically. Ensure your custom elements and animations provide a good fallback experience when these settings are on as well.

**Avoid overusing Liquid Glass effects.** If you apply Liquid Glass effects to a custom control, do so sparingly. Liquid Glass seeks to bring attention to the underlying content, and overusing this material in multiple custom controls can provide a subpar user experience by distracting from that content. Limit these effects to the most important functional elements in your app. To learn more, read [Applying-Liquid-Glass-to-custom](/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views).

[app](/design/Human-Interface-Guidelines/app-icons) take on a design that’s dynamic and expressive. Updates to the icon grid result in a standardized iconography that’s visually consistent across devices and concentric with hardware and other elements across the system. App icons now contain layers, which dynamically respond to lighting and other visual effects the system provides. iOS, iPadOS, and macOS all now offer default (light), dark, clear, and tinted appearance variants, empowering people to personalize the look and feel of their Home Screen.

**Reimagine your app icon for Liquid Glass.** Apply key design principles to help your app icon shine:

- Provide a visually consistent, optically balanced design across the platforms your app supports.
- Consider a simplified design comprised of solid, filled, overlapping semi-transparent shapes.
- Let the system handle applying masking, blurring, and other visual effects, rather than factoring them into your design.

**Design using layers.** The system automatically applies effects like reflection, refraction, shadow, blur, and highlights to your icon layers. Determine which elements of your design make sense as foreground, middle, and background elements, then define separate layers for them. You can perform this task in the design app of your choice.

**Compose and preview in Icon Composer.** Drag and drop app icon layers that you export from your design app directly into the Icon Composer app. Icon Composer lets you add a background, create layer groupings, adjust layer attributes like opacity, and preview your design with system effects and appearances. Icon Composer is available in the latest version of Xcode and for download from [](https://developer.apple.com/design/resources/). To learn more, read [creating-your-app-icon-using-icon](/documentation/Xcode/creating-your-app-icon-using-icon-composer).

**Preview against the updated grids.** The system applies masking to produce your final icon shape — rounded rectangle for iOS, iPadOS, and macOS, and circular for watchOS. Keep elements centered to avoid clipping. Irregularly shaped icons receive a system-provided background. See how your app icon looks with the updated grids to determine whether you need to make adjustments. Download these grids from [](https://developer.apple.com/design/resources/).

Controls have a refreshed look across platforms, and come to life when a person interacts with them. For controls like sliders and toggles, the knob transforms into Liquid Glass during interaction, and [buttons](/design/Human-Interface-Guidelines/buttons) fluidly morph into menus and popovers. The shape of the hardware informs the curvature of controls, so many controls adopt rounder forms to elegantly nestle into the corners of windows and displays. Controls also feature an option for an extra-large size, allowing more space for labels and accents.

**Review updates to control appearance and dimensions.** If you use standard controls from system frameworks and don’t hard-code their layout metrics, your app adopts changes to shapes and sizes automatically when you rebuild your app with the latest version of Xcode. Review changes to the following controls and any others and make sure they continue to look at home with the rest of your interface:

**Review your use of color in controls.** Be judicious with your use of [color](/design/Human-Interface-Guidelines/color) in controls and navigation so they stay legible. If you do apply color to these elements, leverage system colors to automatically adapt to light and dark contexts.

**Check for crowding or overlapping of controls.** Prefer to use standard spacing metrics instead of overriding them, and avoid overcrowding or layering Liquid Glass elements on top of each other.

**Optimize for legibility when content scrolls beneath controls.** Scroll views offer a [scrollEdgeEffectStyle(_:for:)](/documentation/SwiftUI/View/scrollEdgeEffectStyle(_:for:)) that helps maintain sufficient legibility and contrast for controls by obscuring content that scrolls beneath them. System bars like toolbars adopt this behavior by default. If you use a custom bar with elements like controls, text, or icons that have content scrolling beneath them, you can register those views to use a scroll edge effect with these APIs:

**Consider aligning the shape of controls with other rounded elements throughout the interface.** Across Apple platforms, the shape of the hardware informs the curvature, size, and shape of nested interface elements, including controls, sheets, popovers, windows, and more. Help maintain a sense of visual continuity in your interface by using rounded shapes that are concentric to their containers using these APIs:

**Leverage new button styles**. Instead of creating buttons with custom Liquid Glass effects, you can adopt the look and feel of the material with minimal code by using one of the following button style APIs:

Liquid Glass applies to the topmost layer of the interface, where you define your navigation. Key navigation elements like [tab](/design/Human-Interface-Guidelines/tab-bars) and [sidebars](/design/Human-Interface-Guidelines/sidebars) float in this Liquid Glass layer to help people focus on the underlying content.

**Establish a clear navigation hierarchy.** It’s more important than ever for your app to have a clear and consistent navigation structure that’s distinct from the content you provide. Ensure that you clearly separate your content from navigation elements, like tab bars and sidebars, to establish a distinct functional layer above the content layer.

**Consider adapting your tab bar into a sidebar automatically.** If your app uses a tab-based navigation, you can allow the tab bar to adapt into a sidebar depending on the context by using the following APIs:

**Consider using split views to build sidebar layouts with an inspector panel.** [split](/design/Human-Interface-Guidelines/split-views) are optimized to create a consistent and familiar experience for sidebar and inspector layouts across platforms. You can use the following standard system APIs for split views to build these types of layouts with minimal code:

**Check content safe areas for sidebars and inspectors.** If you have these types of components in your app’s navigation structure, audit the safe area compatibility of content next to the sidebar and inspector to help make sure underlying content is peeking through appropriately.

**Extend content beneath sidebars and inspectors.** A background extension effect creates a sense of extending a background under a sidebar or inspector, without actually scrolling or placing content under it. A background extension effect mirrors the adjacent content to give the impression of stretching it under the sidebar, and applies a blur to maintain legibility of the sidebar or inspector. This effect is perfect for creating a full, edge-to-edge content experience in apps that use split views, such as for hero images on product pages.

**Choose whether to automatically minimize your tab bar in iOS.** Tab bars can help elevate the underlying content by receding when a person scrolls up or down. You can opt into this behavior and configure the tab bar to minimize when a person scrolls down or up. The tab bar expands when a person scrolls in the opposite direction.

[menus](/design/Human-Interface-Guidelines/menus) have a refreshed look across platforms. They adopt Liquid Glass, and menu items for common actions use icons to help people quickly scan and identify those actions. New to iPadOS, apps also have a [the-menu](/design/Human-Interface-Guidelines/the-menu-bar) for faster access to common commands.

**Adopt standard icons in menu items.** For menu items that perform standard actions like Cut, Copy, and Paste, the system uses the menu item’s selector to determine which icon to apply. To adopt icons in those menu items with minimal code, make sure to use standard selectors.

**Match top menu actions to swipe actions.** For consistency and predictability, make sure the actions you surface at the top of your contextual menu match the swipe actions you provide for the same item.

[toolbars](/design/Human-Interface-Guidelines/toolbars) take on a Liquid Glass appearance, and provide a grouping mechanism for toolbar items, letting you choose which actions to display together.

**Determine which toolbar items to group together.** Group items that perform similar actions or affect the same part of the interface, and maintain consistent groupings and placement across platforms.

You can create a fixed spacer to separate items that share a background using these APIs:

**Find icons to represent common actions.** Consider representing common actions in toolbars with [icons](/design/Human-Interface-Guidelines/icons) instead of text. This approach helps declutter the interface and increase the ease of use for common actions. For consistency, don’t mix text and icons across items that share a background.

**Provide an accessibility label for every icon.** Regardless of what you show in the interface, always specify an accessibility label for each icon. This way, people who prefer a text label can opt into this information by turning on accessibility features like VoiceOver or Voice Control.

**Audit toolbar customizations.** Review anything custom you do to display items in your toolbars, like your use of fixed spacers or custom items, as these can appear inconsistent with system behavior.

**Check how you hide toolbar items.** If you see an empty toolbar item without any content, your app might be hiding the view in the toolbar item instead of the item itself. Instead, hide the entire toolbar item, using these APIs:

[windows](/design/Human-Interface-Guidelines/windows) adopt rounder corners to fit controls and navigation elements. In iPadOS, apps show window controls and support continuous window resizing. Instead of transitioning between specific preset sizes, windows resize fluidly down to a minimum size.

**Support arbitrary window sizes.** Allow people to resize their window to the width and height that works for them, and adjust your content accordingly.

**Use split views to allow fluid resizing of columns.** To support continuous window resizing, split views automatically reflow content for every size using beautiful, fluid transitions. Make sure to use standard system APIs for split views to get these animations with minimal code:

**Use layout guides and safe areas.** Make sure you specify safe areas for your content so the system can automatically adjust the window controls and title bar in relation to your content.

Modal views like sheets and action sheets adopt Liquid Glass. [sheets](/design/Human-Interface-Guidelines/sheets) feature an increased corner radius, and half sheets are inset from the edge of the display to allow content to peek through from beneath them. When a half sheet expands to full height, it transitions to a more opaque appearance to help maintain focus on the task.

**Check the content around the edges of sheets.** Inside the sheet, check for content and controls that might appear too close to rounder sheet corners. Outside the sheet, check that any content peeking through between the inset sheet and display edge looks as you expect.

**Audit the backgrounds of sheets and popovers.** Check whether you add a visual effect view to your popover’s content view, and remove those custom background views to provide a consistent experience with other sheets across the system.

An [action](/design/Human-Interface-Guidelines/action-sheets) originates from the element that initiates the action, instead of from the bottom edge of the display. When active, an action sheet also lets people interact with other parts of the interface.

**Specify the source of an action sheet.** Position an action sheet’s anchor next to the control it originates from. Make sure to set the source view or item to indicate where to originate the action sheet and create the inline appearance.

Style updates to [lists-and](/design/Human-Interface-Guidelines/lists-and-tables) help you organize and showcase your content so it can shine through the Liquid Glass layer. To give content room to breathe, organizational components like lists, tables, and forms have a larger row height and padding. Sections have an increased corner radius to match the curvature of controls across the system.

**Check capitalization in section headers.** Lists, tables, and forms optimize for legibility by adopting title-style capitalization for [init(content:header:)](/documentation/SwiftUI/Section/init(content:header:)). This means section headers no longer render entirely in capital letters regardless of the capitalization you provide. Make sure to update your section headers to title-style capitalization to match your app’s text to this systemwide convention.

**Adopt forms to take advantage of layout metrics across platform.** Use SwiftUI forms with the [grouped](/documentation/SwiftUI/FormStyle/grouped) to automatically update your form layouts.

Platform conventions for location and behavior of search optimize the experience for each device and use case. To provide an engaging search experience in your app, review these [search](/design/Human-Interface-Guidelines/search-fields) design conventions.

**Check the keyboard layout when activating your search interface.** In iOS, when a person taps a search field to give it focus, it slides upwards as the keyboard appears. Test this experience in your app to make sure the search field moves consistently with other apps and system experiences.

**Use semantic search tabs.** If your app’s search appears as part of a tab bar, make sure to use the standard system APIs for indicating which tab is the search tab. The system automatically separates the search tab from other tabs and places it at the trailing end to make your search experience consistent with other apps and help people find content faster.

Liquid Glass can have a distinct appearance and behavior across different platforms, contexts, and input methods. Test your app across devices to understand how the material looks and feels across platforms.

**In watchOS, adopt standard button styles and toolbar APIs.** Liquid Glass changes are minimal in watchOS, so they appear automatically when you open your app on the latest release even if you don’t build against the latest SDK. However, to make sure your app picks up this appearance, adopt standard toolbar APIs and button styles from watchOS 10.

**In tvOS, adopt standard focus APIs.** Across apps and system experiences in tvOS, standard buttons and controls take on a Liquid Glass appearance when focus moves to them. For consistency with the system experience, consider applying these effects to custom controls in your app when they gain focus by adopting the standard focus APIs. Apple TV 4K (2nd generation) and newer models support Liquid Glass effects. On older devices, your app maintains its current appearance.

**Combine custom Liquid Glass effects to improve rendering performance.** If you apply these effects to custom elements, make sure to combine them using a [Glass Effect Container](/documentation/SwiftUI/GlassEffectContainer), which helps optimize performance while fluidly morphing Liquid Glass shapes into each other.

**Performance test your app across platforms.** It’s a good idea to regularly assess and improve your app’s performance, and building your app with the latest SDKs provides an opportunity to check in. Profile your app to gather information about its current performance and find any opportunities for improving the user experience. To learn more, read [improving-your-app-s](/documentation/Xcode/improving-your-app-s-performance).

To update and ship your app with the latest SDKs while keeping your app as it looks when built against previous versions of the SDKs, you can add the [UIDesign Requires Compatibility](/documentation/BundleResources/Information-Property-List/UIDesignRequiresCompatibility) key to your project’s Info pane.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

---

## PrimitiveButtonStyle

**URL:** https://sosumi.ai/documentation/swiftui/primitivebuttonstyle?.md

**Contents:**
- Overview
- Conforming Types
- Getting built-in button styles
- Creating custom button styles
- Supporting types
- Styling buttons

---
title: PrimitiveButtonStyle
description: A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
source: https://developer.apple.com/documentation/swiftui/primitivebuttonstyle
timestamp: 2026-02-13T19:36:17.976Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.

To configure the current button style for a view hierarchy, use the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)) modifier. Specify a style that conforms to `PrimitiveButtonStyle` to create a button with custom interaction behavior. To create a button with the standard button interaction behavior defined for each platform, use [Button Style](/documentation/swiftui/buttonstyle) instead.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

- [AccessoryBarActionButtonStyle](/documentation/swiftui/accessorybaractionbuttonstyle)
- [AccessoryBarButtonStyle](/documentation/swiftui/accessorybarbuttonstyle)
- [BorderedButtonStyle](/documentation/swiftui/borderedbuttonstyle)
- [BorderedProminentButtonStyle](/documentation/swiftui/borderedprominentbuttonstyle)
- [BorderlessButtonStyle](/documentation/swiftui/borderlessbuttonstyle)
- [CardButtonStyle](/documentation/swiftui/cardbuttonstyle)
- [DefaultButtonStyle](/documentation/swiftui/defaultbuttonstyle)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [LinkButtonStyle](/documentation/swiftui/linkbuttonstyle)
- [PlainButtonStyle](/documentation/swiftui/plainbuttonstyle)

- [automatic](/documentation/swiftui/primitivebuttonstyle/automatic) The default button style, based on the button’s context.
- [accessoryBar](/documentation/swiftui/primitivebuttonstyle/accessorybar) A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [accessoryBarAction](/documentation/swiftui/primitivebuttonstyle/accessorybaraction) A button style that you use for extra actions in an accessory toolbar.
- [bordered](/documentation/swiftui/primitivebuttonstyle/bordered) A button style that applies the standard border style based on the button’s context.
- [borderedProminent](/documentation/swiftui/primitivebuttonstyle/borderedprominent) A button style that applies the standard bordered prominent style based on the button’s context.
- [borderless](/documentation/swiftui/primitivebuttonstyle/borderless) A button style that doesn’t apply a border.
- [card](/documentation/swiftui/primitivebuttonstyle/card) A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glass](/documentation/swiftui/primitivebuttonstyle/glass) A button style that applies a Liquid Glass effect based on the button’s context.
- [glassProminent](/documentation/swiftui/primitivebuttonstyle/glassprominent) A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](/documentation/swiftui/primitivebuttonstyle/glass(_:)) A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](/documentation/swiftui/primitivebuttonstyle/link) A button style for buttons that emulate links.
- [plain](/documentation/swiftui/primitivebuttonstyle/plain) A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.

- [makeBody(configuration:)](/documentation/swiftui/primitivebuttonstyle/makebody(configuration:)) Creates a view that represents the body of a button.
- [PrimitiveButtonStyle.Configuration](/documentation/swiftui/primitivebuttonstyle/configuration) The properties of a button.
- [Body](/documentation/swiftui/primitivebuttonstyle/body) A view that represents the body of a button.

- [DefaultButtonStyle](/documentation/swiftui/defaultbuttonstyle) The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](/documentation/swiftui/accessorybarbuttonstyle) A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](/documentation/swiftui/accessorybaractionbuttonstyle) A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](/documentation/swiftui/borderedbuttonstyle) A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](/documentation/swiftui/borderedprominentbuttonstyle) A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](/documentation/swiftui/borderlessbuttonstyle) A button style that doesn’t apply a border.
- [CardButtonStyle](/documentation/swiftui/cardbuttonstyle) A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](/documentation/swiftui/linkbuttonstyle) A button style for buttons that emulate links.
- [PlainButtonStyle](/documentation/swiftui/plainbuttonstyle) A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.

- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:))
- [ButtonStyle](/documentation/swiftui/buttonstyle)
- [ButtonStyleConfiguration](/documentation/swiftui/buttonstyleconfiguration)
- [PrimitiveButtonStyleConfiguration](/documentation/swiftui/primitivebuttonstyleconfiguration)
- [signInWithAppleButtonStyle(_:)](/documentation/swiftui/view/signinwithapplebuttonstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol PrimitiveButtonStyle
```

Example 2 (swift):
```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Example 3 (swift):
```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

---

## overlay(alignment:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/overlay(alignment:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: overlay(alignment:content:)
description: Layers the views that you specify in front of this view.
source: https://developer.apple.com/documentation/swiftui/view/overlay(alignment:content:)
timestamp: 2026-02-13T19:33:16.864Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Layers the views that you specify in front of this view.

The alignment that the modifier uses to position the implicit [ZStack](/documentation/swiftui/zstack) that groups the foreground views. The default is [center](/documentation/swiftui/alignment/center).

A [View Builder](/documentation/swiftui/viewbuilder) that you use to declare the views to draw in front of this view, stacked in the order that you list them. The last view that you list appears at the front of the stack.

A view that uses the specified content as a foreground.

Use this modifier to place one or more views in front of another view. For example, you can place a group of stars on a [Rounded Rectangle](/documentation/swiftui/roundedrectangle):

The example above assumes that you’ve defined a `Star` view with a parameterized color:

By setting different `alignment` values for each modifier, you make the stars appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier collects all of the views in the closure into an implicit [ZStack](/documentation/swiftui/zstack), taking them in order from back to front. For example, you can place a star and a [Circle](/documentation/swiftui/circle) on a field of [blue](/documentation/swiftui/shapestyle/blue):

Both the overlay modifier and the implicit [ZStack](/documentation/swiftui/zstack) composed from the overlay content — the circle and the star — use a default [center](/documentation/swiftui/alignment/center) alignment. The star appears centered on the circle, and both appear as a composite view centered in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack rather than to the individual views in the closure. You can see this if you add the [bottom](/documentation/swiftui/alignment/bottom) alignment:

The circle and the star move down as a unit to align the stack’s bottom edge with the bottom edge of the square, while the star remains centered on the circle:

To control the placement of individual items inside the `content` closure, either use a different overlay modifier for each item, as the earlier example of stars in the corners of a rectangle demonstrates, or add an explicit [ZStack](/documentation/swiftui/zstack) inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the modified view and the overlay content into a [ZStack](/documentation/swiftui/zstack). This can produce a simpler view hierarchy, but changes the layout priority that SwiftUI applies to the views. Use the overlay modifier when you want the modified view to dominate the layout.

If you want to specify a [Shape Style](/documentation/swiftui/shapestyle) like a [Color](/documentation/swiftui/color) or a [Material](/documentation/swiftui/material) as the overlay, use [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)) instead. To specify a [Shape](/documentation/swiftui/shape), use [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:))
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:))
- [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:))
- [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:))
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial)
- [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:))
- [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:))
- [ContainerBackgroundPlacement](/documentation/swiftui/containerbackgroundplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func overlay<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
RoundedRectangle(cornerRadius: 8)
    .frame(width: 200, height: 100)
    .overlay(alignment: .topLeading) { Star(color: .red) }
    .overlay(alignment: .topTrailing) { Star(color: .yellow) }
    .overlay(alignment: .bottomLeading) { Star(color: .green) }
    .overlay(alignment: .bottomTrailing) { Star(color: .blue) }
```

Example 3 (swift):
```swift
struct Star: View {
    var color = Color.yellow

    var body: some View {
        Image(systemName: "star.fill")
            .foregroundStyle(color)
    }
}
```

Example 4 (swift):
```swift
Color.blue
    .frame(width: 200, height: 200)
    .overlay {
        Circle()
            .frame(width: 100, height: 100)
        Star()
    }
```

---

## TupleView

**URL:** https://sosumi.ai/documentation/swiftui/tupleview?.md

**Contents:**
- Conforms To
- Creating a tuple view
- Supporting view types

---
title: TupleView
description: A View created from a swift tuple of View values.
source: https://developer.apple.com/documentation/swiftui/tupleview
timestamp: 2026-02-13T19:31:30.392Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A View created from a swift tuple of View values.

- [View](/documentation/swiftui/view)

- [init(_:)](/documentation/swiftui/tupleview/init(_:))
- [value](/documentation/swiftui/tupleview/value)

- [AnyView](/documentation/swiftui/anyview)
- [EmptyView](/documentation/swiftui/emptyview)
- [EquatableView](/documentation/swiftui/equatableview)
- [SubscriptionView](/documentation/swiftui/subscriptionview)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct TupleView<T>
```

---

## Capsule

**URL:** https://sosumi.ai/documentation/swiftui/capsule?.md

**Contents:**
- Overview
- Conforms To
- Creating a capsule
- Getting the shape’s characteristics
- Creating circular shapes

---
title: Capsule
description: A capsule shape aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/capsule
timestamp: 2026-02-13T19:34:02.169Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A capsule shape aligned inside the frame of the view containing it.

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(style:)](/documentation/swiftui/capsule/init(style:)) Creates a new capsule shape.

- [style](/documentation/swiftui/capsule/style)

- [Circle](/documentation/swiftui/circle)
- [Ellipse](/documentation/swiftui/ellipse)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Capsule
```

---

## glassEffectID(_:in:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffectid(_:in:)?.md

**Contents:**
- Discussion

---
title: glassEffectID(_:in:)
description: Associates an identity value to Liquid Glass effects defined within this view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffectid(_:in:)
timestamp: 2026-02-13T19:37:14.255Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Associates an identity value to Liquid Glass effects defined within this view.

You use this modifier with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) view modifier and a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) view. When used together, SwiftUI uses the identifier to animate shapes to and from each other during transitions.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func glassEffectID(_ id: (some Hashable & Sendable)?, in namespace: Namespace.ID) -> some View
```

---

## cornerRadius(_:antialiased:)

**URL:** https://sosumi.ai/documentation/swiftui/view/cornerradius(_:antialiased:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Graphics and rendering modifiers

---
title: cornerRadius(_:antialiased:)
description: Clips this view to its bounding frame, with the specified corner radius.
source: https://developer.apple.com/documentation/swiftui/view/cornerradius(_:antialiased:)
timestamp: 2026-02-13T19:33:26.938Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Clips this view to its bounding frame, with the specified corner radius.

A CGFloat value that specifies the corner radius to use when clipping the view to its bounding frame.

A Boolean value that indicates whether the rendering system applies smoothing to the edges of the clipping rectangle.

A view that clips this view to its bounding frame with the specified corner radius.

By default, a view’s bounding frame only affects its layout, so any content that extends beyond the edges of the frame remains visible. Use `cornerRadius(_:antialiased:)` to hide any content that extends beyond these edges while applying a corner radius.

The following code applies a corner radius of 25 to a text view:

- [accentColor(_:)](/documentation/swiftui/view/accentcolor(_:))
- [mask(_:)](/documentation/swiftui/view/mask(_:))
- [animation(_:)](/documentation/swiftui/view/animation(_:)-1hc0p)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func cornerRadius(_ radius: CGFloat, antialiased: Bool = true) -> some View
```

Example 2 (swift):
```swift
Text("Rounded Corners")
    .frame(width: 175, height: 75)
    .foregroundColor(Color.white)
    .background(Color.black)
    .cornerRadius(25)
```

---

## glassEffectTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffecttransition(_:)?.md

**Contents:**
- Discussion

---
title: glassEffectTransition(_:)
description: Associates a glass effect transition with any glass effects defined within this view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffecttransition(_:)
timestamp: 2026-02-13T19:37:16.145Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Associates a glass effect transition with any glass effects defined within this view.

You use this modifier with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) view modifier and [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) view. When used together, SwiftUI will use the provided transition to apply changes to the glass effect when you add or remove views with these effects from the view hierarchy.

In the example below, the notepad image will transition into and out of the pencil image when the isExpanded variable changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency func glassEffectTransition(_ transition: GlassEffectTransition) -> some View
```

Example 2 (swift):
```swift
var isExpanded: Bool
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 10.0) {
        HStack(spacing: 10.0) {
            Image(systemName: "pencil")
                .frame(width: 20.0, height: 20.0)
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

                if isExpanded {
                    Image(systemName: "note")
                        .frame(width: 20.0, height: 20.0)
                        .glassEffect()
                        .glassEffectID("note", in: namespace)
                        .glassEffectTransition(.matchedGeometry)
                }
            }
        }
    }
}
```

---

## hidden()

**URL:** https://sosumi.ai/documentation/swiftui/view/hidden()?.md

**Contents:**
- Return Value
- Discussion
- Hiding views

---
title: hidden()
description: Hides this view unconditionally.
source: https://developer.apple.com/documentation/swiftui/view/hidden()
timestamp: 2026-02-13T19:33:51.750Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Hides this view unconditionally.

Hidden views are invisible and can’t receive or respond to interactions. However, they do remain in the view hierarchy and affect layout. Use this modifier if you want to include a view for layout purposes, but don’t want it to display.

The third circle takes up space, because it’s still present, but SwiftUI doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if` statement instead:

Depending on the current value of the `isHidden` state variable in the example above, controlled by the [Toggle](/documentation/swiftui/toggle) instance, SwiftUI draws the circle or completely omits it from the layout.

- [opacity(_:)](/documentation/swiftui/view/opacity(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func hidden() -> some View
```

Example 2 (swift):
```swift
HStack {
    Image(systemName: "a.circle.fill")
    Image(systemName: "b.circle.fill")
    Image(systemName: "c.circle.fill")
        .hidden()
    Image(systemName: "d.circle.fill")
}
```

Example 3 (swift):
```swift
VStack {
    HStack {
        Image(systemName: "a.circle.fill")
        Image(systemName: "b.circle.fill")
        if !isHidden {
            Image(systemName: "c.circle.fill")
        }
        Image(systemName: "d.circle.fill")
    }
    Toggle("Hide", isOn: $isHidden)
}
```

---

## sheet(isPresented:onDismiss:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/sheet(ispresented:ondismiss:content:)?.md

**Contents:**
- Parameters
- Discussion
  - Breakthrough effect
- Showing a sheet, cover, or popover

---
title: sheet(isPresented:onDismiss:content:)
description: Presents a sheet when a binding to a Boolean value that you provide is true.
source: https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:)
timestamp: 2026-02-13T19:36:22.926Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Presents a sheet when a binding to a Boolean value that you provide is true.

A binding to a Boolean value that determines whether to present the sheet that you create in the modifier’s `content` closure.

The closure to execute when dismissing the sheet.

A closure that returns the content of the sheet.

Use this method when you want to present a modal view to the user when a Boolean value you provide is true. The example below displays a modal view of the mockup for a software license agreement when the user toggles the `isShowingSheet` variable by clicking or tapping on the “Show License Agreement” button:

In vertically compact environments, such as iPhone in landscape orientation, a sheet presentation automatically adapts to appear as a full-screen cover. Use the [presentationCompactAdaptation(_:)](/documentation/swiftui/view/presentationcompactadaptation(_:)) or [presentationCompactAdaptation(horizontal:vertical:)](/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)) modifier to override this behavior.

In visionOS, most system presentations appear with a breakthrough effect by default. To change how the enclosing presentation breaks through content occluding it, use [presentationBreakthroughEffect(_:)](/documentation/swiftui/view/presentationbreakthrougheffect(_:)), like in the following example:

> [!NOTE]
> Passing a `.none` value for a sheet has no effect.

- [sheet(item:onDismiss:content:)](/documentation/swiftui/view/sheet(item:ondismiss:content:))
- [fullScreenCover(isPresented:onDismiss:content:)](/documentation/swiftui/view/fullscreencover(ispresented:ondismiss:content:))
- [fullScreenCover(item:onDismiss:content:)](/documentation/swiftui/view/fullscreencover(item:ondismiss:content:))
- [popover(item:attachmentAnchor:arrowEdge:content:)](/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
- [PopoverAttachmentAnchor](/documentation/swiftui/popoverattachmentanchor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

Example 2 (swift):
```swift
struct ShowLicenseAgreement: View {
    @State private var isShowingSheet = false
    var body: some View {
        Button(action: {
            isShowingSheet.toggle()
        }) {
            Text("Show License Agreement")
        }
        .sheet(isPresented: $isShowingSheet,
               onDismiss: didDismiss) {
            VStack {
                Text("License Agreement")
                    .font(.title)
                    .padding(50)
                Text("""
                        Terms and conditions go here.
                    """)
                    .padding(50)
                Button("Dismiss",
                       action: { isShowingSheet.toggle() })
            }
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }
}
```

Example 3 (swift):
```swift
.sheet(isPresented: $isShowingSheet,
       onDismiss: didDismiss) {
    VStack {
        Text("License Agreement")
            .font(.title)
            .padding(50)
        Text("""
                Terms and conditions go here.
            """)
            .padding(50)
        Button("Dismiss",
               action: { isShowingSheet.toggle() })
    }
    .presentationBreakthroughEffect(.prominent)
}
```

---

## scaleEffect(_:anchor:)

**URL:** https://sosumi.ai/documentation/swiftui/view/scaleeffect(_:anchor:)?.md

**Contents:**
- Parameters
- Discussion
- Scaling, rotating, or transforming a view

---
title: scaleEffect(_:anchor:)
description: Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
source: https://developer.apple.com/documentation/swiftui/view/scaleeffect(_:anchor:)
timestamp: 2026-02-13T19:33:33.197Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.

The amount to scale the view in the view in both the horizontal and vertical directions.

The anchor point with a default of [center](/documentation/swiftui/unitpoint/center) that indicates the starting position for the scale operation.

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling transform to a view.

- [scaledToFill()](/documentation/swiftui/view/scaledtofill())
- [scaledToFit()](/documentation/swiftui/view/scaledtofit())
- [scaleEffect(x:y:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:anchor:))
- [scaleEffect(x:y:z:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:z:anchor:))
- [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:))
- [rotationEffect(_:anchor:)](/documentation/swiftui/view/rotationeffect(_:anchor:))
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:anchorz:perspective:))
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:))
- [rotation3DEffect(_:anchor:)](/documentation/swiftui/view/rotation3deffect(_:anchor:))
- [rotation3DEffect(_:axis:anchor:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:))
- [transformEffect(_:)](/documentation/swiftui/view/transformeffect(_:))
- [transform3DEffect(_:)](/documentation/swiftui/view/transform3deffect(_:))
- [projectionEffect(_:)](/documentation/swiftui/view/projectioneffect(_:))
- [ProjectionTransform](/documentation/swiftui/projectiontransform)
- [ContentMode](/documentation/swiftui/contentmode)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> ModifiedContent<Self, _UniformScaleEffect>
```

Example 2 (swift):
```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(2, anchor: .leading)
    .border(Color.gray)
```

---

## ScrollViewReader

**URL:** https://sosumi.ai/documentation/swiftui/scrollviewreader?.md

**Contents:**
- Overview
- Conforms To
- Creating a scroll view reader
- Configuring a scroll view reader
- Creating a scroll view

---
title: ScrollViewReader
description: A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
source: https://developer.apple.com/documentation/swiftui/scrollviewreader
timestamp: 2026-02-13T19:33:11.025Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.

The scroll view reader’s content view builder receives a [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) instance; you use the proxy’s [scrollTo(_:anchor:)](/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)) to perform scrolling.

The following example creates a [Scroll View](/documentation/swiftui/scrollview) containing 100 views that together display a color gradient. It also contains two buttons, one each at the top and bottom. The top button tells the [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) to scroll to the bottom button, and vice versa.

> [!IMPORTANT]
> You may not use the [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) during execution of the `content` view builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/scrollviewreader/init(content:)) Creates an instance that can perform programmatic scrolling of its child scroll views.

- [content](/documentation/swiftui/scrollviewreader/content) The view builder that creates the reader’s content.

- [ScrollView](/documentation/swiftui/scrollview)
- [ScrollViewProxy](/documentation/swiftui/scrollviewproxy)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct ScrollViewReader<Content> where Content : View
```

Example 2 (swift):
```swift
@Namespace var topID
@Namespace var bottomID

var body: some View {
    ScrollViewReader { proxy in
        ScrollView {
            Button("Scroll to Bottom") {
                withAnimation {
                    proxy.scrollTo(bottomID)
                }
            }
            .id(topID)

            VStack(spacing: 0) {
                ForEach(0..<100) { i in
                    color(fraction: Double(i) / 100)
                        .frame(height: 32)
                }
            }

            Button("Top") {
                withAnimation {
                    proxy.scrollTo(topID)
                }
            }
            .id(bottomID)
        }
    }
}

func color(fraction: Double) -> Color {
    Color(red: fraction, green: 1 - fraction, blue: 0.5)
}
```

---

## foregroundStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/foregroundstyle(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Styling content

---
title: foregroundStyle(_:)
description: Sets a view’s foreground elements to use a given style.
source: https://developer.apple.com/documentation/swiftui/view/foregroundstyle(_:)
timestamp: 2026-02-13T19:33:41.691Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets a view’s foreground elements to use a given style.

The color or pattern to use when filling in the foreground elements. To indicate a specific value, use [Color](/documentation/swiftui/color) or [image(_:sourceRect:scale:)](/documentation/swiftui/shapestyle/image(_:sourcerect:scale:)), or one of the gradient types, like [linearGradient(colors:startPoint:endPoint:)](/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)). To set a style that’s relative to the containing view’s style, use one of the semantic styles, like [primary](/documentation/swiftui/shapestyle/primary).

A view that uses the given foreground style.

Use this method to style foreground content like text, shapes, and template images (including symbols):

The example above creates a row of [teal](/documentation/swiftui/shapestyle/teal) foreground elements:

You can use any style that conforms to the [Shape Style](/documentation/swiftui/shapestyle) protocol, like the [teal](/documentation/swiftui/shapestyle/teal) color in the example above, or the [linearGradient(colors:startPoint:endPoint:)](/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)) gradient shown below:

> [!TIP]
> If you want to fill a single [Shape](/documentation/swiftui/shape) instance with a style, use the [fill(style:)](/documentation/swiftui/shape/fill(style:)) shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a [Color](/documentation/swiftui/color) that you load from an asset catalog can have different light and dark appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a style of their own, but instead modify other styles. In particular, they modify the primary level of the current foreground style to the degree given by the hierarchical style’s name. To find the current foreground style to modify, SwiftUI looks for the innermost containing style that you apply with the `foregroundStyle(_:)` or the [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)) modifier. If you haven’t specified a style, SwiftUI uses the default foreground style, as in the following example:

If you add a foreground style on the enclosing [VStack](/documentation/swiftui/vstack), the hierarchical styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect for foreground elements in that view, or in any of its child views, that it would otherwise gain from adding a background material — for example, using the [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)) modifier. However, hierarchical styles applied to the default foreground don’t disable vibrancy.

- [border(_:width:)](/documentation/swiftui/view/border(_:width:))
- [foregroundStyle(_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:))
- [foregroundStyle(_:_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:_:))
- [backgroundStyle(_:)](/documentation/swiftui/view/backgroundstyle(_:))
- [backgroundStyle](/documentation/swiftui/environmentvalues/backgroundstyle)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [AnyShapeStyle](/documentation/swiftui/anyshapestyle)
- [Gradient](/documentation/swiftui/gradient)
- [MeshGradient](/documentation/swiftui/meshgradient)
- [AnyGradient](/documentation/swiftui/anygradient)
- [ShadowStyle](/documentation/swiftui/shadowstyle)
- [Glass](/documentation/swiftui/glass)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
HStack {
    Image(systemName: "triangle.fill")
    Text("Hello, world!")
    RoundedRectangle(cornerRadius: 5)
        .frame(width: 40, height: 20)
}
.foregroundStyle(.teal)
```

Example 3 (swift):
```swift
Text("Gradient Text")
    .font(.largeTitle)
    .foregroundStyle(
        .linearGradient(
            colors: [.yellow, .blue],
            startPoint: .top,
            endPoint: .bottom
        )
    )
```

Example 4 (swift):
```swift
VStack(alignment: .leading) {
    Label("Primary", systemImage: "1.square.fill")
    Label("Secondary", systemImage: "2.square.fill")
        .foregroundStyle(.secondary)
}
```

---

## onHover(perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onhover(perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to hover events

---
title: onHover(perform:)
description: Adds an action to perform when the user moves the pointer over or away from the view’s frame.
source: https://developer.apple.com/documentation/swiftui/view/onhover(perform:)
timestamp: 2026-02-13T19:35:20.236Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+

> Adds an action to perform when the user moves the pointer over or away from the view’s frame.

The action to perform whenever the pointer enters or exits this view’s frame. If the pointer is in the view’s frame, the `action` closure passes `true` as a parameter; otherwise, `false`.

A view that triggers `action` when the pointer enters or exits this view’s frame.

Calling this method defines a region for detecting pointer movement with the size and position of this view.

- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:))
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:))
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:))
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:))
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled)
- [HoverPhase](/documentation/swiftui/hoverphase)
- [HoverEffectPhaseOverride](/documentation/swiftui/hovereffectphaseoverride)
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect)
- [OrnamentHoverEffect](/documentation/swiftui/ornamenthovereffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onHover(perform action: @escaping (Bool) -> Void) -> some View
```

---

## accentColor(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/accentcolor(_:)?.md

**Contents:**
- Parameters
- Discussion
- Graphics and rendering modifiers

---
title: accentColor(_:)
description: Sets the accent color for this view and the views it contains.
source: https://developer.apple.com/documentation/swiftui/view/accentcolor(_:)
timestamp: 2026-02-13T19:33:45.474Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the accent color for this view and the views it contains.

The color to use as an accent color. Set the value to `nil` to use the inherited accent color.

Use `accentColor(_:)` when you want to apply a broad theme color to your app’s user interface. Some styles of controls use the accent color as a default tint color.

> [!NOTE]
> In macOS, SwiftUI applies customization of the accent color only if the user chooses Multicolor under General > Accent color in System Preferences.

In the example below, the outer [VStack](/documentation/swiftui/vstack) contains two child views. The first is a button with the default accent color. The second is a [VStack](/documentation/swiftui/vstack) that contains a button and a slider, both of which adopt the purple accent color of their containing view. Note that the [Text](/documentation/swiftui/text) element used as a label alongside the `Slider` retains its default color.

- [mask(_:)](/documentation/swiftui/view/mask(_:))
- [animation(_:)](/documentation/swiftui/view/animation(_:)-1hc0p)
- [cornerRadius(_:antialiased:)](/documentation/swiftui/view/cornerradius(_:antialiased:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func accentColor(_ accentColor: Color?) -> some View
```

Example 2 (swift):
```swift
VStack(spacing: 20) {
    Button(action: {}) {
        Text("Regular Button")
    }
    VStack {
        Button(action: {}) {
            Text("Accented Button")
        }
        HStack {
            Text("Accented Slider")
            Slider(value: $sliderValue, in: -100...100, step: 0.1)
        }
    }
    .accentColor(.purple)
}
```

---

## Applying Liquid Glass to custom views

**URL:** https://sosumi.ai/documentation/swiftui/applying-liquid-glass-to-custom-views?.md

**Contents:**
- Overview
- Apply and configure Liquid Glass effects
- Combine multiple views with Liquid Glass containers
- Morph Liquid Glass effects during transitions
- Optimize performance when using Liquid Glass effects
- Styling views with Liquid Glass

---
title: Applying Liquid Glass to custom views
description: Configure, combine, and morph views using Liquid Glass effects.
source: https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views
timestamp: 2026-02-13T19:36:48.664Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

> Configure, combine, and morph views using Liquid Glass effects.

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Liquid Glass is a material that blurs content behind it, reflects color and light of surrounding content, and reacts to touch and pointer interactions in real time. Standard components in SwiftUI use Liquid Glass. Adopt Liquid Glass on custom components to move, combine, and morph them into one another with unique animations and transitions.

To learn about Liquid Glass and more, see [Landmarks-Building-an-app-with-Liquid](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass).

Use the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier to add Liquid Glass effects to a view. By default, the modifier uses the [regular](/documentation/swiftui/glass/regular) variant of [Glass](/documentation/swiftui/glass) and applies the given effect within a [Capsule](/documentation/swiftui/capsule) shape behind the view’s content.

Configure the effect to customize your components in a variety of ways:

- Use different shapes to have a consistent look and feel across custom components in your app. For example, use a rounded rectangle if you’re applying the effect to larger components that would look odd as a `Capsule` or [Circle](/documentation/swiftui/circle).
- Assign a tint color to suggest prominence.
- Add [interactive(_:)](/documentation/swiftui/glass/interactive(_:)) to custom components to make them react to touch and pointer interactions. This applies the same responsive and fluid reactions that [glass](/documentation/swiftui/primitivebuttonstyle/glass) provides to standard buttons.

In the examples below, observe how to apply Liquid Glass effects to a view, use an alternate shape with a specific corner radius, and create a tinted view that responds to interactivity:

Use [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) when applying Liquid Glass effects on multiple views to achieve the best rendering performance. A container also allows views with Liquid Glass effects to blend their shapes together and to morph in and out of each other during transitions. Inside a container, each view with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier renders with the effects behind it.

Customize the spacing on the container to control how the Liquid Glass effects behind views interact with one another. The larger the spacing value on the container, the sooner the Liquid Glass effects behind views blend together and merge the shapes during a transition. A spacing value on the container that’s larger than the spacing of an interior [HStack](/documentation/swiftui/hstack), [VStack](/documentation/swiftui/vstack), or other layout container causes Liquid Glass effects to blend together at rest because the views are too close to each other. Animating views in or out causes the shapes to morph apart or together as the space in the container changes.

The `glassEffect(_:in:)` modifier captures the content to send to the container to render. Apply the `glassEffect(_:in:)` modifier after other modifiers that affect the appearance of the view.

In the example below, two images are placed close to each other and the Liquid Glass effects begin to blend their shapes together. This creates a fluid animation as components move around each other within a container:

In some cases, you want the geometries of multiple views to contribute to a single Liquid Glass effect capsule, even when your content is at rest. Use the [glassEffectUnion(id:namespace:)](/documentation/swiftui/view/glasseffectunion(id:namespace:)) modifier to specify that a view contributes to a unified effect with a particular ID. This combines all effects with a similar shape, Liquid Glass effect, and ID into a single shape with the applied Liquid Glass material. This is especially useful when creating views dynamically, or with views that live outside of a layout container, like an `HStack` or `VStack`.

Morphing effects occur during transitions or animations between views with Liquid Glass effects. Coordinate transitions between views with effects in a container by using the [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)) modifier. [Glass Effect Transition](/documentation/swiftui/glasseffecttransition) allows you to specify the type of transition to use when you want to add or remove effects within a container. For effects you want to add or remove that are positioned within the container’s assigned spacing, the default transition type is [matched Geometry](/documentation/swiftui/glasseffecttransition/matchedgeometry).

If you prefer to have a simpler transition or to create a custom transition, use the [materialize](/documentation/swiftui/glasseffecttransition/materialize) transition and [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)). Use the `materialize` transition for effects you want to add or remove that are farther from each other than the container’s assigned spacing. To provide people with a consistent experience, use `matchedGeometry` and `materialize` transitions across your apps. The system applies more than opacity changes with the available transition types.

Associate each Liquid Glass effect with a unique identifier within a namespace that the [Namespace](/documentation/swiftui/namespace) property wrapper provides. These IDs ensure SwiftUI animates the same shapes correctly when a shape appears or disappears due to view hierarchy changes. SwiftUI uses the spacing provided to the effect container along with the geometry of the shapes themselves to determine when and which appropriate shapes to morph into and out of.

The `glassEffectID(_:in:)` and `glassEffectTransition(_:)` modifiers only affect their content during view hierarchy transitions or animations.

In the example below, the eraser image transitions into and out of the pencil image when the `isExpanded` variable changes. The `GlassEffectContainer` has a spacing value of `40.0`, and the `HStack` within it has a spacing of `40.0`. This morphs the eraser image into the pencil image when the eraser’s nearest edge is less than or equal to the container’s spacing.

Creating too many Liquid Glass effect containers and applying too many effects to views outside of containers can degrade performance. Limit the use of Liquid Glass effects onscreen at the same time. Additionally, optimize how your app spends rendering time as people use it. To learn how to improve the performance of your UI, see [](https://developer.apple.com/videos/play/tech-talks/10855/) and [](https://developer.apple.com/videos/play/wwdc2025/306/).

- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16.0))

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(.regular.tint(.orange).interactive())
```

Example 2 (swift):
```swift
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

        Image(systemName: "eraser.fill")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

            // An `offset` shows how Liquid Glass effects react to each other in a container.
            // Use animations and components appearing and disappearing to obtain effects that look purposeful.
            .offset(x: -40.0, y: 0.0)
    }
}
```

Example 3 (swift):
```swift
let symbolSet: [String] = ["cloud.bolt.rain.fill", "sun.rain.fill", "moon.stars.fill", "moon.fill"]

GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(symbolSet.indices, id: \.self) { item in
            Image(systemName: symbolSet[item])
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectUnion(id: item < 2 ? "1" : "2", namespace: namespace)
        }
    }
}
```

Example 4 (swift):
```swift
@State private var isExpanded: Bool = false
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 40.0) {
        HStack(spacing: 40.0) {
            Image(systemName: "scribble.variable")
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

            if isExpanded {
                Image(systemName: "eraser.fill")
                    .frame(width: 80.0, height: 80.0)
                    .font(.system(size: 36))
                    .glassEffect()
                    .glassEffectID("eraser", in: namespace)
            }
        }
    }

    Button("Toggle") {
        withAnimation {
            isExpanded.toggle()
        }
    }
    .buttonStyle(.glass)
}
```

---

## border(_:width:)

**URL:** https://sosumi.ai/documentation/swiftui/view/border(_:width:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Styling content

---
title: border(_:width:)
description: Adds a border to this view with the specified style and width.
source: https://developer.apple.com/documentation/swiftui/view/border(_:width:)
timestamp: 2026-02-13T19:33:24.825Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a border to this view with the specified style and width.

A value that conforms to the [Shape Style](/documentation/swiftui/shapestyle) protocol, like a [Color](/documentation/swiftui/color) or [Hierarchical Shape Style](/documentation/swiftui/hierarchicalshapestyle), that SwiftUI uses to fill the border.

The thickness of the border. The default is 1 pixel.

A view that adds a border with the specified style and width to this view.

Use this modifier to draw a border of a specified width around the view’s frame. By default, the border appears inside the bounds of this view. For example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same width before adding the border:

- [foregroundStyle(_:)](/documentation/swiftui/view/foregroundstyle(_:))
- [foregroundStyle(_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:))
- [foregroundStyle(_:_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:_:))
- [backgroundStyle(_:)](/documentation/swiftui/view/backgroundstyle(_:))
- [backgroundStyle](/documentation/swiftui/environmentvalues/backgroundstyle)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [AnyShapeStyle](/documentation/swiftui/anyshapestyle)
- [Gradient](/documentation/swiftui/gradient)
- [MeshGradient](/documentation/swiftui/meshgradient)
- [AnyGradient](/documentation/swiftui/anygradient)
- [ShadowStyle](/documentation/swiftui/shadowstyle)
- [Glass](/documentation/swiftui/glass)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func border<S>(_ content: S, width: CGFloat = 1) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
Text("Purple border inside the view bounds.")
    .border(Color.purple, width: 4)
```

Example 3 (swift):
```swift
Text("Purple border outside the view bounds.")
    .padding(4)
    .border(Color.purple, width: 4)
```

---

## onDisappear(perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ondisappear(perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to view life cycle updates

---
title: onDisappear(perform:)
description: Adds an action to perform after this view disappears.
source: https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)
timestamp: 2026-02-13T19:34:59.192Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform after this view disappears.

The action to perform. If `action` is `nil`, the call has no effect.

A view that triggers `action` after it disappears.

The exact moment that SwiftUI calls this method depends on the specific view type that you apply it to, but the `action` closure doesn’t execute until the view disappears from the interface.

- [onAppear(perform:)](/documentation/swiftui/view/onappear(perform:))
- [task(priority:_:)](/documentation/swiftui/view/task(priority:_:))
- [task(id:priority:_:)](/documentation/swiftui/view/task(id:priority:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onDisappear(perform action: (() -> Void)? = nil) -> some View
```

---

## navigationTitle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/navigationtitle(_:)?.md

**Contents:**
- Parameters
- Discussion
- Setting titles for navigation content

---
title: navigationTitle(_:)
description: Configures the view’s title for purposes of navigation, using a string binding.
source: https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:)
timestamp: 2026-02-13T19:36:37.672Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Configures the view’s title for purposes of navigation, using a string binding.

The text of the title.

In iOS, iPadOS, and macOS, this allows editing the navigation title when the title is displayed in the toolbar.

Refer to the [Configure-Your-Apps-Navigation](/documentation/swiftui/configure-your-apps-navigation-titles) article for more information on navigation title modifiers.

- [navigationSubtitle(_:)](/documentation/swiftui/view/navigationsubtitle(_:))
- [navigationDocument(_:)](/documentation/swiftui/view/navigationdocument(_:))
- [navigationDocument(_:preview:)](/documentation/swiftui/view/navigationdocument(_:preview:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func navigationTitle(_ title: Binding<String>) -> some View
```

---

## labelStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/labelstyle(_:)?.md

**Contents:**
- Discussion
- Displaying text

---
title: labelStyle(_:)
description: Sets the style for labels within this view.
source: https://developer.apple.com/documentation/swiftui/view/labelstyle(_:)
timestamp: 2026-02-13T19:36:15.857Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Sets the style for labels within this view.

Use this modifier to set a specific style for all labels within a view:

- [Text](/documentation/swiftui/text)
- [Label](/documentation/swiftui/label)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func labelStyle<S>(_ style: S) -> some View where S : LabelStyle
```

Example 2 (swift):
```swift
VStack {
    Label("Fire", systemImage: "flame.fill")
    Label("Lightning", systemImage: "bolt.fill")
}
.labelStyle(MyCustomLabelStyle())
```

---

## onTapGesture(count:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ontapgesture(count:perform:)?.md

**Contents:**
- Parameters
- Discussion
- Recognizing tap gestures

---
title: onTapGesture(count:perform:)
description: Adds an action to perform when this view recognizes a tap gesture.
source: https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:)
timestamp: 2026-02-13T19:35:12.859Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 16.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform when this view recognizes a tap gesture.

The number of taps or clicks required to trigger the action closure provided in `action`. Defaults to `1`.

The action to perform.

Use this method to perform the specified `action` when the user clicks or taps on the view or container `count` times.

> [!NOTE]
> If you create a control that’s functionally equivalent to a [Button](/documentation/swiftui/button), use [Button Style](/documentation/swiftui/buttonstyle) to create a customized button instead.

In the example below, the color of the heart images changes to a random color from the `colors` array whenever the user clicks or taps on the view twice:

- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
- [TapGesture](/documentation/swiftui/tapgesture)
- [SpatialTapGesture](/documentation/swiftui/spatialtapgesture)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onTapGesture(count: Int = 1, perform action: @escaping () -> Void) -> some View
```

Example 2 (swift):
```swift
struct TapGestureExample: View {
    let colors: [Color] = [.gray, .red, .orange, .yellow,
                           .green, .blue, .purple, .pink]
    @State private var fgColor: Color = .gray

    var body: some View {
        Image(systemName: "heart.fill")
            .resizable()
            .frame(width: 200, height: 200)
            .foregroundColor(fgColor)
            .onTapGesture(count: 2) {
                fgColor = colors.randomElement()!
            }
    }
}
```

---

## padding(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/padding(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Adding padding around a view

---
title: padding(_:_:)
description: Adds an equal padding amount to specific edges of this view.
source: https://developer.apple.com/documentation/swiftui/view/padding(_:_:)
timestamp: 2026-02-13T19:32:17.090Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an equal padding amount to specific edges of this view.

The set of edges to pad for this view. The default is [all](/documentation/swiftui/edge/set/all).

An amount, given in points, to pad this view on the specified edges. If you set the value to `nil`, SwiftUI uses a platform-specific default amount. The default value of this parameter is `nil`.

A view that’s padded by the specified amount on the specified edges.

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from [Set](/documentation/swiftui/edge/set), or by specifying an [Option Set](/documentation/Swift/OptionSet) that contains edge values:

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

You can omit either or both of the parameters. If you omit the `length`, SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI applies the padding to all edges. Omit both to add a default padding all the way around a view. SwiftUI chooses a default amount of padding that’s appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use [padding(_:)](/documentation/swiftui/view/padding(_:)-6pgqq). To pad all outside edges of a view by a specified amount, use [padding(_:)](/documentation/swiftui/view/padding(_:)-68shk).

- [padding(_:)](/documentation/swiftui/view/padding(_:))
- [padding3D(_:)](/documentation/swiftui/view/padding3d(_:))
- [padding3D(_:_:)](/documentation/swiftui/view/padding3d(_:_:))
- [scenePadding(_:)](/documentation/swiftui/view/scenepadding(_:))
- [scenePadding(_:edges:)](/documentation/swiftui/view/scenepadding(_:edges:))
- [ScenePadding](/documentation/swiftui/scenepadding)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func padding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
```

Example 2 (swift):
```swift
VStack {
    Text("Text padded by 20 points on the bottom and trailing edges.")
        .padding([.bottom, .trailing], 20)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

Example 3 (swift):
```swift
VStack {
    Text("Text with default padding.")
        .padding()
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

---

## onChange(of:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onchange(of:perform:)?.md

**Contents:**
- Discussion
- Input and events modifiers

---
title: onChange(of:perform:)
description: Adds an action to perform when the given value changes.
source: https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)
timestamp: 2026-02-13T19:35:08.480Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Adds an action to perform when the given value changes.

Use this modifier to trigger a side effect when a value changes, like the value associated with an [Environment](/documentation/swiftui/environment) value or a [Binding](/documentation/swiftui/binding). For example, you can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

The system passes the new value into the closure. If you need the old value, capture it in the closure.

- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)-36x9h)
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:))
- [onLongPressGesture(minimumDuration:pressing:perform:)](/documentation/swiftui/view/onlongpressgesture(minimumduration:pressing:perform:))
- [onPasteCommand(of:perform:)](/documentation/swiftui/view/onpastecommand(of:perform:)-4f78f)
- [onPasteCommand(of:validator:perform:)](/documentation/swiftui/view/onpastecommand(of:validator:perform:)-964k1)
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)-2vr9o)
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:))
- [focusable(_:onFocusChange:)](/documentation/swiftui/view/focusable(_:onfocuschange:))
- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-8gyrl)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some View where V : Equatable
```

Example 2 (swift):
```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

Example 3 (swift):
```swift
.onChange(of: scenePhase) { newScenePhase in
    if newScenePhase == .background {
        Task.detached(priority: .background) {
            // ...
        }
    }
}
```

---

## disabled(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/disabled(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Managing view interaction

---
title: disabled(_:)
description: Adds a condition that controls whether users can interact with this view.
source: https://developer.apple.com/documentation/swiftui/view/disabled(_:)
timestamp: 2026-02-13T19:33:49.646Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a condition that controls whether users can interact with this view.

A Boolean value that determines whether users can interact with this view.

A view that controls whether users can interact with this view.

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button isn’t interactive because the outer `disabled(_:)` modifier overrides the inner one:

- [isEnabled](/documentation/swiftui/environmentvalues/isenabled)
- [interactionActivityTrackingTag(_:)](/documentation/swiftui/view/interactionactivitytrackingtag(_:))
- [invalidatableContent(_:)](/documentation/swiftui/view/invalidatablecontent(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func disabled(_ disabled: Bool) -> some View
```

Example 2 (swift):
```swift
HStack {
    Button(Text("Press")) {}
    .disabled(false)
}
.disabled(true)
```

---

## contextMenu(menuItems:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contextmenu(menuitems:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Creating context menus

---
title: contextMenu(menuItems:)
description: Adds a context menu to a view.
source: https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)
timestamp: 2026-02-13T19:35:28.566Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

> Adds a context menu to a view.

A closure that produces the menu’s contents. You can deactivate the context menu by returning nothing from the closure.

A view that can display a context menu.

Use this modifier to add a context menu to a view in your app’s user interface. Compose the menu by returning controls like [Button](/documentation/swiftui/button), [Toggle](/documentation/swiftui/toggle), and [Picker](/documentation/swiftui/picker) from the `menuItems` closure. You can also use [Menu](/documentation/swiftui/menu) to define submenus or [Section](/documentation/swiftui/section) to group items.

The following example creates a [Text](/documentation/swiftui/text) view that has a context menu with two buttons:

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system displays the menu next to the content:

The system dismisses the menu if someone makes a selection, or taps or clicks outside the menu.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)) with a [context Menu Preview](/documentation/swiftui/contentshapekinds/contextmenupreview) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

> [!NOTE]
> This view modifier produces a context menu on macOS, but that platform doesn’t display a preview.

If you want to show a different preview, you can use [contextMenu(menuItems:preview:)](/documentation/swiftui/view/contextmenu(menuitems:preview:)). To add a context menu to a container that supports selection, like a [List](/documentation/swiftui/list) or a [Table](/documentation/swiftui/table), and to distinguish between menu activation on a selection and activation in an empty area of the container, use [contextMenu(forSelectionType:menu:primaryAction:)](/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:)).

- [contextMenu(menuItems:preview:)](/documentation/swiftui/view/contextmenu(menuitems:preview:))
- [contextMenu(forSelectionType:menu:primaryAction:)](/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
```

Example 2 (swift):
```swift
Text("Turtle Rock")
    .padding()
    .contextMenu {
        Button {
            // Add this item to a list of favorites.
        } label: {
            Label("Add to Favorites", systemImage: "heart")
        }
        Button {
            // Open Maps and center it on this item.
        } label: {
            Label("Show in Maps", systemImage: "mappin")
        }
    }
```

---

## searchable(text:placement:prompt:)

**URL:** https://sosumi.ai/documentation/swiftui/view/searchable(text:placement:prompt:)?.md

**Contents:**
- Parameters
- Discussion
- Searching your app’s data model

---
title: searchable(text:placement:prompt:)
description: Marks this view as searchable, which configures the display of a search field.
source: https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)
timestamp: 2026-02-13T19:36:39.788Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Marks this view as searchable, which configures the display of a search field.

The text to display and edit in the search field.

The preferred placement of the search field within the containing view hierarchy.

The key for the localized prompt of the search field which provides users with guidance on what to search for.

For more information about using searchable modifiers, see [Adding-a-search-interface-to-your](/documentation/swiftui/adding-a-search-interface-to-your-app).

- [Adding a search interface to your app](/documentation/swiftui/adding-a-search-interface-to-your-app)
- [Performing a search operation](/documentation/swiftui/performing-a-search-operation)
- [searchable(text:tokens:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:))
- [searchable(text:editableTokens:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:editabletokens:placement:prompt:token:))
- [SearchFieldPlacement](/documentation/swiftui/searchfieldplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey) -> some View
```

---

## focused(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/focused(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Managing focus state

---
title: focused(_:)
description: Modifies this view by binding its focus state to the given Boolean state value.
source: https://developer.apple.com/documentation/swiftui/view/focused(_:)
timestamp: 2026-02-13T19:35:22.323Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Modifies this view by binding its focus state to the given Boolean state value.

The focus state to bind. When focus moves to the view, the binding sets the bound value to `true`. If a caller sets the value to  `true` programmatically, then focus moves to the modified view. When focus leaves the modified view, the binding sets the value to `false`. If a caller sets the value to `false`, SwiftUI automatically dismisses focus.

Use this modifier to cause the view to receive focus whenever the `condition` value is `true`. You can use this modifier to observe the focus state of a single view, or programmatically set and remove focus from the view.

In the following example, a single [Text Field](/documentation/swiftui/textfield) accepts a user’s desired `username`. The text field binds its focus state to the Boolean value `usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name is available. If the name is unavailable, the button sets `usernameFieldIsFocused` to `true`, which causes focus to return to the text field, so the user can enter a different name.

To control focus by matching a value, use the [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) method instead.

- [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:))
- [isFocused](/documentation/swiftui/environmentvalues/isfocused)
- [FocusState](/documentation/swiftui/focusstate)
- [FocusedValue](/documentation/swiftui/focusedvalue)
- [Entry()](/documentation/swiftui/entry())
- [FocusedValueKey](/documentation/swiftui/focusedvaluekey)
- [FocusedBinding](/documentation/swiftui/focusedbinding)
- [searchFocused(_:)](/documentation/swiftui/view/searchfocused(_:))
- [searchFocused(_:equals:)](/documentation/swiftui/view/searchfocused(_:equals:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func focused(_ condition: FocusState<Bool>.Binding) -> some View
```

Example 2 (swift):
```swift
@State private var username: String = ""
@FocusState private var usernameFieldIsFocused: Bool
@State private var showUsernameTaken = false

var body: some View {
    VStack {
        TextField("Choose a username.", text: $username)
            .focused($usernameFieldIsFocused)
        if showUsernameTaken {
            Text("That username is taken. Please choose another.")
        }
        Button("Submit") {
            showUsernameTaken = false
            if !isUserNameAvailable(username: username) {
                usernameFieldIsFocused = true
                showUsernameTaken = true
            }
        }
    }
}
```

---

## alert(_:isPresented:actions:message:)

**URL:** https://sosumi.ai/documentation/swiftui/view/alert(_:ispresented:actions:message:)?.md

**Contents:**
- Parameters
- Discussion
- Presenting an alert

---
title: alert(_:isPresented:actions:message:)
description: Presents an alert with a message when a given condition is true using a text view as a title.
source: https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:message:)
timestamp: 2026-02-13T19:36:27.115Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Presents an alert with a message when a given condition is true using a text view as a title.

The title of the alert.

A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

A [View Builder](/documentation/swiftui/viewbuilder) returning the alert’s actions.

A [View Builder](/documentation/swiftui/viewbuilder) returning the message for the alert.

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence.  You can influence the default button by assigning it the [default Action](/documentation/swiftui/keyboardshortcut/defaultaction) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [cancel](/documentation/swiftui/buttonrole/cancel).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [Text](/documentation/swiftui/text). Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

- [AlertScene](/documentation/swiftui/alertscene)
- [alert(_:isPresented:actions:)](/documentation/swiftui/view/alert(_:ispresented:actions:))
- [alert(_:isPresented:presenting:actions:)](/documentation/swiftui/view/alert(_:ispresented:presenting:actions:))
- [alert(isPresented:error:actions:)](/documentation/swiftui/view/alert(ispresented:error:actions:))
- [alert(_:isPresented:presenting:actions:message:)](/documentation/swiftui/view/alert(_:ispresented:presenting:actions:message:))
- [alert(isPresented:error:actions:message:)](/documentation/swiftui/view/alert(ispresented:error:actions:message:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func alert<A, M>(_ title: Text, isPresented: Binding<Bool>, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```

Example 2 (swift):
```swift
struct Login: View {
    @State private var didFail = false
    let alertTitle: String = "Login failed."

    var body: some View {
        LoginForm(didFail: $didFail)
            .alert(
                Text(alertTitle),
                isPresented: $didFail
            ) {
                Button("OK") {
                    // Handle the acknowledgement.
                }
            } message: {
               Text("Please check your credentials and try again.")
            }
    }
}
```

---

## onDrag(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ondrag(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving items using item providers

---
title: onDrag(_:)
description: Activates this view as the source of a drag and drop operation.
source: https://developer.apple.com/documentation/swiftui/view/ondrag(_:)
timestamp: 2026-02-13T19:35:16.026Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+

> Activates this view as the source of a drag and drop operation.

A closure that returns a single [NSItem Provider](/documentation/Foundation/NSItemProvider) that represents the draggable data from this view.

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)) with a [drag Preview](/documentation/swiftui/contentshapekinds/dragpreview) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

If you want to show a different preview, you can use [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)).

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:))
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:))
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:))
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:))
- [DropDelegate](/documentation/swiftui/dropdelegate)
- [DropProposal](/documentation/swiftui/dropproposal)
- [DropOperation](/documentation/swiftui/dropoperation)
- [DropInfo](/documentation/swiftui/dropinfo)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
```

---

## GlassEffectContainer

**URL:** https://sosumi.ai/documentation/swiftui/glasseffectcontainer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Styling views with Liquid Glass

---
title: GlassEffectContainer
description: A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
source: https://developer.apple.com/documentation/swiftui/glasseffectcontainer
timestamp: 2026-02-13T19:37:02.469Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.

Use a container with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier. Each view with a Liquid Glass effect contributes a shape rendered with the effect to a set of shapes. SwiftUI renders the effects together, improving rendering performance and allowing the effects to interact with and morph into one another.

Configure how shapes interact with one another by customizing the default spacing value of the container. As shapes near one another, their paths start to blend into one another. The higher the spacing, the sooner blending begins as the shapes approach each other.

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [init(spacing:content:)](/documentation/swiftui/glasseffectcontainer/init(spacing:content:)) Creates a glass effect container with the provided spacing, extracting glass shapes from the provided content.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct GlassEffectContainer<Content> where Content : View
```

---

## RoundedRectangle

**URL:** https://sosumi.ai/documentation/swiftui/roundedrectangle?.md

**Contents:**
- Conforms To
- Creating a rounded rectangle
- Getting the shape’s characteristics
- Supporting types
- Creating rectangular shapes

---
title: RoundedRectangle
description: A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/roundedrectangle
timestamp: 2026-02-13T19:34:09.983Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(cornerRadius:style:)](/documentation/swiftui/roundedrectangle/init(cornerradius:style:)) Creates a new rounded rectangle shape.
- [init(cornerSize:style:)](/documentation/swiftui/roundedrectangle/init(cornersize:style:)) Creates a new rounded rectangle shape.

- [cornerSize](/documentation/swiftui/roundedrectangle/cornersize) The width and height of the rounded rectangle’s corners.
- [style](/documentation/swiftui/roundedrectangle/style) The style of corners drawn by the rounded rectangle.

- [animatableData](/documentation/swiftui/roundedrectangle/animatabledata) The data to animate.

- [Rectangle](/documentation/swiftui/rectangle)
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii)
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct RoundedRectangle
```

---
