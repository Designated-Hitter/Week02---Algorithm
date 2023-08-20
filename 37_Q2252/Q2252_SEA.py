from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
topol = []
indegrees = [0] * (N + 1)
q = deque()

# 그래프 그리고 인접간선 개수 추가
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegrees[v] += 1

# 인접간선 개수 0인거를 큐에 넣고 돌리기
for i in range(1, N + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    # 꺼내서 토폴에 넣기
    cur = q.popleft()
    topol.append(cur)

    # 이 정점의 나가는 간선이 만나는 정점의 indegree 1만큼 줄이기
    for nxt in graph[cur]:
        indegrees[nxt] -= 1

        # 인접간선 0 되었으면 큐에 넣기
        if indegrees[nxt] == 0:
            q.append(nxt)

for n in topol:
    print(n, end = ' ')
