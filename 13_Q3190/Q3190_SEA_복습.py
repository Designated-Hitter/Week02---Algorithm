# 27분
from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dirs = deque()

for i in range(L):
    dirs.append(input().split())

board = [[0] * (N + 1) for _ in range(N + 1)]

for apple in apples:
    board[apple[0]][apple[1]] = 1 # 사과 위치에 1 넣음

board[1][1] = 2 # 뱀 위치에 2 넣음

game_time = 0
dir = 0
cur_x, cur_y = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((1, 1))

while True:
    # 다음 뱀 머리 위치
    cur_x += dx[dir]
    cur_y += dy[dir]

    # 갈 수 있는지 체크

    # 보드 밖이면 끝
    if cur_x < 1 or cur_x > N or cur_y < 1 or cur_y > N:
        game_time += 1
        break

    # 뱀 만나면 끝
    if board[cur_x][cur_y] == 2:
        game_time += 1
        break

    q.append((cur_x, cur_y))

    # 사과 만났으면 
    if board[cur_x][cur_y] == 1:
        # 보드에 뱀 넣기
        board[cur_x][cur_y] = 2
    
    # 빈칸 만났으면
    if board[cur_x][cur_y] == 0:
        # 보드에 뱀 넣고
        board[cur_x][cur_y] = 2
        # 길이 안 길어지니까 큐에서 하나 빼고
        tail = q.popleft()
        # 보드에서 지우기
        board[tail[0]][tail[1]] = 0
    
    # 다 움직였으면 이제 게임시간 + 1 해주고 방향 바꾸기
    game_time += 1

    if dirs and int(dirs[0][0]) == game_time:
        if dirs[0][1] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        dirs.popleft()

print(game_time)

