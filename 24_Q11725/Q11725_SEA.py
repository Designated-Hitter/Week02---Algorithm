N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = []
q.append(1)

while q:
    cur = q.pop()

    for nxt in graph[cur]:
        if parents[cur] == nxt:
            continue
        parents[nxt] = cur
        q.append(nxt)

for i in range(2, N + 1):
    print(parents[i])