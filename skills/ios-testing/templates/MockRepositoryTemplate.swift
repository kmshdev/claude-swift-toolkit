import Foundation
@testable import YourApp

// MARK: - Protocol

/// Protocol defining repository operations.
/// Both the real implementation and mock conform to this.
protocol ItemRepositoryProtocol: Sendable {
    func fetchItems() async throws -> [Item]
    func fetchItem(id: String) async throws -> Item?
    func saveItem(_ item: Item) async throws
    func deleteItem(id: String) async throws
}

// MARK: - Mock Implementation

/// A mock repository for testing.
///
/// Features:
/// - Stubbed return values for all methods
/// - Call counting for verification
/// - Argument capture for assertion
/// - Configurable failure injection
/// - Optional artificial delay for testing loading states
final class MockItemRepository: ItemRepositoryProtocol, @unchecked Sendable {

    // MARK: - Stubbed Values

    /// Items returned by `fetchItems()`.
    var stubbedItems: [Item] = []

    /// Item returned by `fetchItem(id:)`. Defaults to looking up `stubbedItems` by ID.
    var stubbedItemByID: [String: Item] = [:]

    /// Error thrown when `shouldFail` is `true`.
    var stubbedError: Error = TestError.mockFailure

    // MARK: - Configuration

    /// When `true`, all methods throw `stubbedError`.
    var shouldFail = false

    /// Optional delay before returning results (for testing loading states).
    var delay: Duration?

    // MARK: - Call Tracking: fetchItems

    private(set) var fetchItemsCallCount = 0

    func fetchItems() async throws -> [Item] {
        fetchItemsCallCount += 1
        if let delay { try? await Task.sleep(for: delay) }
        if shouldFail { throw stubbedError }
        return stubbedItems
    }

    // MARK: - Call Tracking: fetchItem

    private(set) var fetchItemCallCount = 0
    private(set) var lastFetchedItemID: String?

    func fetchItem(id: String) async throws -> Item? {
        fetchItemCallCount += 1
        lastFetchedItemID = id
        if shouldFail { throw stubbedError }
        return stubbedItemByID[id] ?? stubbedItems.first { $0.id == id }
    }

    // MARK: - Call Tracking: saveItem

    private(set) var saveCallCount = 0
    private(set) var savedItems: [Item] = []

    func saveItem(_ item: Item) async throws {
        saveCallCount += 1
        savedItems.append(item)
        if shouldFail { throw stubbedError }
    }

    // MARK: - Call Tracking: deleteItem

    private(set) var deleteCallCount = 0
    private(set) var lastDeletedItemID: String?

    func deleteItem(id: String) async throws {
        deleteCallCount += 1
        lastDeletedItemID = id
        if shouldFail { throw stubbedError }
        stubbedItems.removeAll { $0.id == id }
    }

    // MARK: - Reset

    /// Reset all call counts and captured arguments. Useful between tests if sharing a mock.
    func reset() {
        fetchItemsCallCount = 0
        fetchItemCallCount = 0
        lastFetchedItemID = nil
        saveCallCount = 0
        savedItems = []
        deleteCallCount = 0
        lastDeletedItemID = nil
        shouldFail = false
    }
}

// MARK: - Test Errors

/// Common errors used in test mocks.
enum TestError: LocalizedError, Equatable {
    case mockFailure
    case networkUnavailable
    case unauthorized
    case notFound
    case timeout

    var errorDescription: String? {
        switch self {
        case .mockFailure: return "Mock failure for testing"
        case .networkUnavailable: return "Network is unavailable"
        case .unauthorized: return "Unauthorized access"
        case .notFound: return "Resource not found"
        case .timeout: return "Request timed out"
        }
    }
}
