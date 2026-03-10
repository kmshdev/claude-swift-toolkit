# Navigation Patterns

## Foundation: Type-Safe Navigation

```swift
enum Route: Hashable {
    case profile
    case settings
    case item(id: Int)
}

struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Profile", value: Route.profile)
                NavigationLink("Settings", value: Route.settings)
            }
            .navigationDestination(for: Route.self) { route in
                switch route {
                case .profile: ProfileView()
                case .settings: SettingsView()
                case .item(let id): ItemDetailView(id: id)
                }
            }
        }
    }
}
```

## Scalable Architecture: RouterPath

For apps with multiple tabs, deep links, and sheet routing, use an `@Observable` router class per tab:

```swift
@MainActor @Observable
final class RouterPath {
    var path: [Route] = []
    var presentedSheet: SheetDestination?

    func navigate(to route: Route) {
        path.append(route)
    }

    func reset() {
        path = []
    }
}
```

### Per-Tab Navigation Stacks

Each tab owns its own router and `NavigationStack`:

```swift
@MainActor
struct TimelineTab: View {
    @State private var routerPath = RouterPath()

    var body: some View {
        NavigationStack(path: $routerPath.path) {
            TimelineView()
                .withAppRouter()
        }
        .environment(routerPath)
    }
}
```

### Centralized Destination Mapping

Avoid duplicating route switches — use a shared modifier:

```swift
extension View {
    func withAppRouter() -> some View {
        navigationDestination(for: Route.self) { route in
            switch route {
            case .account(let id): AccountView(id: id)
            case .status(let id): StatusView(id: id)
            }
        }
    }
}
```

### TabRouter — Dynamic Per-Tab Routers

When tabs are data-driven, generate routers lazily:

```swift
@MainActor @Observable
final class TabRouter {
    private var routers: [AppTab: RouterPath] = [:]

    func router(for tab: AppTab) -> RouterPath {
        if let r = routers[tab] { return r }
        let r = RouterPath()
        routers[tab] = r
        return r
    }

    func binding(for tab: AppTab) -> Binding<[Route]> {
        let router = router(for: tab)
        return Binding(get: { router.path }, set: { router.path = $0 })
    }
}
```

Usage with `ForEach`:

```swift
TabView(selection: $selectedTab) {
    ForEach(AppTab.allCases) { tab in
        NavigationStack(path: tabRouter.binding(for: tab)) {
            tab.makeContentView()
                .withAppRouter()
        }
        .environment(tabRouter.router(for: tab))
        .tabItem { tab.label }
        .tag(tab)
    }
}
```

### Account Switch / Reset

Reset navigation state when app context changes:

```swift
func handleAccountSwitch() {
    for tab in AppTab.allCases {
        tabRouter.router(for: tab).reset()
    }
}
```

## Rules

- One `NavigationStack` per tab for independent history
- Use `navigationDestination(for:)` for type-safe routing (not `NavigationLink(destination:)`)
- `NavigationPath` for programmatic navigation; `RouterPath` for full-app routing
- Inject router via `.environment()` — child views navigate without prop-drilling
- Keep sheet state on the router for centralized modal management
- Store lightweight route data in the path, never view instances
- Reset path on account switch, logout, or major context changes
