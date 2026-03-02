---
name: ios-testing
description: This skill should be used when the user asks to "write tests", "add unit tests", "implement UI tests", "analyze test coverage", "use XCTest", "use Swift Testing", "test SwiftUI views", or needs iOS/macOS testing guidance. Provides testing strategies, XCTest and Swift Testing framework patterns, and SwiftUI-specific testing techniques.
allowed-tools: [Read, Grep, Glob, mcp__xcodebuildmcp__test_*]
---

# iOS/macOS Testing

## Lifecycle Position

Phase 6 (Test). After code is reviewed in Phase 5. Run tests via `/test` or XcodeBuildMCP `test_macos`/`test_sim`.

## Framework Choice

| Framework | When to Use |
|-----------|-------------|
| **Swift Testing** (`@Test`, `#expect`) | New test code. Preferred for modern projects. |
| **XCTest** (`XCTestCase`, `XCTAssert*`) | Legacy tests, UI tests, performance tests. |

Both frameworks can coexist in the same target.

## Swift Testing Framework

### Basic Test

```swift
import Testing
@testable import MyApp

@Suite("User Model Tests")
struct UserTests {
    @Test("Creating user with valid email succeeds")
    func createUserWithValidEmail() {
        let user = User(name: "Alice", email: "alice@example.com")
        #expect(user.name == "Alice")
        #expect(user.email == "alice@example.com")
    }

    @Test("Creating user with empty name throws")
    func createUserWithEmptyName() {
        #expect(throws: ValidationError.emptyName) {
            try User(name: "", email: "alice@example.com")
        }
    }
}
```

### Parameterized Tests

```swift
@Test("Email validation", arguments: [
    ("valid@test.com", true),
    ("no-at-sign", false),
    ("@no-local.com", false),
    ("user@.com", false),
])
func emailValidation(email: String, isValid: Bool) {
    #expect(Email.isValid(email) == isValid)
}
```

### Async Tests

```swift
@Test("Fetching items returns non-empty list")
func fetchItems() async throws {
    let service = ItemService(repository: MockRepository())
    let items = try await service.fetchAll()
    #expect(!items.isEmpty)
}
```

### Tags and Organization

```swift
extension Tag {
    @Tag static var networking: Self
    @Tag static var persistence: Self
}

@Test("API call succeeds", .tags(.networking))
func apiCall() async throws { ... }
```

## XCTest Patterns

### Basic XCTest

```swift
import XCTest
@testable import MyApp

final class UserServiceTests: XCTestCase {
    var sut: UserService!
    var mockRepository: MockUserRepository!

    override func setUp() {
        super.setUp()
        mockRepository = MockUserRepository()
        sut = UserService(repository: mockRepository)
    }

    override func tearDown() {
        sut = nil
        mockRepository = nil
        super.tearDown()
    }

    func testFetchUsersReturnsExpectedCount() async throws {
        mockRepository.stubbedUsers = [User.sample, User.sample2]
        let users = try await sut.fetchUsers()
        XCTAssertEqual(users.count, 2)
    }
}
```

### Async Expectations

```swift
func testPublisherEmitsValue() {
    let expectation = expectation(description: "Value received")
    let cancellable = viewModel.$items
        .dropFirst()
        .sink { items in
            XCTAssertFalse(items.isEmpty)
            expectation.fulfill()
        }
    viewModel.loadItems()
    wait(for: [expectation], timeout: 5.0)
    cancellable.cancel()
}
```

## Testing @Observable Models

```swift
@Test("ViewModel loads items on fetch")
func viewModelLoadsItems() async {
    let viewModel = ItemListViewModel(repository: MockRepository(items: Item.samples))
    await viewModel.fetch()
    #expect(viewModel.items.count == 3)
    #expect(viewModel.isLoading == false)
}
```

## Testing SwiftData Models

```swift
@Test("Inserting model persists correctly")
func insertModel() throws {
    let config = ModelConfiguration(isStoredInMemoryOnly: true)
    let container = try ModelContainer(for: Item.self, configurations: config)
    let context = container.mainContext

    let item = Item(title: "Test", createdAt: .now)
    context.insert(item)
    try context.save()

    let fetched = try context.fetch(FetchDescriptor<Item>())
    #expect(fetched.count == 1)
    #expect(fetched.first?.title == "Test")
}
```

### Testing Relationships and Cascading Deletes

```swift
@Test("Deleting parent cascades to children")
func cascadeDelete() throws {
    let config = ModelConfiguration(isStoredInMemoryOnly: true)
    let container = try ModelContainer(for: Folder.self, Document.self, configurations: config)
    let context = container.mainContext

    let folder = Folder(name: "Work")
    let doc = Document(title: "Notes", folder: folder)
    context.insert(folder)
    try context.save()

    context.delete(folder)
    try context.save()

    let docs = try context.fetch(FetchDescriptor<Document>())
    #expect(docs.isEmpty)
}
```

## Mocking with Protocols

```swift
protocol ItemRepository: Sendable {
    func fetchAll() async throws -> [Item]
    func save(_ item: Item) async throws
}

// Production
final class RemoteItemRepository: ItemRepository {
    func fetchAll() async throws -> [Item] { /* network call */ }
    func save(_ item: Item) async throws { /* network call */ }
}

// Test mock
final class MockItemRepository: ItemRepository {
    var stubbedItems: [Item] = []
    var savedItems: [Item] = []

    func fetchAll() async throws -> [Item] { stubbedItems }
    func save(_ item: Item) async throws { savedItems.append(item) }
}
```

## Test Structure — Arrange/Act/Assert

Every test follows three sections:

```swift
@Test("Item title updates correctly")
func updateTitle() {
    // Arrange
    let item = Item(title: "Old")

    // Act
    item.title = "New"

    // Assert
    #expect(item.title == "New")
}
```

## Test Naming

- **Swift Testing:** Use the display name string: `@Test("Descriptive behavior")`
- **XCTest:** Method name pattern: `test<Unit>_<Condition>_<ExpectedResult>()`
  - Example: `testUserService_EmptyEmail_ThrowsValidationError()`

## Checklist Before Submitting Tests

- [ ] Tests follow Arrange/Act/Assert
- [ ] Each test verifies one behavior
- [ ] Test names describe the expected behavior
- [ ] Mocks use protocol-based dependency injection
- [ ] No real network calls or file system access
- [ ] SwiftData tests use `isStoredInMemoryOnly: true`
- [ ] Async tests use `async throws` (Swift Testing) or expectations (XCTest)
- [ ] Edge cases covered: empty input, nil values, boundary conditions
- [ ] Tests are isolated — no shared mutable state between tests
- [ ] Critical paths have 80%+ coverage

## Templates

Test scaffolding in `templates/` — copy and adapt:

- **`ViewModelTestTemplate.swift`** — Swift Testing `@Suite` pattern with fresh state per test, parameterized `@Test`, async loading
- **`MockRepositoryTemplate.swift`** — Protocol-conforming mock with `@unchecked Sendable` for actor-safe testing
