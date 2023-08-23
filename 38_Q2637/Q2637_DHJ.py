import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N + 1) #모든 노드에 대한 진입차수는 0으로 초기화

graph =[[] for _ in range(N + 1)]
count = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    X, Y, K = map(int, input().split()) #완성품, 재료, 필요 수량
    graph[Y].append((X, K)) #graph[완성품] 에 재료와 필요 수량을 append
    indegree[X] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        count[i][i] += 1

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if count[i] != 0:
            count[nxt[0]][i] += count[now][i] * nxt[1]

        indegree[nxt[0]] -= 1

        if indegree[nxt[0]] == 0:
            q.append(nxt[0])

for i in range(len(count[N])):
    if count[N][i] != 0:
        print(f"{i} {count[N][i]}")

