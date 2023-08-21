from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

"""
시작점을 X로 하고 bfs 돌다가 다른 도시 방문했을 때 비용합이 K면 배열에 추가하고 다음거 확인
근데 지금 도시를 한번만 방문할 수 있다는 가정이 없으므로, continue 되는 조건은 비용합이 K + 1가 되었을 때이다.
-> 이런 줄 알았는데 한 번 방문한 도시는 다시 가면 안됨
"""
ans = []
vis = [False] * (N + 1)

def bfs():
    global N, M, K, X, graph

    q = deque()
    q.append((X, 0)) # 시작 도시, 이동횟수
    
    while q:
        cur = q.popleft()

        # 만약 k번 이동했으면, X가 아닌 도시일 때 정답 set에 추가
        if cur[1] == K and cur[0] != X:
            vis[cur[0]] = True # 방문체크하고
            ans.append(cur[0]) # 답에 넣기.
            continue

        # K번 초과했으면 패스
        if cur[1] > K:
            continue

        for nxt in graph[cur[0]]:
            if vis[nxt]:
                continue

            # 빼내서 방문에 체크하고 넣기
            vis[nxt] = True
            q.append((nxt, cur[1] + 1))
bfs()


if not ans:
    print(-1) 
else:
    for n in sorted(ans):
        print(n)
    
