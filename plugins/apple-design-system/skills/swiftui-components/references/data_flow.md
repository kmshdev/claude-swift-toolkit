# Swiftui-Components - Data Flow

**Pages:** 8

---

## Binding

**URL:** https://sosumi.ai/documentation/swiftui/binding?.md

**Contents:**
- Overview
- Conforms To
- Creating a binding
- Getting the value
- Managing changes
- Subscripts
- Default Implementations
- Creating and sharing view state

---
title: Binding
description: A property wrapper type that can read and write a value owned by a source of truth.
source: https://developer.apple.com/documentation/swiftui/binding
timestamp: 2026-02-13T19:35:34.865Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A property wrapper type that can read and write a value owned by a source of truth.

Use a binding to create a two-way connection between a property that stores data, and a view that displays and changes the data. A binding connects a property to a source of truth stored elsewhere, instead of storing data directly. For example, a button that toggles between play and pause can create a binding to a property of its parent view using the `Binding` property wrapper.

The parent view declares a property to hold the playing state, using the [State](/documentation/swiftui/state) property wrapper to indicate that this property is the value’s source of truth.

When `PlayerView` initializes `PlayButton`, it passes a binding of its state property into the button’s binding property. Applying the `$` prefix to a property wrapped value returns its [projected Value](/documentation/swiftui/state/projectedvalue), which for a state property wrapper returns a binding to the value.

Whenever the user taps the `PlayButton`, the `PlayerView` updates its `isPlaying` state.

A binding conforms to `Sendable` only if its wrapped value type also conforms to `Sendable`. It is always safe to pass a sendable binding between different concurrency domains. However, reading from or writing to a binding’s wrapped value from a different concurrency domain may or may not be safe, depending on how the binding was created. SwiftUI will issue a warning at runtime if it detects a binding being used in a way that may compromise data safety.

> [!NOTE]
> To create bindings to properties of a type that conforms to the [Observable](/documentation/Observation/Observable) protocol, use the [Bindable](/documentation/swiftui/bindable) property wrapper. For more information, see [Migrating-from-the-observable-object-protocol-to-the-observable](/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro).

- [BidirectionalCollection](/documentation/Swift/BidirectionalCollection)
- [Collection](/documentation/Swift/Collection)
- [Copyable](/documentation/Swift/Copyable)
- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Identifiable](/documentation/Swift/Identifiable)
- [RandomAccessCollection](/documentation/Swift/RandomAccessCollection)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Sequence](/documentation/Swift/Sequence)

- [init(_:)](/documentation/swiftui/binding/init(_:)) Creates a binding by projecting the base value to a hashable value.
- [init(projectedValue:)](/documentation/swiftui/binding/init(projectedvalue:)) Creates a binding from the value of another binding.
- [init(get:set:)](/documentation/swiftui/binding/init(get:set:)) Creates a binding with closures that read and write the binding value.
- [constant(_:)](/documentation/swiftui/binding/constant(_:)) Creates a binding with an immutable value.

- [wrappedValue](/documentation/swiftui/binding/wrappedvalue) The underlying value referenced by the binding variable.
- [projectedValue](/documentation/swiftui/binding/projectedvalue) A projection of the binding value that returns a binding.
- [subscript(dynamicMember:)](/documentation/swiftui/binding/subscript(dynamicmember:)) Returns a binding to the resulting value of a given key path.

- [id](/documentation/swiftui/binding/id) The stable identity of the entity associated with this instance, corresponding to the  of the binding’s wrapped value.
- [animation(_:)](/documentation/swiftui/binding/animation(_:)) Specifies an animation to perform when the binding value changes.
- [transaction(_:)](/documentation/swiftui/binding/transaction(_:)) Specifies a transaction for the binding.
- [transaction](/documentation/swiftui/binding/transaction) The binding’s transaction.

- [subscript(_:)](/documentation/swiftui/binding/subscript(_:))

- [Identifiable Implementations](/documentation/swiftui/binding/identifiable-implementations)

- [Managing user interface state](/documentation/swiftui/managing-user-interface-state)
- [State](/documentation/swiftui/state)
- [Bindable](/documentation/swiftui/bindable)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper @dynamicMemberLookup struct Binding<Value>
```

Example 2 (swift):
```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

Example 3 (swift):
```swift
struct PlayerView: View {
    var episode: Episode
    @State private var isPlaying: Bool = false

    var body: some View {
        VStack {
            Text(episode.title)
                .foregroundStyle(isPlaying ? .primary : .secondary)
            PlayButton(isPlaying: $isPlaying) // Pass a binding.
        }
    }
}
```

---

## StateObject

**URL:** https://sosumi.ai/documentation/swiftui/stateobject?.md

**Contents:**
- Overview
  - Share state objects with subviews
  - Initialize state objects using external data
  - Force reinitialization by changing view identity
- Conforms To
- Creating a state object
- Getting the value
- Creating model data

---
title: StateObject
description: A property wrapper type that instantiates an observable object.
source: https://developer.apple.com/documentation/swiftui/stateobject
timestamp: 2026-02-13T19:35:43.162Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A property wrapper type that instantiates an observable object.

Use a state object as the single source of truth for a reference type that you store in a view hierarchy. Create a state object in an [App](/documentation/swiftui/app), [Scene](/documentation/swiftui/scene), or [View](/documentation/swiftui/view) by applying the `@StateObject` attribute to a property declaration and providing an initial value that conforms to the [Observable Object](/documentation/Combine/ObservableObject) protocol. Declare state objects as private to prevent setting them from a memberwise initializer, which can conflict with the storage management that SwiftUI provides:

SwiftUI creates a new instance of the model object only once during the lifetime of the container that declares the state object. For example, SwiftUI doesn’t create a new instance if a view’s inputs change, but does create a new instance if the identity of a view changes. When published properties of the observable object change, SwiftUI updates any view that depends on those properties, like the [Text](/documentation/swiftui/text) view in the above example.

