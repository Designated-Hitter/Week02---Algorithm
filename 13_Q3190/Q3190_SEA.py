from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dir_changes = deque()

for _ in range(L):
    dir_changes.append(input().split())

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

game_time = 0
dir = 0


board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 보드에 사과 표시
for apple in apples:
    board[apple[0]][apple[1]] = 1

# 보드에 뱀 표시
# 사과를 먹으면 popleft시키고, 안먹으면 새 위치(머리)를 append한다.
# 우선 초기 위치 넣기.
q = deque()
q.append((1, 1))
cur_x, cur_y = 1, 1
board[cur_x][cur_y] = 2

def check():
    global board, cur_x, cur_y
    nx = cur_x + dx[dir]
    ny = cur_y + dy[dir]

    if nx < 1 or nx > N or ny < 1 or ny > N: # 보드 밖이면 False
        return False
    
    # 몸통 만나면 False
    if board[nx][ny] == 2:
        return False
    
    return True    

while check(): # 갈 수 있으면 가기
    # 갈 수 있다. 큐에 머리 넣기
    cur_x += dx[dir]
    cur_y += dy[dir]
    q.append((cur_x, cur_y))

    # 위치에 사과가 없으면 몸 길이 그대로 -> q.popleft
    if board[cur_x][cur_y] != 1:
        x, y = q.popleft()

        # 꼬리 빼서 0으로 만든다
        board[x][y] = 0

    # 머리 보드에 업데이트
    board[cur_x][cur_y] = 2
    game_time += 1

    # 시간 확인 후 방향 바꾸기
    if len(dir_changes) != 0 and int(dir_changes[0][0]) == game_time:
        if dir_changes[0][1] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        dir_changes.popleft()

    
        
# 못가면 while 나가고 시간 출력
print(game_time + 1)
    





