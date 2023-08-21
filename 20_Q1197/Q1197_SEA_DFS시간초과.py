import sys
sys.setrecursionlimit(100000)
V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
vis = [False] * (V + 1)
min_weights = sys.maxsize
cnts = 1

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

"""
dfs 풀이
"""

# 왔다갔다 비용이 같아서 하나만 봐도 된다.
# for i in range(1, V + 1):
#     dfs(i) # 정점 1이 시작점일 때의 

def dfs(city, weights):
    global cnts, min_weights, vis, graph
    vis[city] = True

    if cnts == V:
        min_weights = min(min_weights, weights)
        return
    
    for nxt in graph[city]:
        if not vis[nxt[0]]:
            cnts += 1
            dfs(nxt[0], weights + nxt[1])
            vis[nxt[0]] = False
            cnts -= 1

dfs(1, 0)
print(min_weights)