> [!NOTE]
> If you need to store a value type, like a structure, string, or integer, use the [State](/documentation/swiftui/state) property wrapper instead. Also use [State](/documentation/swiftui/state) if you need to store a reference type that conforms to the [Observable()](/documentation/Observation/Observable()) protocol. To learn more about Observation in SwiftUI, see [Managing-model-data-in-your](/documentation/swiftui/managing-model-data-in-your-app).

You can pass a state object into a subview through a property that has the [Observed Object](/documentation/swiftui/observedobject) attribute. Alternatively, add the object to the environment of a view hierarchy by applying the [environmentObject(_:)](/documentation/swiftui/view/environmentobject(_:)) modifier to a view, like `MySubView` in the above code. You can then read the object inside `MySubView` or any of its descendants using the [Environment Object](/documentation/swiftui/environmentobject) attribute:

Get a [Binding](/documentation/swiftui/binding) to the state object’s properties using the dollar sign (`$`) operator. Use a binding when you want to create a two-way connection. In the above code, the [Toggle](/documentation/swiftui/toggle) controls the model’s `isEnabled` value through a binding.

When a state object’s initial state depends on data that comes from outside its container, you can call the object’s initializer explicitly from within its container’s initializer. For example, suppose the data model from the previous example takes a `name` input during initialization and you want to use a value for that name that comes from outside the view. You can do this with a call to the state object’s initializer inside an explicit initializer that you create for the view:

Use caution when doing this. SwiftUI only initializes a state object the first time you call its initializer in a given view. This ensures that the object provides stable storage even as the view’s inputs change. However, it might result in unexpected behavior or unwanted side effects if you explicitly initialize the state object.

In the above example, if the `name` input to `MyInitializableView` changes, SwiftUI reruns the view’s initializer with the new value. However, SwiftUI runs the autoclosure that you provide to the state object’s initializer only the first time you call the state object’s initializer, so the model’s stored `name` value doesn’t change.

Explicit state object initialization works well when the external data that the object depends on doesn’t change for a given instance of the object’s container. For example, you can create two views with different constant names:

> [!IMPORTANT]
> Even for a configurable state object, you still declare it as private. This ensures that you can’t accidentally set the parameter through a memberwise initializer of the view, because doing so can conflict with the framework’s storage management and produce unexpected results.

If you want SwiftUI to reinitialize a state object when a view input changes, make sure that the view’s identity changes at the same time. One way to do this is to bind the view’s identity to the value that changes using the [id(_:)](/documentation/swiftui/view/id(_:)) modifier. For example, you can ensure that the identity of an instance of `MyInitializableView` changes when its `name` input changes:

> [!NOTE]
> If your view appears inside a [For Each](/documentation/swiftui/foreach), it implicitly receives an [id(_:)](/documentation/swiftui/view/id(_:)) modifier that uses the identifier of the corresponding data element.

If you need the view to reinitialize state based on changes in more than one value, you can combine the values into a single identifier using a [Hasher](/documentation/Swift/Hasher). For example, if you want to update the data model in `MyInitializableView` when the values of either `name` or `isEnabled` change, you can combine both variables into a single hash:

Then apply the combined hash to the view as an identifier:

Be mindful of the performance cost of reinitializing the state object every time the input changes. Also, changing view identity can have side effects. For example, SwiftUI doesn’t automatically animate changes inside the view if the view’s identity changes at the same time. Also, changing the identity resets *all* state held by the view, including values that you manage as [State](/documentation/swiftui/state), [Focus State](/documentation/swiftui/focusstate), [Gesture State](/documentation/swiftui/gesturestate), and so on.

- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(wrappedValue:)](/documentation/swiftui/stateobject/init(wrappedvalue:)) Creates a new state object with an initial wrapped value.

- [wrappedValue](/documentation/swiftui/stateobject/wrappedvalue) The underlying value referenced by the state object.
- [projectedValue](/documentation/swiftui/stateobject/projectedvalue) A projection of the state object that creates bindings to its properties.

- [Managing model data in your app](/documentation/swiftui/managing-model-data-in-your-app)
- [Migrating from the Observable Object protocol to the Observable macro](/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro)
- [Observable()](/documentation/Observation/Observable())
- [Monitoring data changes in your app](/documentation/swiftui/monitoring-model-data-changes-in-your-app)
- [ObservedObject](/documentation/swiftui/observedobject)
- [ObservableObject](/documentation/Combine/ObservableObject)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct StateObject<ObjectType> where ObjectType : ObservableObject
```

Example 2 (swift):
```swift
class DataModel: ObservableObject {
    @Published var name = "Some Name"
    @Published var isEnabled = false
}

struct MyView: View {
    @StateObject private var model = DataModel() // Create the state object.

