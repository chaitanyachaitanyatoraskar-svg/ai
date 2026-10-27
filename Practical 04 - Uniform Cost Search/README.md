# Practical 4: Uniform Cost Search to find least-cost path between cities

## 📌 Problem Statement / Aim
Using a min-heap priority queue to determine the least-cost path across a weighted graph of cities.

## 💻 Source Code
File: [`uniform_cost_search.py`](./uniform_cost_search.py)

```python
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
    start = input("Enter start city: ")
    goal = input("Enter goal city: ")

    path, cost = ucs(graph, start, goal)

    print("Least-cost path:", " -> ".join(path))
    print("Total cost:", cost)
```

## 🖥️ How to Run
```bash
python3 uniform_cost_search.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:
Enter start city: A
Enter goal city: G
Least-cost path: A -> B -> D -> G
Total cost: 7
```
