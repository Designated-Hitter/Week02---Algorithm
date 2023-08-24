#검은 벽을 통과할 때 마다 비용 카운트를 +1 올리고 끝에 도착 했을 때 통과한 검은 벽의 수(비용)를 계산하는 다익스트라 알고리즘
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maze = []
for _ in range(N):
    maze.append(list(map(int,input().strip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(maze)

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == N - 1: #도착했다면
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if maze[nx][ny] == 1: #하얀방
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else: #검은 방
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1 #검은 방을 하얀방으로 바꿀 횟수를 추가

print(bfs())