"""
bfs로 풀자
우선 vis 필요하고, 딱 칸에 진입했는데 True면 버리고 False 일때만 다시 큐에 넣기
N, M일 때 cnts값 리턴하고 끝
큐에서 나오는 순서가 시간순서라서 다른 cnts값 더 안봐도 된다.
"""
from collections import deque

N, M = map(int, input().split())
board = []
vis = [[False] * M for _ in range(N)]

for i in range(N):
    board.append(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global N, M, board, vis, dx, dy

    q = deque()
    q.append((0, 0, 1))
    vis[0][0] = True

    while q:
        cur = q.popleft()

        if cur[0] == N - 1 and cur[1] == M - 1:
            return cur[2]

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if vis[nx][ny]:
                continue

            if board[nx][ny] == '0':
                continue

            vis[nx][ny] = True
            q.append((nx, ny, cur[2] + 1))

print(bfs())