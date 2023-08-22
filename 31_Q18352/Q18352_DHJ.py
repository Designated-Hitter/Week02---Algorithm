from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [0] * (N + 1) #거리를 담는 리스트를 하나 추가
visited = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) #단방향 도로이므로 A -> B 값만 표시

def BFS(start):
    answer = []
    que = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while que:
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1 #모든 도시 간 거리가 1이므로 i로 가는 거리는 현재 거리 + 1
                if distance[i] == K: #거리가 K값과 같다면
                    answer.append(i)#answer에 정답인 도시를 추가
                    continue
                que.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

BFS(X)