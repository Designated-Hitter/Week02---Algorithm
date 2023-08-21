import heapq
"""
반례
4
0011
0000
0000
0100
실행 결과 : 1 4 2 3
정답 : 1 3 4 2
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
            graph[i + 1].append(j + 1)
            indegree[j + 1] += 1
    
hq = []

for i in range(1, N + 1):
    if indegree[i] == 0: # indeg 없으면 넣기
        heapq.heappush(hq, i)
num = 1

while hq:
    cur = heapq.heappop(hq)
    new_num[cur] = num
    num += 1
    
    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            heapq.heappush(hq, nxt)

if new_num.count(0) > 1:
    print(-1)
else:
    for n in new_num[1:]:
        print(n, end= ' ')
