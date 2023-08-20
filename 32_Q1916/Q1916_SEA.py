import sys, heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

st_pos, en_pos = map(int, input().split())
dist = [sys.maxsize] * (N + 1)
dist[st_pos] = 0
hq = []
"""
테케: 출발지 = 1, 도착지 = 5
일단 거리를 담는 배열 dist를 만든다. 이후 힙에 (거리, 위치)를 넣는다.
이후 하나씩 빼서 기존 거리와 새롭게 확인하는 거리를 비교해서 더 작을 때만 갱신해주고 다시 넣어주는 거를 하면 된다.
힙에서 뺄 때 나오는건 거리가 제일 작은거다.
"""

heapq.heappush(hq, (0, st_pos))

while hq:
    cur = heapq.heappop(hq)
    
    if cur[0] != dist[cur[1]]:
        continue

    for nxt in graph[cur[1]]:
        if dist[nxt[0]] > cur[0] + nxt[1]:
            dist[nxt[0]] = cur[0] + nxt[1]
            heapq.heappush(hq, (dist[nxt[0]], nxt[0]))

print(dist[en_pos])