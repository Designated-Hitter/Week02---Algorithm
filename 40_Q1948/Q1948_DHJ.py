#출발 -> 도착 가중치
#가장 오래 걸리는 경로
#가장 오래 걸리는 경로가 몇 개 인지

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 도로의 개수

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
bgraph = [[] for _ in range(N + 1)]    # backward of graph 역방향 비용 계산을 하기 위한 백워드 그래프
result = [0] * (N + 1)
check = [0] * (N + 1)

q = deque()

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    bgraph[b].append((a, t))
    indegree[b] += 1
start, end = map(int, input().split())

q.append(start)

def topology_sort():
    while q:
        now = q.popleft()
        for i, t in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + t) #이미 result에 들어있던 값과 현재까지의 값 + 시간 중 누가 더 큰지
            if indegree[i] == 0:
                q.append(i)

    #백트래킹 - 도착점 -> 시작점으로 
    count = 0 #임계경로에 속한 모든 정점의 개수
    q.append(end)
    while q:
        now = q.popleft()
        for i, t in bgraph[now]:
            if result[now] - result[i] == t: #도착점까지의 최대 비용 - 시작점으로부터의 비용 = 현재 비용 이라면 이 경로는 가장 오래걸리는 간선
                
                if check[i] == 0: #단 이 간선을 간 적이 없어야 q에 append
                    count += 1
                    q.append(i)
                    check[i] == 1

    print(result[end])
    print(count)

topology_sort()