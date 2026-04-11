# Networking Patterns Reference

## Protocol-Based API Client

The recommended pattern separates the transport layer from business logic for testability.

### 1. Define the Protocol

```swift
protocol APIClientProtocol: Sendable {
    func request<T: Decodable>(
        _ endpoint: String,
        method: HTTPMethod,
        body: (any Encodable)? ,
        headers: [String: String]
    ) async throws -> T
}

enum HTTPMethod: String, Sendable {
    case get = "GET", post = "POST", put = "PUT", patch = "PATCH", delete = "DELETE"
}
```

### 2. Implement the Client

```swift
actor APIClient: APIClientProtocol {
    private let baseURL: URL
    private let session: URLSession
    private let decoder: JSONDecoder

    init(baseURL: URL, session: URLSession = .shared) {
        self.baseURL = baseURL
        self.session = session
        self.decoder = JSONDecoder()
        self.decoder.keyDecodingStrategy = .convertFromSnakeCase
        self.decoder.dateDecodingStrategy = .iso8601
    }

    func request<T: Decodable>(
        _ endpoint: String,
        method: HTTPMethod = .get,
        body: (any Encodable)? = nil,
        headers: [String: String] = [:]
    ) async throws -> T {
        var urlRequest = URLRequest(url: baseURL.appendingPathComponent(endpoint))
        urlRequest.httpMethod = method.rawValue
        urlRequest.setValue("application/json", forHTTPHeaderField: "Content-Type")
        for (key, value) in headers {
            urlRequest.setValue(value, forHTTPHeaderField: key)
        }
        if let body {
            urlRequest.httpBody = try JSONEncoder().encode(body)
        }

        let (data, response) = try await session.data(for: urlRequest)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }

        guard (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.httpError(statusCode: httpResponse.statusCode, data: data)
        }

        do {
            return try decoder.decode(T.self, from: data)
        } catch {
            throw NetworkError.decodingFailed(error)
        }
    }
}
```

### 3. Define Errors

```swift
enum NetworkError: Error, LocalizedError {
    case invalidResponse
    case httpError(statusCode: Int, data: Data)
    case decodingFailed(Error)
    case noConnection
    case timeout

    var errorDescription: String? {
        switch self {
        case .invalidResponse: "Invalid server response"
        case .httpError(let code, _): "Server error (\(code))"
        case .decodingFailed: "Failed to process server response"
        case .noConnection: "No internet connection"
        case .timeout: "Request timed out"
        }
    }
}
```

### 4. Mock for Testing

```swift
final class MockAPIClient: APIClientProtocol, @unchecked Sendable {
    var mockResponses: [String: Any] = [:]
    var mockErrors: [String: Error] = [:]

    func request<T: Decodable>(
        _ endpoint: String,
        method: HTTPMethod = .get,
        body: (any Encodable)? = nil,
        headers: [String: String] = [:]
    ) async throws -> T {
        if let error = mockErrors[endpoint] { throw error }
        guard let response = mockResponses[endpoint] as? T else {
            throw NetworkError.invalidResponse
        }
        return response
    }
}
```

### 5. Usage in SwiftUI

```swift
@Observable @MainActor
class UserViewModel {
    private let api: any APIClientProtocol
    var user: User?
    var error: NetworkError?
    var isLoading = false

    init(api: any APIClientProtocol) { self.api = api }

    func loadUser() async {
        isLoading = true
        defer { isLoading = false }
        do {
            user = try await api.request("/users/me", method: .get)
        } catch let networkError as NetworkError {
            error = networkError
        } catch {
            error = nil // CancellationError or unexpected
        }
    }
}

struct UserView: View {
    @State private var viewModel: UserViewModel

    init(api: any APIClientProtocol) {
        _viewModel = State(initialValue: UserViewModel(api: api))
    }

    var body: some View {
        Group {
            if viewModel.isLoading {
                ProgressView()
            } else if let user = viewModel.user {
                Text(user.name)
            } else if let error = viewModel.error {
                ContentUnavailableView(error.localizedDescription, systemImage: "wifi.exclamationmark")
            }
        }
        .task { await viewModel.loadUser() }
    }
}
```
