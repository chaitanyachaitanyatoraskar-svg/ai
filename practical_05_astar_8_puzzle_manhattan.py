# ==============================================================================
# Practical 5 : Astar for 8 puzzle using Manhattan Distance.
# ==============================================================================

from heapq import heappush, heappop

goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def h(s):  # Manhattan Distance
    d = 0
    for i in range(3):
        for j in range(3):
            n = s[i][j]
            if n:
                x, y = divmod(n - 1, 3)
                d += abs(i - x) + abs(j - y)
    return d

def astar(start):
    pq = [(h(start), 0, start, [start])]
    seen = set()

    while pq:
        f, g, s, path = heappop(pq)
        if s == goal:
            for i, p in enumerate(path):
                print("Step", i)
                for r in p:
                    print(r)
                print()
            print("Total Distance =", g)
            return

        if s in seen:
            continue
        seen.add(s)

        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x = i
                    y = j

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                t = []
                for r in s:
                    t.append(list(r))
                t[x][y], t[nx][ny] = t[nx][ny], t[x][y]
                t = tuple(map(tuple, t))
                heappush(pq, (g + 1 + h(t), g + 1, t, path + [t]))

if __name__ == "__main__":
    start = ((1, 2, 3),
             (4, 0, 6),
             (7, 5, 8))

    astar(start)
