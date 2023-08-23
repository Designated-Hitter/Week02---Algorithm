import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]
weights = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())     # 중or완 x를 만드는데 중or기 y가 k개 필요
    graph[y].append((x, k))
    indegree[x] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # result.append((now, status))
        for x, k in graph[now]:
            if weights[now].count(0) == n+1:    # now가 기본부품이라면
                weights[x][now] += k    # x만드는데 기본부품now는 k개 필요
            else:
                for i in range(1, n+1):
                    weights[x][i] += weights[now][i]*k
            

            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

topology_sort()

for i, j in enumerate(weights[n]):
    # n을 만드는데 i부품이 j개 필요하다
    if j > 0:
        print(f'{i} {j}')