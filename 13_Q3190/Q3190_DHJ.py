import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple_list = []
for _ in range(K):
    apple_list.append(list(map(int, sys.stdin.readline().split())))
print(apple_list)

L = int(sys.stdin.readline())
turn_list = deque()
for _ in range(L):
    turn_list.append(list(sys.stdin.readline().split()))
print(turn_list)

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