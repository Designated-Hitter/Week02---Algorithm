import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple_list = []
for _ in range(K):
    apple_list.append(list(map(int, sys.stdin.readline().split())))

L = int(sys.stdin.readline())
turn_list = deque()
for _ in range(L):
    turn_list.append(list(sys.stdin.readline().split()))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

game_time = 0
dir = 0

#각 변이 N인 2차원 리스트
board = [[0 for _ in range(N + 1)] for _ in range(N + 1)] 

#사과의 위치 표시
for apple in apple_list:
    board[apple[0]][apple[1]] = 1 #1은 사과가 있다는 뜻

# 보드에 뱀 표시
# 사과를 먹으면 popleft시키고, 안먹으면 새 위치(머리)를 append한다.
# 우선 초기 위치 넣기.
snake = deque()
snake.append((1, 1))
cur_x, cur_y = 1, 1
board[cur_x][cur_y] = 2 #2는 뱀이 있다는 뜻

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

while check(): #check함수의 return이 True라면 계속 뱀이 나아감.
    cur_x += dx[dir]
    cur_y += dy[dir]
    #뱀이 (cur_x, cur_y)로 머리를 넣었음
    snake.append((cur_x, cur_y))

    # 위치에 사과가 없으면 몸 길이 그대로 -> snake deque 에서 꼬리가 빠짐
    if board[cur_x][cur_y] != 1:
        x, y = snake.popleft()
        # 꼬리가 사라져서 2->0으로 만든다
        board[x][y] = 0

    # 머리의 위치를 보드에 업데이트
    board[cur_x][cur_y] = 2
    game_time += 1

    # 시간 확인 후 방향 바꾸기
    if len(turn_list) != 0 and int(turn_list[0][0]) == game_time:
        #방향 명령이 D라면 우 -> 하 -> 좌 -> 상 
        if turn_list[0][1] == 'D':
            dir = (dir + 1) % 4
        #방향 명령이 L이라면 우 -> 상 -> 좌 -> 하   
        else:
            dir = (dir - 1) % 4
        turn_list.popleft()

    
        
# check()의 return이 False라면 while 반복문을 나가고 시간을 출력
print(game_time + 1)