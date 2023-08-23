from collections import deque

n = int(input())

indegree = [0]*n
graph = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            indegree[j] += 1

def topology_sort():
    if 0 not in indegree:
        print(-1)
        return

    result = [0]*n
    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    num = 1
    while q:
        now = q.popleft()
        result[now] = num
        for i, x in enumerate(graph[now]):
            if x == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        num += 1

    for i in result:
        print(i, end=' ')

topology_sort()