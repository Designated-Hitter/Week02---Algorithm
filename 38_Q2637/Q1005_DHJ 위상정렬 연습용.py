import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split()) #N = 건물(노드) 개수 K = 규칙(간선) 개수
    time = [0] + list(map(int, input().split()))

    print(time)
    graph = [[] for _ in range(K + 1)]
    indegree = [0] * (N + 1) #모든 노드에 대한 진입차수는 0으로 초기화
    dp = [0 for _ in range(N + 1)] #비용을 기록하기 위한 리스트
    q = deque()

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

        while q:
            now = q.popleft()

            for i in graph[now]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[now]+time[i])
                #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        

    print(dp[W])            

