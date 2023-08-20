from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
cnts = [[0] * (N + 1) for _ in range(N + 1)]

indegrees = [0] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    indegrees[u] += 1

q = deque()

# 들어오는 간선 없으면 큐에 추가
for i in range(1, N + 1):
    if indegrees[i] == 0:
        q.append(i)
        cnts[i][i] += 1

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        # cur의 cnts 값들을 더해준다.
        for i in range(1, N + 1):
            if cnts[i] != 0:
                cnts[nxt[0]][i] += cnts[cur][i] * nxt[1]
        
        # indeg를 1 줄인다
        indegrees[nxt[0]] -= 1

        # indeg가 0이면 q에 추가한다.
        if indegrees[nxt[0]] == 0:
            q.append(nxt[0])

for i in range(len(cnts[N])):
    if cnts[N][i] != 0:
        print(f"{i} {cnts[N][i]}")