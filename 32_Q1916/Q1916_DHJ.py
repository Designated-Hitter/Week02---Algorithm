import sys
from sys import maxsize
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [maxsize] * (N + 1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

target_start, target_end = map(int, input().split())


def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd

dijkstra(target_start)
print(visited[target_end])