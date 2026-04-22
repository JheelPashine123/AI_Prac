import heapq

def astar(graph, start, goal, h):
    open_list = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, node = heapq.heappop(open_list)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, weight in graph[node]:
            new_cost = cost[node] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + h[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = node

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 1, 'C': 1, 'D': 0}

print(astar(graph, 'A', 'D', h))


# Explanation:
# A* uses cost + heuristic to find shortest path.
# cost = actual distance from start
# heuristic = estimated distance to goal
# We use a priority queue to always pick best node.