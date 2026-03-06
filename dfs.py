# DFS example — recursive graph traversal
# Practice: https://leetcode.com/problems/number-of-islands/
def dfs(graph, node, visited):
    print(node, end=' ')
    visited.add(node)
    for nei in graph.get(node, []):
        if nei not in visited:
            dfs(graph, nei, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
visited = set()
dfs(graph, 'A', visited)
