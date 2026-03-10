---
name: ios-testing
description: This skill should be used when the user asks to "write tests", "add unit tests", "implement UI tests", "analyze test coverage", "use XCTest", "use Swift Testing", "test SwiftUI views", or needs iOS/macOS testing guidance. Provides testing strategies, XCTest and Swift Testing framework patterns, and SwiftUI-specific testing techniques.
allowed-tools: [Read, Grep, Glob, mcp__xcodebuildmcp__test_*]
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Evaluate if the testing task is complete. Check: 1) Were test files actually created or modified? 2) Were tests run and results reported? 3) Are there any failing tests that need attention? Context: $ARGUMENTS. Respond {\"ok\": true} if complete, or {\"ok\": false, \"reason\": \"what remains\"} if not."
          timeout: 30
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

### SwiftData Testing Safety

Swift Testing runs `@Suite` tests **in parallel by default**. This causes crashes with SwiftData:

**The Problem:** Multiple tests creating separate in-memory `ModelContainer` instances simultaneously leads to Core Data coordinator conflicts → `Fatal error: This model instance was destroyed by calling ModelContext.reset`.

**Two Safe Patterns:**

**Option 1 — Serialize the suite (recommended when tests share setup patterns):**
```swift
@MainActor
@Suite("MyModel Tests", .serialized)  // Forces sequential execution
struct MyModelTests {
    private func makeContainer() throws -> ModelContainer {
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        return try ModelContainer(for: MyModel.self, configurations: config)
    }

    @Test("insert persists")
    func insert() throws {
        let container = try makeContainer()
        let context = container.mainContext
        // container stays alive for the duration of this test
        // ...
    }
}
```

**Option 2 — Fresh container per test (safe without `.serialized`):**
```swift
@Test("insert persists")
func insert() throws {
    let config = ModelConfiguration(isStoredInMemoryOnly: true)
    let container = try ModelContainer(for: MyModel.self, configurations: config)
    let context = container.mainContext
    // container is local to this test — no cross-test interference
    // ...
}
```

**Critical Rule:** `ModelContainer` must outlive any `ModelContext` or `@Model` objects derived from it. If a helper function creates a container and returns only a context or a model object, the container is ARC-deallocated when the helper returns — and all model instances become invalid.

```swift
// WRONG — container dies when helper returns
func makeContext() throws -> ModelContext {
    let container = try ModelContainer(...)  // local → deallocated on return
    return container.mainContext  // orphaned context
}

// RIGHT — return the container (or have the owner retain it)
func makeContainer() throws -> ModelContainer {
    return try ModelContainer(for: MyModel.self,
        configurations: ModelConfiguration(isStoredInMemoryOnly: true))
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
- [ ] SwiftData test suites use `.serialized` or create fresh containers per `@Test`
- [ ] `ModelContainer` is retained for the lifetime of any `ModelContext` using it
- [ ] Async tests use `async throws` (Swift Testing) or expectations (XCTest)
- [ ] Edge cases covered: empty input, nil values, boundary conditions
- [ ] Tests are isolated — no shared mutable state between tests
- [ ] Critical paths have 80%+ coverage

## Templates

Test scaffolding in `templates/` — copy and adapt:

- **`ViewModelTestTemplate.swift`** — Swift Testing `@Suite` pattern with fresh state per test, parameterized `@Test`, async loading
- **`MockRepositoryTemplate.swift`** — Protocol-conforming mock with `@unchecked Sendable` for actor-safe testing
