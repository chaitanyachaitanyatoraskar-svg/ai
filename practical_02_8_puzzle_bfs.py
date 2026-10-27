# ==============================================================================
# Practical 2: BFS for 8-Puzzle Problem
# ==============================================================================

from collections import deque

# Function to generate possible moves
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # Position of the blank tile (0)
    # Possible moves: Up, Down, Left, Right
    moves = {
        'Up': -3,
        'Down': 3,
        'Left': -1,
        'Right': 1
    }
    for move, change in moves.items():
        new_index = index + change

        # Check valid moves
        if move == 'Up' and index < 3:
            continue
        if move == 'Down' and index > 5:
            continue
        if move == 'Left' and index % 3 == 0:
            continue
        if move == 'Right' and index % 3 == 2:
            continue

        new_state = list(state)
        new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
        neighbors.append((tuple(new_state), move))
    return neighbors

# BFS function
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        if current_state in visited:
            continue
        visited.add(current_state)
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [move]))
    return None

# Main Program
if __name__ == "__main__":
    start = (1, 2, 3,
             4, 5, 6,
             7, 0, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    solution = bfs(start, goal)
    if solution:
        print("Shortest Path:")
        print(" -> ".join(solution))
        print("Number of Moves:", len(solution))
    else:
        print("No solution found.")
