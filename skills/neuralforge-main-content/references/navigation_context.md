# Neuralforge-Main-Content - Navigation Context

**Pages:** 2

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
timestamp: 2026-02-13T03:44:22.001Z
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
timestamp: 2026-02-13T03:44:24.181Z
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
