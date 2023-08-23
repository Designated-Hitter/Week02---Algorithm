
"""
기본부품과 중간부품을 방향 있는 그래프로 만들어서 위상정렬을 사용해서 필요한 기본부품 개수를 갱신해주면 된다.
10분
"""
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
q = deque()
cnts = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))
    indegree[u] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        cnts[i][i] = 1

while q:
    cur = q.pop()

    for nxt, weight in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)
        
        for i in range(1, len(cnts[nxt])):
            cnts[nxt][i] += cnts[cur][i] * weight

for i in range(len(cnts[N])):
    if cnts[N][i] != 0:
        print(f"{i} {cnts[N][i]}")
        