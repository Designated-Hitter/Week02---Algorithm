#0. 이분 그래프는 무엇인가
# 집합이 두 개 있을 때, 인접한 노드끼리 서로 다른 집합에 넣을 수 있다면 이분 그래프
# 즉, DFS로 node들을 돌 때, 직전에 지나왔던 node와 이번 node의 그룹이 같다면 이분 그래프가 아님
# visited[i] 가 0이라면 미탐색, 1이라면 group 1, -1이라면 group 2

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(start, visited, graph, group):
    visited[start] = group # visited 배열의 현재 요소에 그룹값 저장 

    for v in graph[start]:
        if visited[v] == 0: #인접 노드를 아직 방문하지 않았다면
            result = DFS(v, visited, graph, -(group)) #그룹을 바꿔서 다시 DFS
            if not result:
                return False
        else:
            if visited[v] == group: #연결된 노드와 그룹이 같으므로 이분 그래프가 아님
                return False
            
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result:
                break

    if result:
        print('YES')
    else:
        print('NO') 