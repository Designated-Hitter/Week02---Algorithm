N = int(input())
types = input()
graph = [[] for _ in range(N + 1)]
vis = [False] * (N + 1)
ans = 0

for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    if types[u - 1] == '1' and types[u - 1] == types[v - 1]:
        ans += 2 

# 실내 = 1, 실외 = 0
# 실외 무리를 순회해서 인접하는 실내 개수를 구한다.
# 실내 무리 중 2개를 뽑아 순열의 경우의 수를 cnts에 추가한다.

def bfs1(node):
    global vis

    cnts = 0
    q = []
    q.append(node)
    vis[node] = True

    while q:
        cur = q.pop()

        for nxt in graph[cur]:
            # 방문 했었으면 패스
            if vis[nxt]:
                continue

            # 방문 안했던 경우

            # 우선 실내면 추가만.
            if types[nxt - 1] == '1':
                # temp = nxt
                cnts += 1

            # 실외면 큐에 넣기
            else:
                vis[nxt] = True
                q.append(nxt)

    # if cnts == 1:
        # vis[temp] = False

    return cnts
        
# 실외 순회
for i in range(1, N + 1):
    cnts = 0

    if types[i - 1] == '0' and not vis[i]: # 실외인 노드고 방문 안했으면.
        cnts = bfs1(i) # bfs 돌려서 인접 실내 개수 구함.
    
        ans += cnts * (cnts - 1)

print(ans)

