import sys
from collections import deque
N = int(input())
board = [input() for _ in range(N)]
black_cnts = [[sys.maxsize] * (N + 1) for _ in range(N + 1)] 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

"""
우선, bfs로 풀고, 큐에 들어갈 값들은 (방문한 위치, 검은방 들어간 횟수다)
검은 방 들어간 횟수를 담는 배열을 만들고 여기에다가도 저장을 하는데, 흰방을 검은방 여러개 방문하고 지름길로 간 경우와, 검은방은 안갔지만 돌아간 경우가 있을 때 후자의 루트를 택해야 하므로 비교과정이 필요하다.
"""

q = deque()
q.append((0, 0, 0))
ans = sys.maxsize

while q:
    cur = q.popleft()
    cur_x, cur_y, black_cnt = cur

    if cur_x == N - 1 and cur_y == N - 1:
        ans = min(ans, black_cnt)
        continue

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 밖이면 패스
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        # 1(흰방)에 갔을 때
        if board[nx][ny] == '1':
            # 큐에 있던 black_cnt가 black_cnts에 적힌 값보다 작으면 배열에 적고 가기
            if black_cnt < black_cnts[nx][ny]:
                black_cnts[nx][ny] = black_cnt
                q.append((nx, ny, black_cnt)) 

        # 0(검은방)에 갔을 때
        else:
            # 방문은 했었지만 더 적은 검은방 카운트면 가기
            if black_cnt + 1 < black_cnts[nx][ny]:
                black_cnts[nx][ny] = black_cnt + 1
                q.append((nx, ny, black_cnt + 1))
            

print(ans)