    var body: some View {
        Text(model.name) // Updates when the data model changes.
        MySubView()
            .environmentObject(model)
    }
}
```

Example 3 (swift):
```swift
struct MySubView: View {
    @EnvironmentObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

Example 4 (swift):
```swift
struct MyInitializableView: View {
    @StateObject private var model: DataModel

    init(name: String) {
        // SwiftUI ensures that the following initialization uses the
        // closure only once during the lifetime of the view, so
        // later changes to the view's name input have no effect.
        _model = StateObject(wrappedValue: DataModel(name: name))
    }

    var body: some View {
        VStack {
            Text("Name: \(model.name)")
        }
    }
}
```

---

## Observable

**URL:** https://sosumi.ai/documentation/Observation/Observable?.md

**Contents:**
- Overview
- Observable conformance

---
title: Observable
description: A type that emits notifications to observers when underlying data changes.
source: https://developer.apple.com/documentation/Observation/Observable
timestamp: 2026-02-13T19:35:45.240Z
---

**Navigation:** [Observation](/documentation/Observation)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> A type that emits notifications to observers when underlying data changes.

Conforming to this protocol signals to other APIs that the type supports observation. However, applying the `Observable` protocol by itself to a type doesn’t add observation functionality to the type. Instead, always use the [Observable()](/documentation/observation/observable()) macro when adding observation support to a type.

- [Observable()](/documentation/observation/observable())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol Observable
```

---

## 

**URL:** https://sosumi.ai/documentation/Observation?.md

**Contents:**
- Observable conformance
- Change tracking
  - Creating an observation registrar
  - Receiving change notifications
  - Identifying transactional access
- Observation in SwiftUI
- Structures
  - Structures
  - Initializers
  - Type Methods

---
title: Observation
source: https://developer.apple.com/documentation/Observation
timestamp: 2026-02-13T19:35:47.335Z
---

- [macro Observable()](/documentation/observation/observable())
- [Observable](/documentation/observation/observable)

- [func withObservationTracking<T>(() -> T, onChange: @autoclosure () -> () -> Void) -> T](/documentation/observation/withobservationtracking(_:onchange:))
- [ObservationRegistrar](/documentation/observation/observationregistrar)

- [init()](/documentation/observation/observationregistrar/init())

- [func willSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](/documentation/observation/observationregistrar/willset(_:keypath:))
- [func didSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](/documentation/observation/observationregistrar/didset(_:keypath:))

- [func access<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](/documentation/observation/observationregistrar/access(_:keypath:))
- [func withMutation<Subject, Member, T>(of: Subject, keyPath: KeyPath<Subject, Member>, () throws -> T) rethrows -> T](/documentation/observation/observationregistrar/withmutation(of:keypath:_:))

- [Managing model data in your app](/documentation/swiftui/managing-model-data-in-your-app)
- [Migrating from the Observable Object protocol to the Observable macro](/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro)

- [Observations](/documentation/observation/observations)

- [Observations.Iterator](/documentation/observation/observations/iterator)

- [init(() throws(Failure) -> Element)](/documentation/observation/observations/init(_:))

- [static func untilFinished(() throws(Failure) -> Observations<Element, Failure>.Iteration) -> Observations<Element, Failure>](/documentation/observation/observations/untilfinished(_:))

- [Observations.Iteration](/documentation/observation/observations/iteration)

- [case finish](/documentation/observation/observations/iteration/finish)
- [case next(Element)](/documentation/observation/observations/iteration/next(_:))

- [macro ObservationIgnored()](/documentation/observation/observationignored())
- [macro ObservationTracked()](/documentation/observation/observationtracked())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

---

## EnvironmentValues

**URL:** https://sosumi.ai/documentation/swiftui/environmentvalues?.md

**Contents:**
- Overview
- Conforms To
- Creating and accessing values
- Accessibility
- Actions
- Authentication
- Controls and input
- Display characteristics
- Global objects
- Scrolling

---
title: EnvironmentValues
description: A collection of environment values propagated through a view hierarchy.
source: https://developer.apple.com/documentation/swiftui/environmentvalues
timestamp: 2026-02-13T19:35:39.297Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A collection of environment values propagated through a view hierarchy.

SwiftUI exposes a collection of values to your app’s views in an `EnvironmentValues` structure. To read a value from the structure, declare a property using the [Environment](/documentation/swiftui/environment) property wrapper and specify the value’s key path. For example, you can read the current locale:

Use the property you declare to dynamically control a view’s layout. SwiftUI automatically sets or updates many environment values, like [pixel Length](/documentation/swiftui/environmentvalues/pixellength), [scene Phase](/documentation/swiftui/environmentvalues/scenephase), or [locale](/documentation/swiftui/environmentvalues/locale), based on device characteristics, system state, or user settings. For others, like [line Limit](/documentation/swiftui/environmentvalues/linelimit), SwiftUI provides a reasonable default value.

You can set or override some values using the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) view modifier:

The value that you set affects the environment for the view that you modify — including its descendants in the view hierarchy — but only up to the point where you apply a different environment modifier.

SwiftUI provides dedicated view modifiers for setting some values, which typically makes your code easier to read. For example, rather than setting the [line Limit](/documentation/swiftui/environmentvalues/linelimit) value directly, as in the previous example, you should instead use the [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)) modifier:

In some cases, using a dedicated view modifier provides additional functionality. For example, you must use the [preferredColorScheme(_:)](/documentation/swiftui/view/preferredcolorscheme(_:)) modifier rather than setting [color Scheme](/documentation/swiftui/environmentvalues/colorscheme) directly to ensure that the new value propagates up to the presenting container when presenting a view like a popover:

Create a custom environment value by declaring a new property in an extension to the environment values structure and applying the [Entry()](/documentation/swiftui/entry()) macro to the variable declaration:

Clients of your value then access the value in the usual way, reading it with the [Environment](/documentation/swiftui/environment) property wrapper, and setting it with the `myCustomValue` view modifier.

- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)

- [init()](/documentation/swiftui/environmentvalues/init()) Creates an environment values instance.
- [subscript(_:)](/documentation/swiftui/environmentvalues/subscript(_:)) Accesses the environment value associated with a custom key.
- [description](/documentation/swiftui/environmentvalues/description) A string that represents the contents of the environment values instance.

- [accessibilityAssistiveAccessEnabled](/documentation/swiftui/environmentvalues/accessibilityassistiveaccessenabled) A Boolean value that indicates whether Assistive Access is in use.
- [accessibilityDimFlashingLights](/documentation/swiftui/environmentvalues/accessibilitydimflashinglights) Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [accessibilityDifferentiateWithoutColor](/documentation/swiftui/environmentvalues/accessibilitydifferentiatewithoutcolor) Whether the system preference for Differentiate without Color is enabled.
- [accessibilityEnabled](/documentation/swiftui/environmentvalues/accessibilityenabled) A Boolean value that indicates whether the user has enabled an assistive technology.
- [accessibilityInvertColors](/documentation/swiftui/environmentvalues/accessibilityinvertcolors) Whether the system preference for Invert Colors is enabled.
- [accessibilityLargeContentViewerEnabled](/documentation/swiftui/environmentvalues/accessibilitylargecontentviewerenabled) Whether the Large Content Viewer is enabled.
- [accessibilityPlayAnimatedImages](/documentation/swiftui/environmentvalues/accessibilityplayanimatedimages) Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [accessibilityPrefersHeadAnchorAlternative](/documentation/swiftui/environmentvalues/accessibilityprefersheadanchoralternative) Whether the system setting to prefer alternatives to head-anchored content is on.
- [accessibilityQuickActionsEnabled](/documentation/swiftui/environmentvalues/accessibilityquickactionsenabled) A Boolean that indicates whether the quick actions feature is enabled.
- [accessibilityReduceMotion](/documentation/swiftui/environmentvalues/accessibilityreducemotion) Whether the system preference for Reduce Motion is enabled.
- [accessibilityReduceTransparency](/documentation/swiftui/environmentvalues/accessibilityreducetransparency) Whether the system preference for Reduce Transparency is enabled.
- [accessibilityShowButtonShapes](/documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes) Whether the system preference for Show Button Shapes is enabled.
- [accessibilitySwitchControlEnabled](/documentation/swiftui/environmentvalues/accessibilityswitchcontrolenabled) A Boolean value that indicates whether the Switch Control motor accessibility feature is in use.
- [accessibilityVoiceOverEnabled](/documentation/swiftui/environmentvalues/accessibilityvoiceoverenabled) A Boolean value that indicates whether the VoiceOver screen reader is in use.
- [legibilityWeight](/documentation/swiftui/environmentvalues/legibilityweight) The font weight to apply to text.

- [dismiss](/documentation/swiftui/environmentvalues/dismiss) An action that dismisses the current presentation.
- [dismissSearch](/documentation/swiftui/environmentvalues/dismisssearch) An action that ends the current search interaction.
- [dismissWindow](/documentation/swiftui/environmentvalues/dismisswindow) A window dismissal action stored in a view’s environment.
- [openImmersiveSpace](/documentation/swiftui/environmentvalues/openimmersivespace) An action that presents an immersive space.
- [dismissImmersiveSpace](/documentation/swiftui/environmentvalues/dismissimmersivespace) An immersive space dismissal action stored in a view’s environment.
- [newDocument](/documentation/swiftui/environmentvalues/newdocument) An action in the environment that presents a new document.
- [openDocument](/documentation/swiftui/environmentvalues/opendocument) An action in the environment that presents an existing document.
- [openURL](/documentation/swiftui/environmentvalues/openurl) An action that opens a URL.
- [openWindow](/documentation/swiftui/environmentvalues/openwindow) A window presentation action stored in a view’s environment.
- [pushWindow](/documentation/swiftui/environmentvalues/pushwindow) A window presentation action stored in a view’s environment.
- [purchase](/documentation/swiftui/environmentvalues/purchase) An action that starts an in-app purchase.
- [refresh](/documentation/swiftui/environmentvalues/refresh) A refresh action stored in a view’s environment.
- [rename](/documentation/swiftui/environmentvalues/rename) An action that activates the standard rename interaction.
- [resetFocus](/documentation/swiftui/environmentvalues/resetfocus) An action that requests the focus system to reevaluate default focus.
- [openSettings](/documentation/swiftui/environmentvalues/opensettings) A Settings presentation action stored in a view’s environment.

- [authorizationController](/documentation/swiftui/environmentvalues/authorizationcontroller) A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [webAuthenticationSession](/documentation/swiftui/environmentvalues/webauthenticationsession) A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.

- [buttonRepeatBehavior](/documentation/swiftui/environmentvalues/buttonrepeatbehavior) Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [controlSize](/documentation/swiftui/environmentvalues/controlsize) The size to apply to controls within a view.
- [defaultWheelPickerItemHeight](/documentation/swiftui/environmentvalues/defaultwheelpickeritemheight) The default height of an item in a wheel-style picker, such as a date picker.
- [keyboardShortcut](/documentation/swiftui/environmentvalues/keyboardshortcut) The keyboard shortcut that buttons in this environment will be triggered with.
- [menuIndicatorVisibility](/documentation/swiftui/environmentvalues/menuindicatorvisibility) The menu indicator visibility to apply to controls within a view.
- [menuOrder](/documentation/swiftui/environmentvalues/menuorder) The preferred order of items for menus presented from this view.
- [searchSuggestionsPlacement](/documentation/swiftui/environmentvalues/searchsuggestionsplacement) The current placement of search suggestions.
- [preferredPencilDoubleTapAction](/documentation/swiftui/environmentvalues/preferredpencildoubletapaction) The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction) The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.

- [appearsActive](/documentation/swiftui/environmentvalues/appearsactive) Whether views and styles in this environment should prefer an active appearance over an inactive appearance.
- [colorScheme](/documentation/swiftui/environmentvalues/colorscheme) The color scheme of this environment.
- [colorSchemeContrast](/documentation/swiftui/environmentvalues/colorschemecontrast) The contrast associated with the color scheme of this environment.
- [displayScale](/documentation/swiftui/environmentvalues/displayscale) The display scale of this environment.
- [horizontalSizeClass](/documentation/swiftui/environmentvalues/horizontalsizeclass) The horizontal size class of this environment.
- [imageScale](/documentation/swiftui/environmentvalues/imagescale) The image scale for this environment.
- [pixelLength](/documentation/swiftui/environmentvalues/pixellength) The size of a pixel on the screen.
- [sidebarRowSize](/documentation/swiftui/environmentvalues/sidebarrowsize) The current size of sidebar rows.
- [verticalSizeClass](/documentation/swiftui/environmentvalues/verticalsizeclass) The vertical size class of this environment.
- [immersiveSpaceDisplacement](/documentation/swiftui/environmentvalues/immersivespacedisplacement) The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [labelsVisibility](/documentation/swiftui/environmentvalues/labelsvisibility) The labels visibility set by .
- [materialActiveAppearance](/documentation/swiftui/environmentvalues/materialactiveappearance) The behavior materials should use for their active state, defaulting to .
- [TabBarPlacement](/documentation/swiftui/tabbarplacement) A placement for tabs in a tab view.
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle) The label style to apply to controls within a toolbar.

- [calendar](/documentation/swiftui/environmentvalues/calendar) The current calendar that views should use when handling dates.
- [documentConfiguration](/documentation/swiftui/environmentvalues/documentconfiguration) The configuration of a document in a .
- [locale](/documentation/swiftui/environmentvalues/locale) The current locale that views should use.
- [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext)
- [modelContext](/documentation/swiftui/environmentvalues/modelcontext) The SwiftData model context that will be used for queries and other model operations within this environment.
- [timeZone](/documentation/swiftui/environmentvalues/timezone) The current time zone that views should use when handling dates.
- [undoManager](/documentation/swiftui/environmentvalues/undomanager) The undo manager used to register a view’s undo operations.

- [isScrollEnabled](/documentation/swiftui/environmentvalues/isscrollenabled) A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.
- [horizontalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/horizontalscrollindicatorvisibility) The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/verticalscrollindicatorvisibility) The visiblity to apply to scroll indicators of any vertically scrollable content.
- [scrollDismissesKeyboardMode](/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode) The way that scrollable content interacts with the software keyboard.
- [horizontalScrollBounceBehavior](/documentation/swiftui/environmentvalues/horizontalscrollbouncebehavior) The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](/documentation/swiftui/environmentvalues/verticalscrollbouncebehavior) The scroll bounce mode for the vertical axis of scrollable views.

- [editMode](/documentation/swiftui/environmentvalues/editmode) An indication of whether the user can edit the contents of a view associated with this environment.
- [isActivityFullscreen](/documentation/swiftui/environmentvalues/isactivityfullscreen) A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [isEnabled](/documentation/swiftui/environmentvalues/isenabled) A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [isFocused](/documentation/swiftui/environmentvalues/isfocused) Returns whether the nearest focusable ancestor has focus.
- [isFocusEffectEnabled](/documentation/swiftui/environmentvalues/isfocuseffectenabled) A Boolean value that indicates whether the view associated with this environment allows focus effects to be displayed.
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled) A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [isLuminanceReduced](/documentation/swiftui/environmentvalues/isluminancereduced) A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [isPresented](/documentation/swiftui/environmentvalues/ispresented) A Boolean value that indicates whether the view associated with this environment is currently presented.
- [isSceneCaptured](/documentation/swiftui/environmentvalues/isscenecaptured) The current capture state.
- [isSearching](/documentation/swiftui/environmentvalues/issearching) A Boolean value that indicates when the user is searching.
- [isTabBarShowingSections](/documentation/swiftui/environmentvalues/istabbarshowingsections) A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [scenePhase](/documentation/swiftui/environmentvalues/scenephase) The current phase of the scene.
- [supportsMultipleWindows](/documentation/swiftui/environmentvalues/supportsmultiplewindows) A Boolean value that indicates whether the current platform supports opening multiple windows.

- [displayStoreKitMessage](/documentation/swiftui/environmentvalues/displaystorekitmessage)
- [requestReview](/documentation/swiftui/environmentvalues/requestreview)

- [allowsTightening](/documentation/swiftui/environmentvalues/allowstightening) A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [autocorrectionDisabled](/documentation/swiftui/environmentvalues/autocorrectiondisabled) A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [dynamicTypeSize](/documentation/swiftui/environmentvalues/dynamictypesize) The current Dynamic Type size.
- [font](/documentation/swiftui/environmentvalues/font) The default font of this environment.
- [layoutDirection](/documentation/swiftui/environmentvalues/layoutdirection) The layout direction associated with the current environment.
- [lineLimit](/documentation/swiftui/environmentvalues/linelimit) The maximum number of lines that text can occupy in a view.
- [lineSpacing](/documentation/swiftui/environmentvalues/linespacing) The distance in points between the bottom of one line fragment and the top of the next.
- [minimumScaleFactor](/documentation/swiftui/environmentvalues/minimumscalefactor) The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [multilineTextAlignment](/documentation/swiftui/environmentvalues/multilinetextalignment) An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.
- [textCase](/documentation/swiftui/environmentvalues/textcase) A stylistic override to transform the case of  when displayed, using the environment’s locale.
- [truncationMode](/documentation/swiftui/environmentvalues/truncationmode) A value that indicates how the layout truncates the last line of text to fit into the available space.
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity) A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).

- [allowedDynamicRange](/documentation/swiftui/environmentvalues/alloweddynamicrange) The allowed dynamic range for the view, or nil.
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial) The material underneath the current view.
- [backgroundProminence](/documentation/swiftui/environmentvalues/backgroundprominence) The prominence of the background underneath views associated with this environment.
- [backgroundStyle](/documentation/swiftui/environmentvalues/backgroundstyle) An optional style that overrides the default system background style when set.
- [badgeProminence](/documentation/swiftui/environmentvalues/badgeprominence) The prominence to apply to badges associated with this environment.
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition) The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup) A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [defaultMinListHeaderHeight](/documentation/swiftui/environmentvalues/defaultminlistheaderheight) The default minimum height of a header in a list.
- [defaultMinListRowHeight](/documentation/swiftui/environmentvalues/defaultminlistrowheight) The default minimum height of rows in a list.
- [headerProminence](/documentation/swiftui/environmentvalues/headerprominence) The prominence to apply to section headers within a view.
- [physicalMetrics](/documentation/swiftui/environmentvalues/physicalmetrics) The physical metrics associated with a scene.
- [realityKitScene](/documentation/swiftui/environmentvalues/realitykitscene)
- [realityViewCameraControls](/documentation/swiftui/environmentvalues/realityviewcameracontrols) The camera controls for the reality view.
- [redactionReasons](/documentation/swiftui/environmentvalues/redactionreasons) The current redaction reasons applied to the view hierarchy.
- [springLoadingBehavior](/documentation/swiftui/environmentvalues/springloadingbehavior) The behavior of spring loaded interactions for the views associated with this environment.
- [symbolRenderingMode](/documentation/swiftui/environmentvalues/symbolrenderingmode) The current symbol rendering mode, or  denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [symbolVariants](/documentation/swiftui/environmentvalues/symbolvariants) The symbol variant to use in this environment.
- [worldTrackingLimitations](/documentation/swiftui/environmentvalues/worldtrackinglimitations) The current limitations of the device tracking the user’s surroundings.

- [showsWidgetContainerBackground](/documentation/swiftui/environmentvalues/showswidgetcontainerbackground) An environment variable that indicates whether the background of a widget appears.
- [showsWidgetLabel](/documentation/swiftui/environmentvalues/showswidgetlabel) A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [widgetFamily](/documentation/swiftui/environmentvalues/widgetfamily) The template of the widget — small, medium, or large.
- [widgetRenderingMode](/documentation/swiftui/environmentvalues/widgetrenderingmode) The widget’s rendering mode, based on where the system is displaying it.
- [widgetContentMargins](/documentation/swiftui/environmentvalues/widgetcontentmargins) A property that identifies the content margins of a widget.

- [disableAutocorrection](/documentation/swiftui/environmentvalues/disableautocorrection) A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [sizeCategory](/documentation/swiftui/environmentvalues/sizecategory) The size of content.
- [presentationMode](/documentation/swiftui/environmentvalues/presentationmode) A binding to the current presentation mode of the view associated with this environment.
- [PresentationMode](/documentation/swiftui/presentationmode) An indication whether a view is currently presented by another view.
- [complicationRenderingMode](/documentation/swiftui/environmentvalues/complicationrenderingmode) The complication rendering mode for the current environment.
- [controlActiveState](/documentation/swiftui/environmentvalues/controlactivestate) The active appearance expected of controls in a window.

- [accessibilityShowBorders](/documentation/swiftui/environmentvalues/accessibilityshowborders) Whether the system preference for Show Borders is enabled. On macOS this is true when Increased Contrast is enabled.
- [activityFamily](/documentation/swiftui/environmentvalues/activityfamily) The size family of the current Live Activity.
- [buttonSizing](/documentation/swiftui/environmentvalues/buttonsizing) The preferred sizing behavior of buttons in the view hierarchy.
- [credentialDataManager](/documentation/swiftui/environmentvalues/credentialdatamanager) This environment variable is for SwiftUI clients of the ASCredentialDataManager API. An example usage might look like:
- [credentialExportManager](/documentation/swiftui/environmentvalues/credentialexportmanager) This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [credentialImportManager](/documentation/swiftui/environmentvalues/credentialimportmanager) This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [devicePickerSupports](/documentation/swiftui/environmentvalues/devicepickersupports) Checks for support to present a DevicePicker.
- [findContext](/documentation/swiftui/environmentvalues/findcontext)
- [fontResolutionContext](/documentation/swiftui/environmentvalues/fontresolutioncontext) Information used to resolve a font.
- [imagePlaygroundAllowedGenerationStyles](/documentation/swiftui/environmentvalues/imageplaygroundallowedgenerationstyles)
- [imagePlaygroundPersonalizationPolicy](/documentation/swiftui/environmentvalues/imageplaygroundpersonalizationpolicy)
- [imagePlaygroundSelectedGenerationStyle](/documentation/swiftui/environmentvalues/imageplaygroundselectedgenerationstyle)
- [isActivityUpdateReduced](/documentation/swiftui/environmentvalues/isactivityupdatereduced) A Boolean value that indicates whether the Live Activity update synchronization rate is reduced.
- [isUserAuthenticationEnabled](/documentation/swiftui/environmentvalues/isuserauthenticationenabled) The current system user authentication enablement status.
- [labelIconToTitleSpacing](/documentation/swiftui/environmentvalues/labelicontotitlespacing) The spacing between the icon and title of a label.
- [labelReservedIconWidth](/documentation/swiftui/environmentvalues/labelreservediconwidth) The width reserved for icons in labels.
- [levelOfDetail](/documentation/swiftui/environmentvalues/levelofdetail) The level of detail the view is recommended to have.
- [lineHeight](/documentation/swiftui/environmentvalues/lineheight) The default line height for text influenced by this environment.
- [navigationLinkIndicatorVisibility](/documentation/swiftui/environmentvalues/navigationlinkindicatorvisibility) A value that says whether a built-in navigation link would show a disclosure indicator in the current context.
- [remoteDeviceIdentifier](/documentation/swiftui/environmentvalues/remotedeviceidentifier) An opaque object that identifies the device on which the scene (from which this value is accessed from) is being presented on.
- [requestAgeRange](/documentation/swiftui/environmentvalues/requestagerange) An environment value that provides a platform configured action for requesting age ranges.
- [supportedActivityFamilies](/documentation/swiftui/environmentvalues/supportedactivityfamilies) An environment value that that indicates potential rendered family for a Live Activity.
- [supportsImagePlayground](/documentation/swiftui/environmentvalues/supportsimageplayground) A Boolean value that indicates whether image generation is available on the current device.
- [supportsRemoteScenes](/documentation/swiftui/environmentvalues/supportsremotescenes) Indicates if the current device supports presenting a  on a remote device.
- [surfaceSnappingInfo](/documentation/swiftui/environmentvalues/surfacesnappinginfo) Provides information about the current snap state of the scene.
- [symbolColorRenderingMode](/documentation/swiftui/environmentvalues/symbolcolorrenderingmode) The property specifying how symbol images fill their layers, or nil to use the default fill style.
- [symbolVariableValueMode](/documentation/swiftui/environmentvalues/symbolvariablevaluemode) The current symbol variable value mode, or  denoting that the mode is picked automatically.
- [tabBarPlacement](/documentation/swiftui/environmentvalues/tabbarplacement) The current placement of the tab bar.
- [tabViewBottomAccessoryPlacement](/documentation/swiftui/environmentvalues/tabviewbottomaccessoryplacement) The current placement of the tab view bottom accessory.
- [windowClippingMargins](/documentation/swiftui/environmentvalues/windowclippingmargins)
- [writingToolsBehavior](/documentation/swiftui/environmentvalues/writingtoolsbehavior) The current Writing Tools behavior for text and text input.

- [Environment](/documentation/swiftui/environment)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct EnvironmentValues
```

Example 2 (swift):
```swift
@Environment(\.locale) var locale: Locale
```

Example 3 (swift):
```swift
MyView()
    .environment(\.lineLimit, 2)
```

Example 4 (swift):
```swift
MyView()
    .lineLimit(2)
```

---

## Environment

**URL:** https://sosumi.ai/documentation/swiftui/environment?.md

**Contents:**
- Overview
  - Get an observable object
  - Get an observable object using a key path
- Conforms To
- Creating an environment instance
- Getting the value
- Accessing environment values

---
title: Environment
description: A property wrapper that reads a value from a view’s environment.
source: https://developer.apple.com/documentation/swiftui/environment
timestamp: 2026-02-13T19:35:36.861Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A property wrapper that reads a value from a view’s environment.

Use the `Environment` property wrapper to read a value stored in a view’s environment. Indicate the value to read using an [Environment Values](/documentation/swiftui/environmentvalues) key path in the property declaration. For example, you can create a property that reads the color scheme of the current view using the key path of the [color Scheme](/documentation/swiftui/environmentvalues/colorscheme) property:

You can condition a view’s content on the associated value, which you read from the declared property’s [wrapped Value](/documentation/swiftui/environment/wrappedvalue). As with any property wrapper, you access the wrapped value by directly referring to the property:

If the value changes, SwiftUI updates any parts of your view that depend on the value. For example, that might happen in the above example if the user changes the Appearance settings.

You can use this property wrapper to read — but not set — an environment value. SwiftUI updates some environment values automatically based on system settings and provides reasonable defaults for others. You can override some of these, as well as set custom environment values that you define, using the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) view modifier.

