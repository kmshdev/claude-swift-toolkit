# Swiftui-Components - Presentations

**Pages:** 2

---

## Landmarks: Refining the system provided Liquid Glass effect in toolbars

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars?.md

**Contents:**
- Overview
- Organize the toolbar items into logical groupings
- App features

---
title: Landmarks: Refining the system provided Liquid Glass effect in toolbars
description: Organize toolbars into related groupings to improve their appearance and utility.
source: https://developer.apple.com/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars
timestamp: 2026-02-13T19:36:58.606Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Organize toolbars into related groupings to improve their appearance and utility.

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to refine the system provided glass effect in toolbars. In `LandmarkDetailView`, the sample adds toolbar items for:

- sharing a landmark
- adding or removing a landmark from a list of Favorites
- adding or removing a landmark from Collections
- showing or hiding the inspector

The system applies Liquid Glass to the toolbar items automatically.

To organize the toolbar items into logical groupings, the sample adds [Toolbar Spacer](/documentation/swiftui/toolbarspacer) items and passes [fixed](/documentation/swiftui/spacersizing/fixed) as the `sizing` parameter to divide the toolbar into sections:

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect)
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
.toolbar {
    ToolbarSpacer(.flexible)

    ToolbarItem {
        ShareLink(item: landmark, preview: landmark.sharePreview)
    }

    ToolbarSpacer(.fixed)
    
    ToolbarItemGroup {
        LandmarkFavoriteButton(landmark: landmark)
        LandmarkCollectionsMenu(landmark: landmark)
    }
    
    ToolbarSpacer(.fixed)

    ToolbarItem {
        Button("Info", systemImage: "info") {
            modelData.selectedLandmark = landmark
            modelData.isLandmarkInspectorPresented.toggle()
        }
    }
}
```

---

## Landmarks: Extending horizontal scrolling under a sidebar or inspector

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector?.md

**Contents:**
- Overview
- Configure the scroll view
- App features

---
title: Landmarks: Extending horizontal scrolling under a sidebar or inspector
description: Improve your horizontal scrollbar’s appearance by extending it under a sidebar or inspector.
source: https://developer.apple.com/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector
timestamp: 2026-02-13T19:36:56.651Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Improve your horizontal scrollbar’s appearance by extending it under a sidebar or inspector.

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to extend horizontal scrolling under a sidebar or inspector. Within each continent section in `LandmarksView`, an instance of `LandmarkHorizontalListView` shows a horizontally scrolling list of landmark views. When open, the landmark views can scroll underneath the sidebar or inspector.

To achieve this effect, the sample configures the `LandmarkHorizontalListView` so it touches the leading and trailing edges. When a scroll view touches the sidebar or inspector, the system automatically adjusts it to scroll under the sidebar or inspector and then off the edge of the screen.

The sample adds a [Spacer](/documentation/swiftui/spacer) at the beginning of the [Scroll View](/documentation/swiftui/scrollview) to inset the content so it aligns with the title padding:

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect)
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars)
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: Constants.standardPadding) {
        Spacer()
            .frame(width: Constants.standardPadding)
        ForEach(landmarkList) { landmark in
            //...
        }
    }
}
```

---
