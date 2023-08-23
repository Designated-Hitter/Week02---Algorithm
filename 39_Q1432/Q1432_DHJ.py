#위상정렬의 조건에 맞지 않은 형태의 그래프(순환하는 형태)라면 -1이 뜨는 것 같음..
#문제의 조건인 v1 -> v2 로 연결된 간선에서 v2가 더 작은 경우, v2와 v1의 크기를 교환하고 조건이 성립하는지 다시 확인하면 될 것 같은데
#문제는 원래 배열의 순서대로 바뀐 노드의 값을 어떻게 기억하고 다시 출력할지 모르겠음


import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
answer = [0] * (N + 1)
indegree = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
nodes = []
for i in range(1, N + 1):
    node = [0] + list(map(int, input().rstrip()))
    for j in range(1, N + 1):
        if node[j] == 1: #최대힙으로 계산하니까 간선의 방향도 반대로
            graph[j].append(i)
            indegree[i] += 1


# print(graph)
# print(indegree)



def topology_sort():

    q = []

    #처음 시작할 때 진입차수가 0인 노드(최초의 노드)를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            #heapq.heappush(q,i) <- 최소힙
            heapq.heappush(q, -i) #<- 최대힙
    n = N #최대힙으로 정렬한 원소들을 뒤에서부터 채우는 방식으로
    while q:
        now = -(heapq.heappop(q))
        answer[now] = n
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for k in graph[now]:
            indegree[k] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[k] == 0:
                heapq.heappush(q, -k) #heappush 최대힙으로
        n -= 1

topology_sort()
if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])