For the complete list of environment values SwiftUI provides, see the properties of the [Environment Values](/documentation/swiftui/environmentvalues) structure. For information about creating custom environment values, see the [Entry()](/documentation/swiftui/entry()) macro.

You can also use `Environment` to get an observable object from a view’s environment. The observable object must conform to the [Observable](/documentation/Observation/Observable) protocol, and your app must set the object in the environment using the object itself or a key path.

To set the object in the environment using the object itself, use the [environment(_:)](/documentation/swiftui/view/environment(_:)) modifier:

To get the observable object using its type, create a property and provide the `Environment` property wrapper the object’s type:

By default, reading an object from the environment returns a non-optional object when using the object type as the key. This default behavior assumes that a view in the current hierarchy previously stored a non-optional instance of the type using the [environment(_:)](/documentation/swiftui/view/environment(_:)) modifier. If a view attempts to retrieve an object using its type and that object isn’t in the environment, SwiftUI throws an exception.

In cases where there is no guarantee that an object is in the environment, retrieve an optional version of the object as shown in the following code. If the object isn’t available the environment, SwiftUI returns `nil` instead of throwing an exception.

To set the object with a key path, use the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifier:

To get the object, create a property and specify the key path:

- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(_:)](/documentation/swiftui/environment/init(_:)) Creates an environment property to read the specified key path.

