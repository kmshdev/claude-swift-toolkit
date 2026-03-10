# Actor Patterns Reference

## When to Use Actors vs Other Isolation

| Pattern | Use When |
|---------|----------|
| `@MainActor` class | View model, UI state, anything read by SwiftUI views |
| Custom `actor` | Shared mutable resource (cache, connection pool, rate limiter) |
| `nonisolated` func | Pure computation, no shared state access |
| `Sendable` struct | Immutable data crossing isolation boundaries |
| `@unchecked Sendable` | Legacy type you've manually verified is thread-safe (document why) |

## Actor Best Practices

1. **Keep actors small** — one responsibility per actor
2. **Minimize suspension points** — fewer `await` calls inside actor methods reduces reentrancy risk
3. **Don't hold locks across await** — this causes deadlocks. Use actors instead of locks
4. **Batch operations** — instead of calling an actor method in a loop, pass the batch in one call
5. **Test reentrancy** — write tests that exercise concurrent access to verify invariants hold
