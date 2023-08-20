#연결된 노드들을 간선을 따라 dfs 또는 bfs로 순회하면서 방문한 노드들엔 방문 기록을 남긴다.
#연결된 노드들을 다 돌고나서 dfs를 빠져나올 때 마다 count += 1하면 해결
#연결되었던 노드들은 visited 값이 True이므로 다시 순회하지 않음

import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start, depth):
    visited[start] = True #해당 노드를 방문 체크
    #해당 시작점을 기준으로 계속 dfs 탐색
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1 + N)
count = 0
#1~N 노드를 반복하면서
for i in range(1, N + 1):
    if not visited[i]: #i번째 인덱스 노드를 방문하지 않았다면
        if not graph[i]: #해당 노드가 연결된 그래프가 없다면
            count += 1 
            visited[i] = True
        else:
            dfs(i,0)
            count += 1

print(count)