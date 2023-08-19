N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnts = 0
vis = [False] * (N + 1)

# 방문 안한 정점만을 돌면서 연결요소에 추가
for i in range(1, N + 1):
    if vis[i]: # 방문했으면 패스
        continue

    # 방문 안했으면 cnts에 추가하고 해당 영역 bfs로 돌면서 다 vis를 True로 만들어주기
    cnts += 1

    q = []
    vis[i] = True
    q.append(i)

    while q:
        cur = q.pop()

        for nxt in graph[cur]:
            if vis[nxt]:
                continue

            vis[nxt] = True
            q.append(nxt)

print(cnts)    