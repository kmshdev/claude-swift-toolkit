# Neuralforge-Chat-Sidebar - Text Input

**Pages:** 5

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
timestamp: 2026-02-13T01:41:15.466Z
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

## keyboardShortcut(_:modifiers:)

**URL:** https://sosumi.ai/documentation/swiftui/view/keyboardshortcut(_:modifiers:)?.md

**Contents:**
- Discussion
- Creating keyboard shortcuts

---
title: keyboardShortcut(_:modifiers:)
description: Defines a keyboard shortcut and assigns it to the modified control.
source: https://developer.apple.com/documentation/swiftui/view/keyboardshortcut(_:modifiers:)
timestamp: 2026-02-13T01:42:57.657Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> Defines a keyboard shortcut and assigns it to the modified control.

Pressing the control’s shortcut while the control is anywhere in the frontmost window or scene, or anywhere in the macOS main menu, is equivalent to direct interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-first traversal of one or more view hierarchies. On macOS, the system looks in the key window first, then the main window, and then the command groups; on other platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one found is used.

The default localization configuration is set to [automatic](/documentation/swiftui/keyboardshortcut/localization-swift.struct/automatic).

- [keyboardShortcut(_:)](/documentation/swiftui/view/keyboardshortcut(_:))
- [keyboardShortcut(_:modifiers:localization:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:localization:))
- [keyboardShortcut](/documentation/swiftui/environmentvalues/keyboardshortcut)
- [KeyboardShortcut](/documentation/swiftui/keyboardshortcut)
- [KeyEquivalent](/documentation/swiftui/keyequivalent)
- [EventModifiers](/documentation/swiftui/eventmodifiers)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func keyboardShortcut(_ key: KeyEquivalent, modifiers: EventModifiers = .command) -> some View
```

---

## FocusState

**URL:** https://sosumi.ai/documentation/swiftui/focusstate?.md

**Contents:**
- Overview
  - Avoid ambiguous focus bindings
  - Nest focusable views
- Conforms To
- Creating a focus state
- Inspecting the focus state
- Managing focus state

---
title: FocusState
description: A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
source: https://developer.apple.com/documentation/swiftui/focusstate
timestamp: 2026-02-13T01:41:19.746Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.

Use this property wrapper in conjunction with [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) and [focused(_:)](/documentation/swiftui/view/focused(_:)) to describe views whose appearance and contents relate to the location of focus in the scene. When focus enters the modified view, the wrapped value of this property updates to match a given prototype value. Similarly, when focus leaves, the wrapped value of this property resets to `nil` or `false`. Setting the property’s value programmatically has the reverse effect, causing focus to move to the view associated with the updated value.

In the following example of a simple login screen, when the user presses the Sign In button and one of the fields is still empty, focus moves to that field. Otherwise, the sign-in process proceeds.

To allow for cases where focus is completely absent from a view tree, the wrapped value must be either an optional or a Boolean. Set the focus binding to `false` or `nil` as appropriate to remove focus from all bound fields. You can also use this to remove focus from a [Text Field](/documentation/swiftui/textfield) and thereby dismiss the keyboard.

The same view can have multiple focus bindings. In the following example, setting `focusedField` to either `name` or `fullName` causes the field to receive focus:

On the other hand, binding the same value to two views is ambiguous. In the following example, two separate fields bind focus to the `name` value:

If the user moves focus to either field, the `focusedField` binding updates to `name`. However, if the app programmatically sets the value to `name`, SwiftUI chooses the first candidate, which in this case is the “Name” field. SwiftUI also emits a runtime warning in this case, since the repeated binding is likely a programmer error.

It is important to consider the difference between [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) and [focused(_:)](/documentation/swiftui/view/focused(_:)) with nested focusable views.

For example, consider the following code:

The code above uses [focused(_:)](/documentation/swiftui/view/focused(_:)), which binds focus state to the given Boolean state value. [focused(_:)](/documentation/swiftui/view/focused(_:)) sets `containerIsFocused` to `true` both when the `VStack` itself receives focus and *just* the `TextField` that it contains receives focus. This behavior occurs because two independent instances of `@FocusState` are used to observe the focus state of the focusable `VStack` and the `TextField`. When the `VStack` does not have focus, SwiftUI checks the view hierarchy to find the closest view with focus to set the value for `containerIsFocused`. If the `TextField` contained within this `VStack` happens to be focused, [focused(_:)](/documentation/swiftui/view/focused(_:)) will set `containerIsFocused` to `true`.

If there is need to observe whether only the `VStack` has focus, but not the inner TextField, consider using [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) instead, for more granular control.

With [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)), the above code can be rewritten as follows:

With [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)), it is possible to define a custom data structure to represent focus state. In this case, a `Focus` enumeration is used. It has two cases, one for the focusable `VStack` and another for the `TextField` it contains. [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) binds focused to `.container` only when the `VStack` itself has focus, and to `.field` when the `TextField` has focus. Because now there is only one `@FocusState` property, SwiftUI is able to disambiguate between cases when `VStack` *contains* focus and *receives* focus itself.

Note that both of the above approaches are acceptable. [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)) can be used to observe whether the given view currently receives focus. While [focused(_:)](/documentation/swiftui/view/focused(_:)) can be used for the same purpose, additionally it can observe whether the given view contains focus.

- [DynamicProperty](/documentation/swiftui/dynamicproperty)

- [init()](/documentation/swiftui/focusstate/init()) Creates a focus state that binds to a Boolean.

- [projectedValue](/documentation/swiftui/focusstate/projectedvalue) A projection of the focus state value that returns a binding.
- [FocusState.Binding](/documentation/swiftui/focusstate/binding) A property wrapper type that can read and write a value that indicates the current focus location.
- [wrappedValue](/documentation/swiftui/focusstate/wrappedvalue) The current state value, taking into account whatever bindings might be in effect due to the current location of focus.

- [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:))
- [focused(_:)](/documentation/swiftui/view/focused(_:))
- [isFocused](/documentation/swiftui/environmentvalues/isfocused)
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
@frozen @propertyWrapper struct FocusState<Value> where Value : Hashable
```

