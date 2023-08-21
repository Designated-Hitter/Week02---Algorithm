#실외 노드가 존재하고, 실외 노드와 연결된 실내노드가 존재할 때, 실내 - 실외 - 실내 산책 루트의 개수 nP2
#실내 노드 끼리 산책 루트의 개수는 2 (a -> b, b -> a)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

A_list = list(str(input()).strip())

print(A_list)
outside = []
for i in range(len(A_list)):
    if A_list[i] == '0':
        outside.append(int(i) + 1) #0인 인덱스를 찾아 outside에 넣고 +1

print(outside)

graph = [[] for _ in range(N + 1)]
print(graph)
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    if a in outside or b in outside:
        graph[a].append(2) #실외인 경우 그래프에 2를 입력
        graph[b].append(2)
    else:
        graph[a].append(1) #실내인 경우 그래프에 1을 입력
        graph[b].append(1)
print(graph)

visited = [0] * (N + 1)

def DFS(i):
    visited[i] = 1
    for j in range(1, N + 1):
        if visited[i] == 0:
            if graph[i][j] == 2:
                visited[i] = 2
            else:
                visited[i] = 1
            DFS(j)

DFS(1)
print(visited)
