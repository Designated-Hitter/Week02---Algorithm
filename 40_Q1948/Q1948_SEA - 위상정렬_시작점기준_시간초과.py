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

q.append((st, 0))

while q:
    cur = q.popleft()
    node, dst = cur[0], cur[1]

    if dst != dist[node]:
        continue

    for nxt in graph[node]:
        # nxt 도시에 도착했고, 이제 기존 거리와 새롭게 갱신될 값을 비교함
        if dist[nxt[0]] < dst + nxt[1]:
            dist[nxt[0]] = dst + nxt[1] # 갱신되는게 더 크면 교체함
            
            paths[nxt[0]] = [(node, nxt[0])] + paths[node]
        
        elif dist[nxt[0]] == dst + nxt[1]: # 같으면 
            # 우선 cur -> nxt 넣고
            paths[nxt[0]].append((node, nxt[0]))
            # 기존에 없는거만 넣기
            for nd in paths[node]:
                if nd not in paths[nxt[0]]:
                    paths[nxt[0]].append(nd)

        indegree[nxt[0]] -= 1

        if indegree[nxt[0]] == 0:
            q.append((nxt[0], dist[nxt[0]]))

print(dist[en])
print(len(paths[en]))
