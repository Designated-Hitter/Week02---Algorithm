import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
bus_list = []
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append(end)
    bus_list.append([start, end, cost])

target_start, target_end = map(int, input().split())
print(bus_list)
print(target_start)
print(target_end)

costs = [0] * (N + 1) #비용을 담는 리스트를 하나 추가
visited = [False] * (N + 1)

def BFS(start):
    answer = []
    que = deque([start])
    visited[start] = True
    costs[start] = 0
    while que:
        now = que.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            que.append(i)
            costs[i] = costs[now] + cost #모든 도시 간 거리가 1이므로 i로 가는 거리는 현재 거리 + 1
            if i == target_end: #거리가 K값과 같다면
                answer.append(costs[i]) #answer에 정답인 도시를 추가

BFS(target_start)
print(min(costs))