import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

result = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = {}
# visited = {}
# for _ in range(m):
#     u, v = map(int, input().split())
#     if u not in graph.keys():
#         graph[u] = [v]
#         visited[u] = False
#     else:
#         graph[u].extend([v])

#     if v not in graph.keys():
#         graph[v] = [u]
#         visited[v] = False
#     else:
#         graph[v].extend([u])


# def dfs(u):
#     if visited[u] == False:
#         visited[u] = True
#         for v in graph[u]:
#             dfs(v)
#         return True
#     return False

# result = 0
# for u in graph.keys():
#     if dfs(u) == True:
#         result += 1

# print(result)