Example 2 (swift):
```swift
struct LoginForm {
    enum Field: Hashable {
        case username
        case password
    }

    @State private var username = ""
    @State private var password = ""
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Username", text: $username)
                .focused($focusedField, equals: .username)

            SecureField("Password", text: $password)
                .focused($focusedField, equals: .password)

            Button("Sign In") {
                if username.isEmpty {
                    focusedField = .username
                } else if password.isEmpty {
                    focusedField = .password
                } else {
                    handleLogin(username, password)
                }
            }
        }
    }
}
```

Example 3 (swift):
```swift
struct ContentView: View {
    enum Field: Hashable {
        case name
        case fullName
    }
    @FocusState private var focusedField: Field?

    var body: some View {
        TextField("Full Name", ...)
            .focused($focusedField, equals: .name)
            .focused($focusedField, equals: .fullName)
    }
}
```

Example 4 (swift):
```swift
struct ContentView: View {
    enum Field: Hashable {
        case name
        case fullName
    }
    @FocusState private var focusedField: Field?

    var body: some View {
        TextField("Name", ...)
            .focused($focusedField, equals: .name)
        TextField("Full Name", ...)
            .focused($focusedField, equals: .name) // incorrect re-use of .name
    }
}
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
timestamp: 2026-02-13T01:41:17.650Z
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

## submitLabel(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/submitlabel(_:)?.md

**Contents:**
- Parameters
- Discussion
- Labeling a submission event

---
title: submitLabel(_:)
description: Sets the submit label for this view.
source: https://developer.apple.com/documentation/swiftui/view/submitlabel(_:)
timestamp: 2026-02-13T01:41:21.836Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the submit label for this view.

One of the cases specified in [Submit Label](/documentation/swiftui/submitlabel).

- [SubmitLabel](/documentation/swiftui/submitlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func submitLabel(_ submitLabel: SubmitLabel) -> some View
```

Example 2 (swift):
```swift
Form {
    TextField("Username", $viewModel.username)
        .submitLabel(.continue)
    SecureField("Password", $viewModel.password)
        .submitLabel(.done)
}
```

---
