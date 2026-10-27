# Practical 6: A* with straight line heuristic distance

## 📌 Problem Statement / Aim
Finding the optimal driving route from Arad to Bucharest on the Romania map using A* search guided by Straight-Line Distance heuristic.

## 💻 Source Code
File: [`astar_straight_line_heuristic.py`](./astar_straight_line_heuristic.py)

```python
# ==============================================================================
# Practical 6: A* with straight line heuristic distance
# ==============================================================================

from heapq import heappush, heappop

# Graph with road distances
graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101},
    'Bucharest': {}
}

# Straight Line Distance (Heuristic)
h = {
    'Arad': 366,
    'Sibiu': 253,
    'Fagaras': 176,
    'Rimnicu': 193,
    'Pitesti': 100,
    'Bucharest': 0,
    'Timisoara': 329,
    'Zerind': 374
}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]

    while pq:
        f, g, node, path = heappop(pq)

        if node == goal:
            return path, g

        for next_node, cost in graph.get(node, {}).items():
            new_g = g + cost
            new_f = new_g + h[next_node]
            heappush(pq, (new_f, new_g, next_node, path + [next_node]))

if __name__ == "__main__":
    path, distance = astar("Arad", "Bucharest")
    print("Path:", " -> ".join(path))
    print("Distance:", distance)
```

## 🖥️ How to Run
```bash
python3 astar_straight_line_heuristic.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:
Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Distance: 418
```
