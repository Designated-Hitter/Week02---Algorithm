import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s #다른 dfs문제와 다른 점은 visited[i]의 값을 단순히 t/f나 0이 아닌 재귀를 시작한 원소값으로 주어서 어떤 부모 노드로부터 왔는지 표시를 남기는 것
            dfs(i)

dfs(1)

for j in range(2, N+1):
    print(visited[j])

