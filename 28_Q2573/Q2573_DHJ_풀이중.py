import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    sea_list = [] #바다인 칸의 리스트

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not graph[nx][ny]: #얼음칸 주변이 바다인 만큼 +1
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]: #얼음 주변에 얼음칸이 있고, 아직 방문하지 않았다면
                    q.append((nx, ny))
                    visited[nx][ny] = 1 #방문 표시
        if sea > 0: #바다칸이 존재한다면, sea_list에 append
            sea_list.append((x, y, sea))
    for x, y, sea in sea_list: #sea_list 에 존재하는 빙하 주변 바다칸의 개수만큼 빙하를 녹임
        graph[x][y] = max(0, graph[x][y] - sea) #0보다 작아지면 0으로 만듬

    return 1 #하나의 그룹을 탐색했다는 뜻으로 1을 return (빙하가 쪼개지면  bfs를 여러번 돌고 2이상으로 반환될 수 있도록)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ice = []
for i in range(N):
    for j in range(M):
        if graph[i][j]: #최초 맵에서 얼음의 위치를 담은 배열
            ice.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * M for _ in range(N)]
    del_list = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0: #bfs탐색이 끝나고 바다가 된 빙하를 체크
            del_list.append((i, j)) #곧 삭제할 list에 append
    if group > 1: #빙하그룹이 2개 이상이면 year를 출력하고 반복문을 종료
        print(year)
        break
    ice = sorted(list(set(ice) - set(del_list))) #원본 빙하에서 삭제해야 할 빙하를 빼주기
    year += 1

if group < 2:
    print(0)




# def melt(iceberg):
#          #상, 하, 좌, 우
#     dx = [-1, 1, 0 ,0]
#     dy = [0, 0, -1, 1]
#     global count
#     for x in range(1, len(iceberg)):
#         for y in range(len(iceberg[x])):
#             if iceberg[x][y] < 0:
#                 iceberg[x][y] = 0
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 #평면 너머는 계산하지 않음
#                 if nx < 0 or nx >= N or ny < 0 or ny >= M: 
#                     continue
#                 if iceberg[x][y] == 0:
#                     iceberg[nx][ny] = iceberg[x][y] - 1

#     count += 1
#     return iceberg

# visited = [False] * (N + 1)
# cut = 0
# def dfs(iceberg, start):
#     melt(iceberg)
#     if visited[start] != 0:
#         #해당 노드를 방문 체크
#         visited[start] = True
#     else:
#          dfs(iceberg, start + 1)
#     #해당 시작점을 기준으로 계속 dfs 탐색
#     for i in iceberg[start]:
#         if not visited[i]:
#             dfs(iceberg, i + 1)

# for i in range(1, N + 1):
#     if cut == 2:
#         print(count)
#         break
#     if not visited[i]: #i번째 인덱스 노드를 방문하지 않았다면
#         if not iceberg[i]: #해당 노드가 연결된 그래프가 없다면
#             cut += 1 
#             visited[i] = True
#         else:
#             dfs(iceberg, 1)
#             cut += 1
    