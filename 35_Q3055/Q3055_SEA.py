import sys
from collections import deque

R, C = map(int, input().split())
ans = sys.maxsize

q = deque()
dest = 0
board = [[0] * C for _ in range(R)]
saved = []
vis_animal = [[False] * (C + 1) for _ in range(R + 1)] 
vis_water = [[False] * (C + 1) for _ in range(R + 1)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    temp = input()
    
    for j in range(len(temp)):
        if temp[j] == 'D': # 목적지면
            dest = (i, j) 
        
        elif temp[j] == '*': # 물이면 일단 saved에 저장
            vis_water[i][j] = True
            saved.append((i, j))

        elif temp[j] == 'S': # 고슴도치 위치면 큐에 넣기
            vis_animal[i][j] = True
            q.append((i, j, 0, 0)) # x, y, 소요시간, 종류(0: 고슴도치, 1: 물)

    for j in range(len(temp)):
        board[i][j] = temp[j]

# 물 위치 큐에 넣기
for water in saved:
    q.append((water[0], water[1], 0, 1))

# 큐 돌기
while q:
    cur = q.popleft() # 큐에서 빼낸다.

    if cur[3] == 0 and board[cur[0]][cur[1]] != 'S': # 고슴도친데 해당 위치에 고슴도치가 없으면 패스
        continue

    # 목적지에
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위 밖이면 패스
            continue
        
        # 물일 경우
        if cur[3] == 1:
            # 물 방문했었으면 패스
            if vis_water[nx][ny]:
                continue
            # 돌있으면 패스
            if board[nx][ny] == 'X':
                continue

            # 목적지면 패스
            if board[nx][ny] == 'D':
                continue

            # 고슴도치 있으면 먹기
            if board[nx][ny] == 'S':
                board[nx][ny] = '*'
            # 비어있으면 먹기
            if board[nx][ny] == '.':
                board[nx][ny] = '*' 
            
            # 방문체크하고
            vis_water[nx][ny] = True
            board[nx][ny] = '*'
            q.append((nx, ny, cur[2] + 1, 1))
            
        # 고슴도치일 경우
        elif cur[3] == 0:    
            # 고슴도치 방문했었으면 패스
            if vis_animal[nx][ny]:
                continue
            # 물 있으면 패스
            if board[nx][ny] == '*':
                continue
            # 돌 있으면 패스
            if board[nx][ny] == 'X':
                continue

            # 갈 수 있다.
            # 현재 위치 고슴도치는 지우고
            board[cur[0]][cur[1]] = '.'
            
            # 목적지에 도착했으면
            if board[nx][ny] == 'D':
                ans = min(ans, cur[2] + 1)
                break

            # 방문체크하고
            vis_animal[nx][ny] = True
            # 이동
            board[nx][ny] = 'S'
            
            # 큐에 넣기
            q.append((nx, ny, cur[2] + 1, 0))

if ans == sys.maxsize:
    print("KAKTUS")
else:
    print(ans)



    