- [wrappedValue](/documentation/swiftui/environment/wrappedvalue) The current value of the environment property.

- [EnvironmentValues](/documentation/swiftui/environmentvalues)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper struct Environment<Value>
```

Example 2 (swift):
```swift
@Environment(\.colorScheme) var colorScheme: ColorScheme
```

Example 3 (swift):
```swift
if colorScheme == .dark { // Checks the wrapped value.
    DarkContent()
} else {
    LightContent()
}
```

Example 4 (swift):
```swift
@Observable
class Library {
    var books: [Book] = [Book(), Book(), Book()]

    var availableBooksCount: Int {
        books.filter(\.isAvailable).count
    }
}

@main
struct BookReaderApp: App {
    @State private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(library)
        }
    }
}
```

---

## State

**URL:** https://sosumi.ai/documentation/swiftui/state?.md

**Contents:**
- Overview
  - Share state with subviews
  - Store observable objects
  - Share observable state objects with subviews
- Conforms To
- Creating a state
- Getting the value
- Creating and sharing view state

---
title: State
description: A property wrapper type that can read and write a value managed by SwiftUI.
source: https://developer.apple.com/documentation/swiftui/state
timestamp: 2026-02-13T19:35:32.747Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A property wrapper type that can read and write a value managed by SwiftUI.

Use state as the single source of truth for a given value type that you store in a view hierarchy. Create a state value in an [App](/documentation/swiftui/app), [Scene](/documentation/swiftui/scene), or [View](/documentation/swiftui/view) by applying the `@State` attribute to a property declaration and providing an initial value. Declare state as private to prevent setting it in a memberwise initializer, which can conflict with the storage management that SwiftUI provides:

SwiftUI manages the property’s storage. When the value changes, SwiftUI updates the parts of the view hierarchy that depend on the value. To access a state’s underlying value, you use its [wrapped Value](/documentation/swiftui/state/wrappedvalue) property. However, as a shortcut Swift enables you to access the wrapped value by referring directly to the state instance. The above example reads and writes the `isPlaying` state property’s wrapped value by referring to the property directly.

Declare state as private in the highest view in the view hierarchy that needs access to the value. Then share the state with any subviews that also need access, either directly for read-only access, or as a binding for read-write access. You can safely mutate state properties from any thread.

If you pass a state property to a subview, SwiftUI updates the subview any time the value changes in the container view, but the subview can’t modify the value. To enable the subview to modify the state’s stored value, pass a [Binding](/documentation/swiftui/binding) instead.

For example, you can remove the `isPlaying` state from the play button in the above example, and instead make the button take a binding:

Then you can define a player view that declares the state and creates a binding to the state. Get the binding to the state value by accessing the state’s [projected Value](/documentation/swiftui/state/projectedvalue), which you get by prefixing the property name with a dollar sign (`$`):

Like you do for a [State Object](/documentation/swiftui/stateobject), declare `State` as private to prevent setting it in a memberwise initializer, which can conflict with the storage management that SwiftUI provides. Unlike a state object, always initialize state by providing a default value in the state’s declaration, as in the above examples. Use state only for storage that’s local to a view and its subviews.

You can also store observable objects that you create with the [Observable()](/documentation/Observation/Observable()) macro in `State`; for example:

A `State` property always instantiates its default value when SwiftUI instantiates the view. For this reason, avoid side effects and performance-intensive work when initializing the default value. For example, if a view updates frequently, allocating a new default object each time the view initializes can become expensive. Instead, you can defer the creation of the object using the [task(priority:_:)](/documentation/swiftui/view/task(priority:_:)) modifier, which is called only once when the view first appears:

Delaying the creation of the observable state object ensures that unnecessary allocations of the object doesn’t happen each time SwiftUI initializes the view. Using the [task(priority:_:)](/documentation/swiftui/view/task(priority:_:)) modifier is also an effective way to defer any other kind of work required to create the initial state of the view, such as network calls or file access.

> [!NOTE]
> It’s possible to store an object that conforms to the [Observable Object](/documentation/Combine/ObservableObject) protocol in a `State` property. However the view will only update when the reference to the object changes, such as when setting the property with a reference to another object. The view will not update if any of the object’s published properties change. To track changes to both the reference and the object’s published properties, use [State Object](/documentation/swiftui/stateobject) instead of [State](/documentation/swiftui/state) when storing the object.

To share an [Observable](/documentation/Observation/Observable) object stored in `State` with a subview, pass the object reference to the subview. SwiftUI updates the subview anytime an observable property of the object changes, but only when the subview’s [body](/documentation/swiftui/view/body-8kl5o) reads the property. For example, in the following code `BookView` updates each time `title` changes but not when `isAvailable` changes:

`State` properties provide bindings to their value. When storing an object, you can get a [Binding](/documentation/swiftui/binding) to that object, specifically the reference to the object. This is useful when you need to change the reference stored in state in some other subview, such as setting the reference to `nil`:

However, passing a [Binding](/documentation/swiftui/binding) to an object stored in `State` isn’t necessary when you need to change properties of that object. For example, you can set the properties of the object to new values in a subview by passing the object reference instead of a binding to the reference:

If you need a binding to a specific property of the object, pass either the binding to the object and extract bindings to specific properties where needed, or pass the object reference and use the [Bindable](/documentation/swiftui/bindable) property wrapper to create bindings to specific properties. For example, in the following code `BookEditorView` wraps `book` with `@Bindable`. Then the view uses the `$` syntax to pass to a [Text Field](/documentation/swiftui/textfield) a binding to `title`:

- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(wrappedValue:)](/documentation/swiftui/state/init(wrappedvalue:)) Creates a state property that stores an initial wrapped value.
- [init(initialValue:)](/documentation/swiftui/state/init(initialvalue:)) Creates a state property that stores an initial value.
- [init()](/documentation/swiftui/state/init()) Creates a state property without an initial value.

- [wrappedValue](/documentation/swiftui/state/wrappedvalue) The underlying value referenced by the state variable.
- [projectedValue](/documentation/swiftui/state/projectedvalue) A binding to the state value.

- [Managing user interface state](/documentation/swiftui/managing-user-interface-state)
- [Bindable](/documentation/swiftui/bindable)
- [Binding](/documentation/swiftui/binding)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper struct State<Value>
```

