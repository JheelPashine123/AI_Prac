from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        print((x, y))
        visited.add((x, y))

        if x == target or y == target:
            print("Target reached")
            return

        # Fill jugs
        queue.append((jug1, y))
        queue.append((x, jug2))

        # Empty jugs
        queue.append((0, y))
        queue.append((x, 0))

        # Pour jug1 -> jug2
        transfer = min(x, jug2 - y)
        queue.append((x - transfer, y + transfer))

        # Pour jug2 -> jug1
        transfer = min(y, jug1 - x)
        queue.append((x + transfer, y - transfer))

water_jug(4, 3, 2)


# Explanation:
# Each state is represented as (x, y) where x and y are water levels.
# We use BFS to explore all possible states.
# Operations: fill, empty, and transfer water.
# We stop when the target amount is reached.