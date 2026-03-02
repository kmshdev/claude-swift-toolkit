import Testing
@testable import YourApp

// MARK: - Custom Tags

extension Tag {
    @Tag static var viewModel: Self
    @Tag static var repository: Self
    @Tag static var networking: Self
    @Tag static var validation: Self
}

// MARK: - Item ViewModel Tests

@Suite("ItemViewModel", .tags(.viewModel))
struct ItemViewModelTests {

    // MARK: - Properties

    let mockRepository: MockItemRepository
    let sut: ItemViewModel

    // MARK: - Initialization (runs before each test)

    init() {
        mockRepository = MockItemRepository()
        sut = ItemViewModel(repository: mockRepository)
    }

    // MARK: - Loading

    @Test("loads items successfully")
    func loadsItemsSuccessfully() async throws {
        mockRepository.stubbedItems = [
            Item(id: "1", title: "First"),
            Item(id: "2", title: "Second"),
            Item(id: "3", title: "Third")
        ]

        await sut.loadItems()

        #expect(sut.items.count == 3)
        #expect(sut.isLoading == false)
        #expect(sut.errorMessage == nil)
    }

    @Test("shows empty state when no items exist")
    func showsEmptyState() async {
        mockRepository.stubbedItems = []

        await sut.loadItems()

        #expect(sut.items.isEmpty)
        #expect(sut.showEmptyState == true)
    }

    @Test("sets loading state during fetch")
    func setsLoadingState() async {
        mockRepository.delay = .milliseconds(100)

        let loadTask = Task { await sut.loadItems() }

        // Allow the task to start
        try? await Task.sleep(for: .milliseconds(10))
        #expect(sut.isLoading == true)

        await loadTask.value
        #expect(sut.isLoading == false)
    }

    // MARK: - Error Handling

    @Test("handles repository failure")
    func handlesRepositoryFailure() async {
        mockRepository.shouldFail = true
        mockRepository.stubbedError = TestError.networkUnavailable

        await sut.loadItems()

        #expect(sut.state == .error)
        #expect(sut.errorMessage != nil)
        #expect(sut.items.isEmpty)
    }

    // MARK: - Parameterized Tests

    @Test("validates email format", arguments: [
        ("user@example.com", true),
        ("user@domain.co.uk", true),
        ("invalid-email", false),
        ("no@tld", false),
        ("@missing-local.com", false),
        ("user@.com", false)
    ])
    func validatesEmailFormat(email: String, isValid: Bool) {
        #expect(EmailValidator.isValid(email) == isValid)
    }

    @Test("filters items by category", arguments: [
        ItemCategory.active,
        ItemCategory.archived,
        ItemCategory.draft
    ])
    func filtersItemsByCategory(category: ItemCategory) async {
        mockRepository.stubbedItems = Item.sampleItems

        await sut.filterItems(by: category)

        let allMatchCategory = sut.items.allSatisfy { $0.category == category }
        #expect(allMatchCategory, "All displayed items should match the selected category")
    }

    // MARK: - Deletion

    @Test("deletes item and refreshes list")
    func deletesItem() async throws {
        let item = Item(id: "1", title: "To Delete")
        mockRepository.stubbedItems = [item]
        await sut.loadItems()

        await sut.deleteItem(item)

        #expect(mockRepository.deleteCallCount == 1)
        #expect(mockRepository.lastDeletedItemID == "1")
    }

    // MARK: - Optional Unwrapping

    @Test("unwraps selected item safely")
    func unwrapsSelectedItem() async throws {
        mockRepository.stubbedItems = [Item(id: "1", title: "First")]
        await sut.loadItems()

        sut.selectItem(at: 0)

        let selected = try #require(sut.selectedItem, "Expected an item to be selected")
        #expect(selected.id == "1")
    }
}
