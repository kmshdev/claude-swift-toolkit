import SwiftUI

// MARK: - Custom ViewModifier Template
// Replace __ModifierName__ with your modifier name

struct __ModifierName__: ViewModifier {
    // MARK: - Configuration
    var isEnabled: Bool = true
    var cornerRadius: CGFloat = 12
    var padding: CGFloat = 16

    // MARK: - Environment
    @Environment(\.colorScheme) private var colorScheme

    // MARK: - Body
    func body(content: Content) -> some View {
        if isEnabled {
            content
                .padding(padding)
                .background(backgroundColor, in: RoundedRectangle(cornerRadius: cornerRadius))
                .shadow(color: shadowColor, radius: 4, y: 2)
        } else {
            content
        }
    }

    // MARK: - Computed Styles
    private var backgroundColor: Color {
        colorScheme == .dark
            ? Color(.systemGray6)
            : Color(.systemBackground)
    }

    private var shadowColor: Color {
        colorScheme == .dark
            ? .clear
            : .black.opacity(0.08)
    }
}

// MARK: - View Extension (clean call site)

extension View {
    /// Applies __ModifierName__ styling to this view.
    ///
    /// - Parameters:
    ///   - isEnabled: Whether to apply the modifier. Defaults to `true`.
    ///   - cornerRadius: Corner radius of the background shape. Defaults to `12`.
    ///   - padding: Inner padding amount. Defaults to `16`.
    func __modifierName__(
        isEnabled: Bool = true,
        cornerRadius: CGFloat = 12,
        padding: CGFloat = 16
    ) -> some View {
        modifier(
            __ModifierName__(
                isEnabled: isEnabled,
                cornerRadius: cornerRadius,
                padding: padding
            )
        )
    }
}

// MARK: - Conditional Modifier Helper

extension View {
    /// Applies a modifier only when the condition is true.
    @ViewBuilder
    func `if`<Transform: View>(
        _ condition: Bool,
        transform: (Self) -> Transform
    ) -> some View {
        if condition {
            transform(self)
        } else {
            self
        }
    }
}

// MARK: - Preview

#Preview("Enabled") {
    Text("Hello, World!")
        .__modifierName__()
}

#Preview("Disabled") {
    Text("Hello, World!")
        .__modifierName__(isEnabled: false)
}
