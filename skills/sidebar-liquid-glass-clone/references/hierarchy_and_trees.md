# Sidebar-Liquid-Glass-Clone - Hierarchy And Trees

**Pages:** 2

---

## OutlineGroup

**URL:** https://sosumi.ai/documentation/swiftui/outlinegroup?.md

**Contents:**
- Overview
  - Type parameters
- Conforms To
- Creating an outline group
- Supporting types
- Disclosing information progressively

---
title: OutlineGroup
description: A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
source: https://developer.apple.com/documentation/swiftui/outlinegroup
timestamp: 2026-02-13T01:04:20.176Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.

Use an outline group when you need a view that can represent a hierarchy of data by using disclosure views. This allows the user to navigate the tree structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a simplified view of a file system. Passing the root of this tree and the key path of its children allows you to quickly create a visual representation of the file system.

Five generic type constraints define a specific `OutlineGroup` instance:

- `Data`: The type of a collection containing the children of an element in the tree-shaped data.
- `ID`: The type of the identifier for an element.
- `Parent`: The type of the visual representation of an element whose children property is non-`nil`
- `Leaf`: The type of the visual representation of an element whose children property is `nil`.
- `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

- [Copyable](/documentation/Swift/Copyable)
- [TableRowContent](/documentation/swiftui/tablerowcontent)
- [View](/documentation/swiftui/view)

- [init(_:children:)](/documentation/swiftui/outlinegroup/init(_:children:)) Creates an outline group from a collection of root data elements and a key path to element’s children.
- [init(_:children:content:)](/documentation/swiftui/outlinegroup/init(_:children:content:)) Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](/documentation/swiftui/outlinegroup/init(_:id:children:content:)) Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.

- [OutlineSubgroupChildren](/documentation/swiftui/outlinesubgroupchildren) A type-erased view representing the children in an outline subgroup.

- [DisclosureGroup](/documentation/swiftui/disclosuregroup)
- [disclosureGroupStyle(_:)](/documentation/swiftui/view/disclosuregroupstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable
```

Example 2 (swift):
```swift
struct FileItem: Hashable, Identifiable, CustomStringConvertible {
    var id: Self { self }
    var name: String
    var children: [FileItem]? = nil
    var description: String {
        switch children {
        case nil:
            return "📄 \(name)"
        case .some(let children):
            return children.isEmpty ? "📂 \(name)" : "📁 \(name)"
        }
    }
}

let data =
  FileItem(name: "users", children:
    [FileItem(name: "user1234", children:
      [FileItem(name: "Photos", children:
        [FileItem(name: "photo001.jpg"),
         FileItem(name: "photo002.jpg")]),
       FileItem(name: "Movies", children:
         [FileItem(name: "movie001.mp4")]),
          FileItem(name: "Documents", children: [])
      ]),
     FileItem(name: "newuser", children:
       [FileItem(name: "Documents", children: [])
       ])
    ])

OutlineGroup(data, children: \.children) { item in
    Text("\(item.description)")
}
```

---

## DisclosureGroup

**URL:** https://sosumi.ai/documentation/swiftui/disclosuregroup?.md

**Contents:**
- Overview
- Conforms To
- Creating a disclosure group
- Disclosing information progressively

---
title: DisclosureGroup
description: A view that shows or hides another content view, based on the state of a disclosure control.
source: https://developer.apple.com/documentation/swiftui/disclosuregroup
timestamp: 2026-02-13T01:04:22.352Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> A view that shows or hides another content view, based on the state of a disclosure control.

A disclosure group view consists of a label to identify the contents, and a control to show and hide the contents. Showing the contents puts the disclosure group into the “expanded” state, and hiding them makes the disclosure group “collapsed”.

In the following example, a disclosure group contains two toggles and an embedded disclosure group. The top level disclosure group exposes its expanded state with the bound property, `topLevelExpanded`. By expanding the disclosure group, the user can use the toggles to update the state of the `toggleStates` structure.

- [View](/documentation/swiftui/view)

- [init(_:content:)](/documentation/swiftui/disclosuregroup/init(_:content:)) Creates a disclosure group, using a provided localized string key to create a text view for the label.
- [init(content:label:)](/documentation/swiftui/disclosuregroup/init(content:label:)) Creates a disclosure group with the given label and content views.
- [init(_:isExpanded:content:)](/documentation/swiftui/disclosuregroup/init(_:isexpanded:content:)) Creates a disclosure group, using a provided localized string key to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded:content:label:)](/documentation/swiftui/disclosuregroup/init(isexpanded:content:label:)) Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).

- [OutlineGroup](/documentation/swiftui/outlinegroup)
- [disclosureGroupStyle(_:)](/documentation/swiftui/view/disclosuregroupstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct DisclosureGroup<Label, Content> where Label : View, Content : View
```

Example 2 (swift):
```swift
struct ToggleStates {
    var oneIsOn: Bool = false
    var twoIsOn: Bool = true
}
@State private var toggleStates = ToggleStates()
@State private var topExpanded: Bool = true

var body: some View {
    DisclosureGroup("Items", isExpanded: $topExpanded) {
        Toggle("Toggle 1", isOn: $toggleStates.oneIsOn)
        Toggle("Toggle 2", isOn: $toggleStates.twoIsOn)
        DisclosureGroup("Sub-items") {
            Text("Sub-item 1")
        }
    }
}
```

---
