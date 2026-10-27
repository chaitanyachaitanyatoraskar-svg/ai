# ==============================================================================
# Practical 4: Uniform Cost Search to find least-cost path between cities
# ==============================================================================

import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

# Weighted graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}

if __name__ == "__main__":
    start = input("Enter start city: ").strip()
    goal = input("Enter goal city: ").strip()

    path, cost = ucs(graph, start, goal)

    print("Least-cost path:", " -> ".join(path))
    print("Total cost:", cost)
