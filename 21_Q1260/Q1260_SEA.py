N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

vis = [False] * (N + 1)

def dfs(node):
    vis[node] = True
    print(node, end= ' ')

    for nxt in graph[node]:
        if not vis[nxt]: # 방문 안했으면
            dfs(nxt)

def bfs(node):
    q = []
    q.append(node)
    vis[node] = True

    while q:
        cur = q.pop(0)
        print(cur, end = ' ')

        for nxt in graph[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                q.append(nxt)



dfs(V)
print()

for i in range(N + 1):
    vis[i] = False
vis[V] = True

bfs(V)

    