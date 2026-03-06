# BFS example — shortest path in unweighted graph
# Practice: https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([(start, 0)])
    while q:
        node, dist = q.popleft()
        print(node, "distance =", dist)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
bfs(graph, 'A')
