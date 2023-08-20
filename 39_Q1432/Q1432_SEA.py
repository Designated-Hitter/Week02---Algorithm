import heapq
"""
틀린 코드와 다른 점은 간선의 방향을 반대로 설정한 것 + 최소힙 대신 최대힙 사용 이다.
저렇게 해야하는 이유
- indeg가 많을수록 늦게 번호가 매겨진다 -> 순열에서 가장 큰 숫자가 붙여진다.
- 그래서 가장 우선순위가 낮은 노드(큰 수가 번호로 매겨질 것들)를 최대힙에 넣어서, 노드번호가 크고, 가장 후순위 번호를 받을 것들부터 번호를 N부터 1씩 줄여가며 붙여준다. 
"""
N = int(input())
matrix = [input() for _ in range(N)]
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
new_num = [0] * (N + 1)

# 그래프 만들고 인접간선 리스트 만들기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1': # i에서 j로 가는 간선이 있음.
            graph[j + 1].append(i + 1)
            indegree[i + 1] += 1
    
hq = []

for i in range(1, N + 1):
    if indegree[i] == 0: # indeg 없으면 넣기
        heapq.heappush(hq, -i)
num = N

while hq:
    cur = -heapq.heappop(hq)
    new_num[cur] = num
    
    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            heapq.heappush(hq, -nxt)
    num -= 1

if new_num.count(0) > 1:
    print(-1)
else:
    for n in new_num[1:]:
        print(n, end= ' ')
