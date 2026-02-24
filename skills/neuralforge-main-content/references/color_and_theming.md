# Neuralforge-Main-Content - Color And Theming

**Pages:** 2

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
timestamp: 2026-02-13T03:44:15.797Z
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
timestamp: 2026-02-13T03:44:17.831Z
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
