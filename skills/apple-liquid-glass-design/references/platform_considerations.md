# Apple-Liquid-Glass-Design - Platform Considerations

**Pages:** 1

---

## UIDesignRequiresCompatibility

**URL:** https://sosumi.ai/documentation/BundleResources/Information-Property-List/UIDesignRequiresCompatibility?.md

**Contents:**
- Discussion
- Styling

---
title: UIDesignRequiresCompatibility
description: A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.
source: https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIDesignRequiresCompatibility
timestamp: 2026-02-13T00:19:37.611Z
---

**Navigation:** [BundleResources](/documentation/BundleResources) › [Information-Property-List](/documentation/BundleResources/Information-Property-List)

**Property List Key**

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, tvOS 26.0+

> A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.

> [!WARNING]
> Temporarily use this key while reviewing and refining your app’s UI for the design in the latest SDKs.

If `YES`, the system runs the app using a compatibility mode for UI elements. The compatibility mode displays the app as it looks when built against previous versions of the SDKs.

If `NO`, the system uses the UI design of the running OS, with no compatibility mode. Absence of the key, or `NO`, is the default value for apps linking against the latest SDKs.

- [UIUserInterfaceStyle](/documentation/bundleresources/information-property-list/uiuserinterfacestyle)
- [UIViewEdgeAntialiasing](/documentation/bundleresources/information-property-list/uiviewedgeantialiasing)
- [UIWhitePointAdaptivityStyle](/documentation/bundleresources/information-property-list/uiwhitepointadaptivitystyle)
- [UIViewGroupOpacity](/documentation/bundleresources/information-property-list/uiviewgroupopacity)
- [UIRequiresFullScreenIgnoredStartingWithVersion](/documentation/bundleresources/information-property-list/uirequiresfullscreenignoredstartingwithversion)
- [UISupportsAssistiveAccess](/documentation/bundleresources/information-property-list/uisupportsassistiveaccess)
- [UISupportsFullScreenInAssistiveAccess](/documentation/bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess)
- [NSPrefersDisplaySafeAreaCompatibilityMode](/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode)
- [NSAccentColorName](/documentation/bundleresources/information-property-list/nsaccentcolorname)
- [NSWidgetBackgroundColorName](/documentation/bundleresources/information-property-list/nswidgetbackgroundcolorname)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

---
