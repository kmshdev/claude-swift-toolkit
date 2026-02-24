import SwiftUI

// MARK: - View Template
// Replace __ViewName__ with your view name
// Replace __ViewModel__ with your view model type

struct __ViewName__: View {
    // MARK: - Dependencies
    @Environment(\.dismiss) private var dismiss
    @State private var viewModel = __ViewModel__()

    // MARK: - State
    @State private var isLoading = false
    @State private var errorMessage: String?

    // MARK: - Body
    var body: some View {
        content
            .task { await viewModel.load() }
            .alert("Error", isPresented: .constant(errorMessage != nil)) {
                Button("OK") { errorMessage = nil }
            } message: {
                if let errorMessage { Text(errorMessage) }
            }
            .accessibilityElement(children: .contain)
    }

    // MARK: - Content
    @ViewBuilder
    private var content: some View {
        if viewModel.isLoading {
            ProgressView()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
        } else {
            ScrollView {
                LazyVStack(alignment: .leading, spacing: 16) {
                    // Your content here
                    ForEach(viewModel.items) { item in
                        ItemRow(item: item)
                    }
                }
                .padding()
            }
        }
    }
}

// MARK: - Subviews (extract when >20 lines)

private struct ItemRow: View {
    let item: Item

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: item.icon)
                .font(.title3)
                .foregroundStyle(.secondary)
                .frame(width: 32, height: 32)
                .accessibilityHidden(true)

            VStack(alignment: .leading, spacing: 2) {
                Text(item.title)
                    .font(.body)
                    .foregroundStyle(.primary)

                Text(item.subtitle)
                    .font(.caption)
                    .foregroundStyle(.tertiary)
            }

            Spacer()
        }
        .padding(.vertical, 4)
        .contentShape(Rectangle())
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(item.title), \(item.subtitle)")
    }
}

// MARK: - Preview

#Preview {
    __ViewName__()
}
