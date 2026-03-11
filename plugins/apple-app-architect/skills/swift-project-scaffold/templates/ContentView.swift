import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "swift")
                .font(.system(size: 64))
                .foregroundStyle(.orange)
            Text("__APP_NAME__")
                .font(.largeTitle)
                .fontWeight(.bold)
            Text("Built with Swift 6.2")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding(40)
    }
}

#Preview {
    ContentView()
}
