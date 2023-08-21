#DFS 는 재귀로, BFS 는 queue로 구현하는 것이 보통
import sys
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)] #각 변이 N+1 인 평면

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_1 = [False] * (N + 1) #DFS의 방문기록
visited_2 = [False] * (N + 1) #BFS의 방문기록

def BFS(V):
    q = deque([V]) 
    visited_2[V] = True #해당 V값을 방문 True
    while q: #len(q) == 0일 때 까지 반복
        V = q.popleft() #Q의 첫 값을 꺼내서 V로 선언
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited_2[i] and graph[V][i]: #i를 방문하지 않았고, V와 연결이 되어있었다면
                q.append(i) #i추가
                visited_2[i] = True

def DFS(V):
    visited_1[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited_1[i] and graph[V][i]:#i를 방문하지 않았고, V와 연결이 되어있었다면
            DFS(i) #더 깊이 탐색

DFS(V)
print()
BFS(V)