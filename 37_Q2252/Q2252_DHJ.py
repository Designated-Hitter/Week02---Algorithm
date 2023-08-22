import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split()) #N은 노드의 개수, M은 간선의 개수

indegree = [0] * (N + 1) #모든 노드에 대한 진입차수는 0으로 초기화

graph =[[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split()) #1 -> 3, 2 -> 3 단방향 노드라고 생각
    graph[A].append(B)
    #진입 차수를 1 증가
    indegree[B] += 1

def topology_sort():
    result = []
    q = deque()

    #처음 시작할 때 진입차수가 0인 노드(최초의 노드)를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    #위상정렬을 수행한 결과 출력
    for i in result:
        print(i, end =" ")

topology_sort()