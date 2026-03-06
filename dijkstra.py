# Dijkstra — shortest path in weighted graph
# Practice: https://leetcode.com/problems/network-delay-time/
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, w in graph[node]:
            new_d = d + w
            if new_d < dist[nei]:
                dist[nei] = new_d
                heapq.heappush(pq, (new_d, nei))
    return dist

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3)],
    'E': [('C', 8), ('D', 3)]
}
print(dijkstra(graph, 'A'))
