N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (N + 1)

cnts = 0

# bfs로 풀이

q = []
q.append(1)
vis[1] = True

while q:
    cur = q.pop()

    for nxt in graph[cur]:
        if vis[nxt]:
            continue
        
        vis[nxt] = True
        cnts += 1
        q.append(nxt)

print(cnts)
