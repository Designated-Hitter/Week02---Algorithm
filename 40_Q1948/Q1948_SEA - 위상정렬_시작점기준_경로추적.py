from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)
q = deque()
dist = [0] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    indegree[v] += 1

st, en = map(int, input().split())
paths = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append((i, 0))

while q:
    cur = q.popleft()
    
    if cur[1] != dist[cur[0]]:
        continue

    for nxt in graph[cur[0]]:
        # nxt 도시에 도착했고, 이제 기존 거리와 새롭게 갱신될 값을 비교함
        if dist[nxt[0]] < cur[1] + nxt[1]:
            dist[nxt[0]] = cur[1] + nxt[1] # 갱신되는게 더 크면 교체함
            
            paths[nxt[0]] = [cur[0]]
        
        elif dist[nxt[0]] == cur[1] + nxt[1]: # 같으면 
            paths[nxt[0]].append(cur[0])

        indegree[nxt[0]] -= 1

        if indegree[nxt[0]] == 0:
            q.append((nxt[0], dist[nxt[0]]))

q = deque([en])
route = set()

while q:
    now = q.popleft() # 7(end) -> 6(now) -> []
    for x in paths[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(dist[en])
print(len(route))
