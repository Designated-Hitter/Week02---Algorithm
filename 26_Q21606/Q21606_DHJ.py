#실외 노드가 존재하고, 실외 노드와 연결된 실내노드가 존재할 때, 실내 - 실외 - 실내 산책 루트의 개수 nP2
#실내 노드 끼리 산책 루트의 개수는 2 (a -> b, b -> a)

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v, count):
    visited[v] = True

    for i in graph[v]: #실외 노드 v와 연결된 인접노드
        if location[i] == 1: #인접 노드의 위치가 실내라면
            count += 1
        elif not visited[i] and location[i] == 0: #아직 방문하지 않은데다가 실외라면
            count = dfs(i, count) #다음 실외 노드를 기준으로 인접한 실내 노드를 구하는 재귀함수
    return count


N = int(input())

location = [0] + list(map(int, input().strip())) #node의 인덱스를 1부터 세기 위해서 앞에 0을 추가

answer = 0
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1: #시작과 끝이 실내라면
        answer += 2

sum = 0
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i] and location[i] == 0: #방문하지 않은 + 실외라면
        x = dfs(i, 0) #dfs 실행 => 실외 노드와 연결된 실내 노드의 수 return
        sum += x*(x-1) #실외노드를 경유하는 산책의 경우의 수는 nP2이므로

print(sum + answer)
