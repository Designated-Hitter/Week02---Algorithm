import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
visited = [sys.maxsize] * (V + 1)

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end)) #2차원 배열의 출발지 인덱스에 비용과 목적지를 표시

def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x)) #Priority Queue에 목적지와 비용(초기값은 0) push
    visited[x] = 0

    while pq:
            d, x = heapq.heappop(pq) #heappop으로 pq에서 꺼내고

            if visited[x] < d: #꺼낸 비용이 이미 다른 방법을 통해 측정한 비용보다 크다면 continue
                continue

            for nw, nx in graph[x]:
                nd = d + nw

                if visited[nx] > nd: #새로 측정한 비용이 지금까지 측정된 비용(maxsize or 이전에 측정한 비용)보다 작다면 새로 heappush
                    heapq.heappush(pq, (nd, nx))
                    visited[nx] = nd #비용도 새로 측정한 더 작은 비용으로 변경

dijkstra(K)

for i in range(1, len(visited)):
    if visited[i] == sys.maxsize:
        visited[i] = 'INF'
    
    print(visited[i])
