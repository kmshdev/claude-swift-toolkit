import SwiftUI

// MARK: - Liquid Glass Component Template
// Replace __GlassComponent__ with your component name
// Requires: iOS 26+ / macOS 26+ (Tahoe) / Xcode 26+

struct __GlassComponent__: View {
    // MARK: - Configuration
    let items: [GlassItem]
    @Binding var selectedID: GlassItem.ID?

    // MARK: - Animation Namespace
    @Namespace private var namespace

    // MARK: - State
    @State private var isExpanded = true

    // MARK: - Body
    var body: some View {
        // GlassEffectContainer combines glass shapes for:
        // 1. Better rendering performance
        // 2. Morph animations between shapes
        GlassEffectContainer(spacing: 12) {
            VStack(spacing: 12) {
                if isExpanded {
                    ForEach(items) { item in
                        GlassItemView(item: item, isSelected: item.id == selectedID)
                            // Apply Liquid Glass material
                            .glassEffect(
                                .regular.interactive(),
                                in: .rect(cornerRadius: 12)
                            )
                            // Identity for morph transitions
                            .glassEffectID(item.id, in: namespace)
                            .onTapGesture { selectedID = item.id }
                    }
                }

                // Toggle button with glass style
                Button {
                    withAnimation(.spring(response: 0.4, dampingFraction: 0.8)) {
                        isExpanded.toggle()
                    }
                } label: {
                    Label(
                        isExpanded ? "Collapse" : "Expand",
                        systemImage: isExpanded ? "chevron.up" : "chevron.down"
                    )
                    .font(.caption)
                    .frame(width: 100, height: 32)
                }
                .buttonStyle(.glass)
                .glassEffectID("toggle", in: namespace)
            }
        }
    }
}

// MARK: - Glass Item View

private struct GlassItemView: View {
    let item: GlassItem
    let isSelected: Bool

    var body: some View {
        HStack(spacing: 10) {
            Image(systemName: item.icon)
                .font(.title3)
                .foregroundStyle(isSelected ? .primary : .secondary)
                .frame(width: 28, height: 28)

            Text(item.title)
                .font(.subheadline.weight(.medium))
                .foregroundStyle(isSelected ? .primary : .secondary)

            Spacer()

            if isSelected {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundStyle(.green)
                    .transition(.scale.combined(with: .opacity))
            }
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 10)
        .contentShape(Rectangle())
        .accessibilityElement(children: .combine)
        .accessibilityLabel(item.title)
        .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}

// MARK: - Model

struct GlassItem: Identifiable, Hashable {
    let id: String
    let title: String
    let icon: String
}

// MARK: - Background Extension Effect Example
// Use on hero images in NavigationSplitView to extend under sidebar/inspector

struct HeroImageWithExtension: View {
    let imageName: String

    var body: some View {
        Image(imageName)
            .resizable()
            .aspectRatio(contentMode: .fill)
            .frame(maxWidth: .infinity)
            .frame(height: 300)
            .clipped()
            // Extends and blurs the image under sidebar/inspector
            .backgroundExtensionEffect()
            // Overlay content AFTER the extension modifier
            // so overlays don't extend under the sidebar
            .overlay(alignment: .bottomLeading) {
                Text("Featured")
                    .font(.largeTitle.bold())
                    .foregroundStyle(.white)
                    .padding()
            }
    }
}

// MARK: - Toolbar Grouping Example
// Use ToolbarSpacer(.fixed) to create separate glass backgrounds

struct ToolbarGroupingExample: View {
    var body: some View {
        Text("Content")
            .toolbar {
                // Group 1: Share
                ToolbarItem {
                    ShareLink(item: URL(string: "https://example.com")!)
                }

                // Fixed spacer creates visual separation with separate glass backgrounds
                ToolbarSpacer(.fixed)

                // Group 2: Actions
                ToolbarItemGroup {
                    Button("Favorite", systemImage: "heart") { }
                    Button("Bookmark", systemImage: "bookmark") { }
                }

                // Another group separation
                ToolbarSpacer(.fixed)

                // Group 3: Info
                ToolbarItem {
                    Button("Info", systemImage: "info.circle") { }
                }
            }
    }
}

// MARK: - Preview

#Preview {
    __GlassComponent__(
        items: [
            GlassItem(id: "1", title: "Design", icon: "paintbrush.fill"),
            GlassItem(id: "2", title: "Develop", icon: "hammer.fill"),
            GlassItem(id: "3", title: "Deploy", icon: "shippingbox.fill"),
        ],
        selectedID: .constant("1")
    )
    .padding()
    .preferredColorScheme(.dark)
}
