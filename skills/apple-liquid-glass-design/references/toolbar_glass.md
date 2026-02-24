# Apple-Liquid-Glass-Design - Toolbar Glass

**Pages:** 2

---

## fixed

**URL:** https://sosumi.ai/documentation/swiftui/spacersizing/fixed?.md

---
title: fixed
description: The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.
source: https://developer.apple.com/documentation/swiftui/spacersizing/fixed
timestamp: 2026-02-13T00:19:20.490Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [spacersizing](/documentation/swiftui/spacersizing)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

> The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static let fixed: SpacerSizing
```

---

## ToolbarSpacer

**URL:** https://sosumi.ai/documentation/swiftui/toolbarspacer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Populating a toolbar

---
title: ToolbarSpacer
description: A standard space item in toolbars.
source: https://developer.apple.com/documentation/swiftui/toolbarspacer
timestamp: 2026-02-13T00:19:18.501Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

> A standard space item in toolbars.

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)

- [init(_:placement:)](/documentation/swiftui/toolbarspacer/init(_:placement:)) Creates a toolbar spacer item with the specified sizing behavior and placement.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarSpacer
```

Example 2 (swift):
```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

---
