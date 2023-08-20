from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

q = deque()

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

st, en = map(int, input().split())

vis = [False] * (N + 1)
max_dist = -1
total_paths = set()
paths = []

def dfs(node, times):
    global total_paths, max_dist, paths, vis

    if node == en: # 도착했음.
        # 시간이 더 많이 걸렸으면
        if max_dist < times:
            total_paths = set(paths)
        
        # 똑같이 걸렸으면
        elif max_dist == times:
            # set에 추가
            total_paths = total_paths.union(set(paths))
            
        # 기존 값과 갱신
        max_dist = max(max_dist, times)
        return
        

    for nxt in graph[node]:
        if vis[nxt[0]]:
            continue

        vis[nxt[0]] = True
        paths.append((node, nxt[0]))
        dfs(nxt[0], times + nxt[1])
        paths.pop()
        vis[nxt[0]] = False

dfs(st, 0)
print(max_dist)
print(len(total_paths))