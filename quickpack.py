# ============================
# ICPC Python QuickPack
# Ready to use in qualification contests
# ============================

import sys
import math
from collections import deque, Counter
import heapq

input = sys.stdin.readline
MOD = 10**9 + 7

# ============================
# BFS - Breadth First Search
# ============================
def bfs(start, graph):
    visited = set([start])
    q = deque([start])
    while q:
        u = q.popleft()
        # process node u here
        print(u, end=" ")
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

# ============================
# DFS - Depth First Search (recursive)
# ============================
def dfs(u, graph, visited):
    visited.add(u)
    # process node u here
    print(u, end=" ")
    for v in graph[u]:
        if v not in visited:
            dfs(v, graph, visited)

# ============================
# Dijkstra - Shortest Path
# graph = { node: [(neighbor, weight), ...] }
# ============================
def dijkstra(start, graph, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

# ============================
# Prefix Sums Helper
# ============================
def prefix_sum(arr):
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps  # sum of arr[l:r] = ps[r] - ps[l]

# ============================
# Greedy / Sorting Helper
# ============================
def sort_list(arr):
    arr.sort()
    return arr

# ============================
# Math Helpers
# ============================
def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // math.gcd(a, b)

def mod_mul(a, b, mod=MOD):
    return (a * b) % mod

def mod_add(a, b, mod=MOD):
    return (a + b) % mod

# ============================
# Fast I/O Example Template
# ============================
def read_int_list():
    return list(map(int, input().split()))

def read_int():
    return int(input())

def main():
    # Example usage of BFS
    graph = {0: [1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
    print("BFS traversal from node 0:")
    bfs(0, graph)
    print("\nDFS traversal from node 0:")
    visited = set()
    dfs(0, graph, visited)

    # Example Dijkstra
    wgraph = {0:[(1,4),(2,1)], 1:[(0,4),(3,1)], 2:[(0,1),(3,5)], 3:[(1,1),(2,5)]}
    dist = dijkstra(0, wgraph, 4)
    print("\nDijkstra distances from 0:", dist)

if __name__ == "__main__":
    main()
