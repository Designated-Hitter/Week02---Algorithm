import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = {1:None}
def dfs(u):
    global parent
    for v in graph[u]:
        if v != u and v != parent[u]:
            parent[v] = u
            dfs(v)
    return

dfs(1)

for i in range(2, n+1):
    print(parent[i])