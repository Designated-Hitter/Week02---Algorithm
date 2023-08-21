import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
hq = []
dist = [-1] * (N + 1)
ans = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    indegree[u] += 1

st, en = map(int, input().split())

heapq.heappush(hq, (0, en, "")) # (거리, 위치, 경로)
paths = []
while hq:
    cur = heapq.heappop(hq)
    dst, cur_city, path = cur[0], cur[1], cur[2]

    if cur_city == st: # 도착했으면
        if dst == ans: # 같으면
            # 경로에 추가
            paths.append(path)   
        elif dst > ans: # 더 크면
            # 갱신
            ans = dst
            # paths.clear()
            paths.append(path)
        else: # 더 작으면 패스
            continue

    for nxt_city, tme in graph[cur_city]:
        if dist[nxt_city] < dst + tme: # 이 경로가 더 길면 간선 제거
            dist[nxt_city] = dst + tme
            indegree[nxt_city] -= 1

            if indegree[nxt_city] == 0:
                heapq.heappush(hq, (dist[nxt_city], nxt_city, path + str(cur_city) + str(nxt_city)))

print(ans, paths)


        
