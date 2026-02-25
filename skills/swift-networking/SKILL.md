---
name: swift-networking
description: Build, test, or review networking code using URLSession with async/await. Use when adding API calls, implementing authentication, handling errors from remote services, or reviewing network layer code for correctness and resilience.
---

# Swift Networking

## Lifecycle Position

Phase 3 (Implement). Load when building features that call external APIs or persist remote data.

## Workflow Decision Tree

### 1) Build a REST API client
- Define a protocol-based API client (see `references/networking-patterns.md`)
- Use `URLSession.shared.data(for:)` for standard requests
- Decode responses with `JSONDecoder` configured for the API's conventions
- Handle errors at every layer: network → HTTP status → decode → domain

### 2) Download files
- Use `URLSession.shared.download(from:)` for large files
- Monitor progress with `AsyncBytes` or delegate
- Save to temporary directory, then move to final location

### 3) WebSocket communication
- Use `URLSession.webSocketTask(with:)` for real-time connections
- Handle `.ping`/`.pong` for keepalive
- Reconnect with exponential backoff on disconnect

### 4) Background transfers
- Create dedicated `URLSessionConfiguration.background(withIdentifier:)`
- Handle `application(_:handleEventsForBackgroundURLSession:completionHandler:)`
- Background transfers survive app termination

## Core APIs

### URLSession async/await
```swift
// GET request
let (data, response) = try await URLSession.shared.data(from: url)

// POST with body
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = try JSONEncoder().encode(payload)
let (data, response) = try await URLSession.shared.data(for: request)

// Download
let (localURL, response) = try await URLSession.shared.download(from: url)

// Stream bytes
let (bytes, response) = try await URLSession.shared.bytes(from: url)
for try await byte in bytes { /* process */ }
```

### JSON Decoding
```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601

let result = try decoder.decode(MyModel.self, from: data)
```

### Request Building
```swift
struct APIClient {
    let baseURL: URL
    let session: URLSession

    func request<T: Decodable>(_ endpoint: String, method: String = "GET", body: (any Encodable)? = nil) async throws -> T {
        var request = URLRequest(url: baseURL.appendingPathComponent(endpoint))
        request.httpMethod = method
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        if let body { request.httpBody = try JSONEncoder().encode(body) }

        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }
        guard (200...299).contains(http.statusCode) else {
            throw NetworkError.httpError(http.statusCode, data)
        }
        return try JSONDecoder().decode(T.self, from: data)
    }
}
```

## Error Handling Hierarchy

Handle errors from most specific to most general:

```swift
do {
    let user: User = try await api.request("/users/me")
} catch let error as NetworkError {
    switch error {
    case .noConnection:        // Show offline banner
    case .timeout:             // Suggest retry
    case .httpError(401, _):   // Redirect to login
    case .httpError(404, _):   // Show not found
    case .httpError(429, _):   // Rate limited — back off
    case .httpError(500..., _): // Server error — retry with backoff
    case .decodingFailed(let underlying): // Log, show generic error
    default: break
    }
} catch is CancellationError {
    // Task was cancelled — do nothing
} catch {
    // Unknown error — log and show generic message
}
```

## Retry with Exponential Backoff

```swift
func withRetry<T>(maxAttempts: Int = 3, operation: () async throws -> T) async throws -> T {
    for attempt in 0..<maxAttempts {
        do {
            return try await operation()
        } catch {
            if attempt == maxAttempts - 1 { throw error }
            let delay = UInt64(pow(2.0, Double(attempt))) * 1_000_000_000
            try await Task.sleep(nanoseconds: delay)
        }
    }
    fatalError("Unreachable")
}
```

## URLSessionConfiguration

| Configuration | Use Case |
|---------------|----------|
| `.default` | Standard requests with disk caching |
| `.ephemeral` | Sensitive data — no disk cache, no cookies persisted |
| `.background(withIdentifier:)` | Downloads/uploads that survive app termination |

Key properties:
- `timeoutIntervalForRequest` — per-request timeout (default 60s, set to 30s for APIs)
- `timeoutIntervalForResource` — total transfer timeout (default 7 days)
- `waitsForConnectivity` — wait for network instead of failing immediately (set `true` for background)
- `httpAdditionalHeaders` — default headers for all requests (auth tokens, User-Agent)

## Caching

```swift
// URL-level cache policy
var request = URLRequest(url: url)
request.cachePolicy = .returnCacheDataElseLoad  // Offline-first

// Session-level cache
let config = URLSessionConfiguration.default
config.urlCache = URLCache(memoryCapacity: 10_000_000, diskCapacity: 50_000_000)

// ETag-based validation (automatic with .default configuration)
// Server sends: ETag: "abc123"
// Client sends: If-None-Match: "abc123"
// Server returns 304 Not Modified if unchanged
```

## Common Mistakes

1. Force-unwrapping decoded data — always use `try` with proper error handling
2. Missing timeout configuration — default 60s is too long for mobile APIs. Set 15-30s
3. Not checking HTTP status code — `data(for:)` succeeds for 4xx/5xx responses. Always check `HTTPURLResponse.statusCode`
4. Ignoring `CancellationError` — `.task` modifier cancels on disappear; don't show error UI for cancellation
5. Building URLs with string concatenation — use `URL(string:relativeTo:)` or `URLComponents` to avoid encoding issues

## Checklist

- [ ] Timeouts configured (15-30s for API calls)
- [ ] HTTP status codes checked (not just decode success)
- [ ] ATS exceptions documented in Info.plist if needed
- [ ] Errors surfaced to user with actionable messages
- [ ] Cancellation handled gracefully (no error UI for `.task` cancellation)
- [ ] No force-unwrap of decoded data
- [ ] Authentication tokens not hardcoded (use Keychain or environment)
- [ ] Retry logic for transient failures (429, 5xx)

## Cross-References

- `swift-concurrency` — async/await patterns, Task cancellation, actor isolation for network state
- `swift-app-lifecycle` — background transfer configuration
- `ios-testing` — mocking URLSession with protocol-based DI
- `code-analyzer` — network error handling review section
