from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')


# Explanation:
# BFS visits nodes level by level.
# We use a queue (FIFO) to store nodes.
# First, we start from the given node.
# Then we visit its neighbors and add them to the queue.
# We keep track of visited nodes to avoid repetition.