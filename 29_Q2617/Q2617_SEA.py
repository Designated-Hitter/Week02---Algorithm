"""
트리의 연결 방향을 무거운 쪽, 가벼운 쪽 이렇게 트리 두개를 만들어서 더 큰수, 더 작은 수가 과반이 넘으면 불가능한 수로 판단한다.
"""

N, M = map(int, input().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph1[u].append(v)
    graph2[v].append(u)

vis = [False] * (N + 1)
cnts = [0] * (N + 1)

def dfs(init_node, node, graph):
    global vis, cnts
    vis[node] = True

    for nxt in graph[node]:
        if vis[nxt]:
            continue

        cnts[init_node] += 1
        dfs(init_node, nxt, graph)

ans = set()

for i in range(1, N + 1):
    dfs(i, i, graph1)

    # dfs 결과 과반수를 넘으면 그 값을 set에 넣기
    for j in range(len(cnts)):
        if cnts[j] >= (N + 1) // 2:
            ans.add(j)

    # 방문기록 초기화 해주기
    # 카운트배열 초기화
    for j in range(1, N + 1):
        vis[j] = False
        cnts[j] = 0
    
    dfs(i, i, graph2)
    
    # dfs 결과 과반수를 넘으면 그 값을 set에 넣기
    for j in range(len(cnts)):
        if cnts[j] >= (N + 1) // 2:
            ans.add(j)

    # 방문기록 초기화 해주기
    # 카운트배열 초기화
    for j in range(1, N + 1):
        vis[j] = False
        cnts[j] = 0

print(len(ans))




