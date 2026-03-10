import SwiftUI
import Observation

// MARK: - ViewModel Template
// Replace __ViewModel__ with your view model name
// Replace Item with your domain model type

@Observable
@MainActor
final class __ViewModel__ {
    // MARK: - Published State
    var items: [Item] = []
    var isLoading = false
    var errorMessage: String?

    // MARK: - Private State
    private var hasLoaded = false

    // MARK: - Dependencies (inject via init for testability)
    private let repository: ItemRepository

    // MARK: - Init
    init(repository: ItemRepository = .live) {
        self.repository = repository
    }

    // MARK: - Actions

    func load() async {
        guard !hasLoaded else { return }
        hasLoaded = true
        isLoading = true
        errorMessage = nil

        do {
            items = try await repository.fetchAll()
        } catch {
            errorMessage = error.localizedDescription
        }

        isLoading = false
    }

    func refresh() async {
        hasLoaded = false
        await load()
    }

    func delete(_ item: Item) async {
        do {
            try await repository.delete(item.id)
            items.removeAll { $0.id == item.id }
        } catch {
            errorMessage = error.localizedDescription
        }
    }
}

// MARK: - Repository Protocol (for testability)

protocol ItemRepository: Sendable {
    func fetchAll() async throws -> [Item]
    func delete(_ id: Item.ID) async throws
}

extension ItemRepository where Self == LiveItemRepository {
    static var live: LiveItemRepository { LiveItemRepository() }
}

struct LiveItemRepository: ItemRepository {
    func fetchAll() async throws -> [Item] {
        // Replace with real implementation
        []
    }

    func delete(_ id: Item.ID) async throws {
        // Replace with real implementation
    }
}

// MARK: - Mock for Previews and Tests

struct MockItemRepository: ItemRepository {
    var items: [Item] = []
    var shouldFail = false

    func fetchAll() async throws -> [Item] {
        if shouldFail { throw URLError(.badServerResponse) }
        return items
    }

    func delete(_ id: Item.ID) async throws {
        if shouldFail { throw URLError(.badServerResponse) }
    }
}
