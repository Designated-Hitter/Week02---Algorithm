from collections import deque
import sys
input = sys.stdin.readline


n, m, v = map(int, input().split())


graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    node_1, node_2 = map(int, input().split())
    graph[node_1][node_2] = graph[node_2][node_1] = 1

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        start = queue.popleft()
        print(start, end= ' ')
        for i in range(1, n+1):
            if not visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)