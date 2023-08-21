import sys
from collections import deque
N = int(sys.stdin.readline())
pairs = int(sys.stdin.readline())
graph =[[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(pairs):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b] #a에 b 연결
    graph[b] += [a] #b에 a 연결

visited[1] = 1
Q = deque([1])

while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1

print(sum(visited)-1)