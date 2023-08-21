import sys
from collections import deque

N = int(input())
board = [input() for _ in range(N)]
ans = sys.maxsize

"""
검은색을 발견했으면 검은색 카운트 하고 간다.
이후 끝방에 도달했을 때 검은색 카운트를 min으로 갱신한다.
"""
vis = [[False] * N for _ in range(N)]
q = deque()
q.append((0, 0, 0)) # 큐의 요소: (x좌표, y좌표, 검은색 카운트)
vis[0][0] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnts = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
cnts[0][0] = -1

while q:
    cur = q.popleft()

    # 끝방 도달했을 때 ans 갱신
    if cur[0] == N - 1 and cur[1] == N - 1:
        ans = min(ans, cur[2])
        continue

    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]

        # 보드 밖이면 패스
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        # 흰색인데
        if board[nx][ny] == '1':
            # 해당 위치 카운트가 지금 cur보다 크면 넣기
            # 이미 방문했으면 패스
            if cnts[nx][ny] > cur[2]:
                cnts[nx][ny] = cur[2]
                q.append((nx, ny, cur[2]))

            # if vis[nx][ny]:
            #     continue

            # 처음이면 체크하고 넣기
            # vis[nx][ny] = True
            # cnts[nx][ny] = cur[2]
            # q.append((nx, ny, cur[2]))
        
        # 검은색인데
        if board[nx][ny] == '0':
            # 지금까지 검은색 밟은 개수가 더 작으면 밟기
            if cnts[nx][ny] > cur[2] + 1:
                cnts[nx][ny] = cur[2] + 1
                q.append((nx, ny, cnts[nx][ny]))

print(ans)


