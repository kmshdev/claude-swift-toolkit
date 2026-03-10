# Swiftui-Animations - Transactions

**Pages:** 6

---

## transaction(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transaction(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The transformation to apply to transactions within this view.

A view that wraps this view and applies a transformation to all transactions used within the view.

Use this modifier to change or replace the animation used in a view. Consider three identical animations controlled by a button that executes all three animations simultaneously:

The following code implements these animations:

Use this modifier on leaf views such as [Image](/documentation/swiftui/image) or [Button](/documentation/swiftui/button) rather than container views such as [VStack](/documentation/swiftui/vstack) or [HStack](/documentation/swiftui/hstack). The transformation applies to all child views within this view; calling `transaction(_:)` on a container view can lead to unbounded scope of execution depending on the depth of the view hierarchy.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
```

Example 2 (swift):
```swift
struct TransactionExample: View {
    @State private var flag = false

    var body: some View {
        VStack(spacing: 50) {
            HStack(spacing: 30) {
                Text("Rotation")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))

                Text("Rotation\nModified")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))
                    .transaction { view in
                        view.animation =
                            view.animation?.delay(2.0).speed(2)
                    }

                Text("Animation\nReplaced")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))
                    .transaction { view in
                        view.animation = .interactiveSpring(
                            response: 0.60,
                            dampingFraction: 0.20,
                            blendDuration: 0.25)
                    }
            }

            Button("Animate") {
                withAnimation(.easeIn(duration: 2.0)) {
                    self.flag.toggle()
                }
            }
        }
    }
}
```

---

## TransactionKey

**URL:** https://sosumi.ai/documentation/swiftui/transactionkey?.md

**Contents:**
- Overview
- Setting a default value
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

You can create custom transaction values by extending the [Transaction](/documentation/swiftui/transaction) structure with new properties. First declare a new transaction key type and specify a value for the required [default Value](/documentation/swiftui/transactionkey/defaultvalue) property:

The Swift compiler automatically infers the associated [Value](/documentation/swiftui/transactionkey/value) type as the type you specify for the default value. Then use the key to define a new transaction value property:

Clients of your transaction value never use the key directly. Instead, they use the key path of your custom transaction value property. To set the transaction value for a change, wrap that change in a call to `withTransaction`:

To use the value from inside `MyView` or one of its descendants, use the [transaction(*:)](/documentation/swiftui/view/transaction(*:)) view modifier:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol TransactionKey
```

Example 2 (swift):
```swift
private struct MyTransactionKey: TransactionKey {
    static let defaultValue = false
}
```

Example 3 (swift):
```swift
extension Transaction {
    var myCustomValue: Bool {
        get { self[MyTransactionKey.self] }
        set { self[MyTransactionKey.self] = newValue }
    }
}
```

Example 4 (swift):
```swift
withTransaction(\.myCustomValue, true) {
    isActive.toggle()
}
```

---

## withTransaction(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/withtransaction(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

A closure to execute.

The result of executing the closure with the specified transaction.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func withTransaction<Result>(_ transaction: Transaction, _ body: () throws -> Result) rethrows -> Result
```

---

## transaction(value:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transaction(value:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

A value to monitor for changes.

The transformation to apply to transactions within this view.

A view that wraps this view and applies a transformation to all transactions used within the view whenever `value` changes.

Use this modifier to change or replace the animation used in a view. Consider three identical views controlled by a button that changes all three simultaneously:

The following code implements these animations:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transaction(value: some Equatable, _ transform: @escaping (inout Transaction) -> Void) -> some View
```

Example 2 (swift):
```swift
struct TransactionExample: View {
    @State var flag = false

    var body: some View {
        VStack(spacing: 50) {
            HStack(spacing: 30) {
                Text("Rotation")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))

                Text("Rotation\nModified")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.animation =
                            t.animation?.delay(2.0).speed(2)
                    }

                Text("Animation\nReplaced")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.disableAnimations = true
                    }
            }

            Button("Animate") {
                withAnimation(.easeIn(duration: 2.0)) {
                    flag.toggle()
                }
            }
        }
    }
}
```

---

## Entry()

**URL:** https://sosumi.ai/documentation/swiftui/entry()?.md

**Contents:**
- Environment Values
- Transaction Values
- Container Values
- Focused Values
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

Create [Environment Values](/documentation/swiftui/environmentvalues) entries by extending the [Environment Values](/documentation/swiftui/environmentvalues) structure with new properties and attaching the @Entry macro to the variable declarations:

Create [Transaction](/documentation/swiftui/transaction) entries by extending the [Transaction](/documentation/swiftui/transaction) structure with new properties and attaching the @Entry macro to the variable declarations:

Create [Container Values](/documentation/swiftui/containervalues) entries by extending the [Container Values](/documentation/swiftui/containervalues) structure with new properties and attaching the @Entry macro to the variable declarations:

Since the default value for [Focused Values](/documentation/swiftui/focusedvalues) is always `nil`, [Focused Values](/documentation/swiftui/focusedvalues) entries cannot specify a different default value and must have an Optional type.

Create [Focused Values](/documentation/swiftui/focusedvalues) entries by extending the [Focused Values](/documentation/swiftui/focusedvalues) structure with new properties and attaching the @Entry macro to the variable declarations:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@attached(accessor) @attached(peer, names: prefixed(__Key_)) macro Entry()
```

Example 2 (swift):
```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
    @Entry var anotherCustomValue = true
}
```

Example 3 (swift):
```swift
extension Transaction {
    @Entry var myCustomValue: String = "Default value"
}
```

Example 4 (swift):
```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

---

## transaction(_:body:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transaction(_:body:)?.md

**Contents:**
- Discussion
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

Any modifiers applied to the content of `body` will be applied to this view, and the changes to the transaction performed in the `transform` will only affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation, while the contents of MyView are animated with the implicit transaction:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transaction<V>(_ transform: @escaping (inout Transaction) -> Void, @ViewBuilder body: (PlaceholderContentView<Self>) -> V) -> some View where V : View
```

Example 2 (swift):
```swift
MyView(isActive: isActive)
    .transaction { transaction in
        transaction.animation = transaction.animation?.speed(2)
    } body: { content in
        content.opacity(isActive ? 1.0 : 0.0)
    }
```

---