Example 2 (swift):
```swift
struct PlayButton: View {
    @State private var isPlaying: Bool = false // Create the state.

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") { // Read the state.
            isPlaying.toggle() // Write the state.
        }
    }
}
```

Example 3 (swift):
```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool // Play button now receives a binding.

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

Example 4 (swift):
```swift
struct PlayerView: View {
    @State private var isPlaying: Bool = false // Create the state here now.

    var body: some View {
        VStack {
            PlayButton(isPlaying: $isPlaying) // Pass a binding.

            // ...
        }
    }
}
```

---

## EnvironmentObject

**URL:** https://sosumi.ai/documentation/swiftui/environmentobject?.md

**Contents:**
- Overview
- Conforms To
- Creating an environment object
- Getting the value
- Distributing model data throughout your app

---
title: EnvironmentObject
description: A property wrapper type for an observable object that a parent or ancestor view supplies.
source: https://developer.apple.com/documentation/swiftui/environmentobject
timestamp: 2026-02-13T19:35:41.200Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A property wrapper type for an observable object that a parent or ancestor view supplies.

An environment object invalidates the current view whenever the observable object that conforms to [Observable Object](/documentation/Combine/ObservableObject) changes. If you declare a property as an environment object, be sure to set a corresponding model object on an ancestor view by calling its [environmentObject(_:)](/documentation/swiftui/view/environmentobject(_:)) modifier.

> [!NOTE]
> If your observable object conforms to the [Observable](/documentation/Observation/Observable) protocol, use [Environment](/documentation/swiftui/environment) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [environment(_:)](/documentation/swiftui/view/environment(_:)) or [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifiers.

- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init()](/documentation/swiftui/environmentobject/init()) Creates an environment object.

- [wrappedValue](/documentation/swiftui/environmentobject/wrappedvalue) The underlying value referenced by the environment object.
- [projectedValue](/documentation/swiftui/environmentobject/projectedvalue) A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [EnvironmentObject.Wrapper](/documentation/swiftui/environmentobject/wrapper) A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

- [environmentObject(_:)](/documentation/swiftui/view/environmentobject(_:))
- [environmentObject(_:)](/documentation/swiftui/scene/environmentobject(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject
```

---
