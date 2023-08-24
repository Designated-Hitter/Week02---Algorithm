import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N + 1) #모든 노드에 대한 진입차수는 0으로 초기화 

graph =[[] for _ in range(N + 1)]
needs = [[0] * (N + 1) for _ in range(N + 1)] #각 제품(부품)을 만들 때 필요한 부품

for _ in range(M):
    a, b, c = map(int, input().split()) #완성품, 재료, 필요 수량
    graph[b].append((a, c)) #graph[완성품] 에 재료와 필요 수량을 append
    indegree[a] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    #현 제품의 다음단계 번호, 현 제품이 얼마나 필요한지
    for next, next_need in graph[now]: 
        #만약 현 제품이 기본 부품이면
        if needs[now].count(0) == N + 1:
            needs[next][now] += next_need
        #현 제품이 중간 부품이면
        else:
            for i in range(1, N + 1):
                needs[next][i] += needs[now][i] * next_need

        #차수 - 1
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
print(needs)




#         indegree[nxt[0]] -= 1

#         if indegree[nxt[0]] == 0:
#             q.append(nxt[0])

# for i in range(len(count[N])):
#     if count[N][i] != 0:
#         print(f"{i} {count[N][i]}")

