#prim 알고리즘
#visited 방문여부를 확인
#E_list 간선을 저장
#heap 현재 그래프에서 짧은 경로를 선택
#     현재 그래프에서 가장 짧은 간선을 골라 방문하지 않은 정점이라면 선택한다.
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False] * (V + 1)
E_list =[[] for _ in range(V+1)]
heap = [[0, 1]]

for _ in range(E):
    s, e, w = map(int, input().split())
    E_list[s].append([w, e])
    E_list[e].append([w, s])

answer = 0
count = 0

while heap:
    if count == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        count += 1

    for i in E_list[s]:
        heapq.heappush(heap, i)

print(answer)