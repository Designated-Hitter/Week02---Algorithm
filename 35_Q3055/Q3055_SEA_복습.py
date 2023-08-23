from collections import deque
R, C = map(int, input().split())
board = [[0] * C for _ in range(R)]

for i in range(R):
    line = input()
    for j in range(len(line)):
        board[i][j] = line[j]

start = (0, 0)
dst = (0, 0)
waters = []
water_vis = [[False] * (C + 1) for _ in range(R + 1)]
animal_vis = [[False] * (C + 1) for _ in range(R + 1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            dst = (i, j)
        
        elif board[i][j] == '*':
            waters.append((i, j))

        elif board[i][j] == 'S':
            animal_vis[i][j] = True
            q.append((i, j, 0, 1)) # x좌표, y좌표, 시간, 타입(0: 물, 1: 고슴도치)
            start = (i, j)

for water in waters:
    water_vis[water[0]][water[1]] = True
    q.append((water[0], water[1], 0, 0))

def bfs():
    global R, C, board, start, dst, waters, water_vis, animal_vis, dx, dy, q

    while q:
        cur = q.popleft()
        cur_x, cur_y, due_time, kind = cur

        # 고슴도치 꺼냈는데 지금 보드에는 물이 있으면 죽은거라서 패스
        if kind == 1 and board[cur_x][cur_y] == '*':
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 범위 밖이면 패스
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            # 돌 만나면 패스
            if board[nx][ny] == 'X':
                continue

            # 이제 . or D or x임
            
            # kind가 고슴도치면 방문체크하고 큐에 넣기
            if kind == 1:
                # 도착했다면 끝
                if board[nx][ny] == 'D':
                    board[nx][ny] = 'S'
                    return due_time + 1
                
                # 빈칸일 때만 가기
                if board[nx][ny] == '.':
                    board[nx][ny] = 'S'
                    board[cur_x][cur_y] = '.'
                    animal_vis[nx][ny] = True
                    q.append((nx, ny, due_time + 1, 1))
            
            # 물인 경우
            else:
                # 빈칸이거나 고슴도치일 때만 가기
                if board[nx][ny] == '.' or board[nx][ny] == 'S':
                    board[nx][ny] = '*'
                    water_vis[nx][ny] = True
                    q.append((nx, ny, due_time + 1, 0))
    
    # while에서 리턴 안되면 도착 못한거다.
    return "KAKTUS"

print(bfs())
                








            
    