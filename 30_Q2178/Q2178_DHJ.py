from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().strip())))

     #상, 하, 좌, 우
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #양쪽 벽면 때문에 이동이 막히는 경우 
            if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                continue
            #0이어서 못 가는 경우
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]

print(BFS(0,0))