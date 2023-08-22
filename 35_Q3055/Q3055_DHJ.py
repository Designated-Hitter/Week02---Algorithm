import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
forests = [list(input().strip()) for _ in range(R)]

distance = [[0] * C for _ in range(R)] #거리를 배열이 아닌 2차원 평면으로 측정

     #상, 하, 좌, 우
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

q = deque()

# def flood():
#     for x in range(len(forests)):
#         for y in range(len(x)):
#             if forests[x][y] =='*':
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     #양쪽 벽면 때문에 물이 막히는 경우 
#                     if nx < 0 or nx >= R or ny < 0 or ny >= C: 
#                         continue
#                 #돌로 물길이 막힌 경우
#                 if forests[nx][ny] == 'X':
#                     continue
#                 elif forests[nx][ny] == '.' or forests[nx][ny] == 'D':
#                     forests[nx][ny] == '*'

def bfs (Dx, Dy):
    while q:
        x, y = q.popleft()
        
        if forests[Dx][Dy] == "S":
            return distance[Dx][Dy]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if (forests[nx][ny] == '.' or forests[nx][ny] == 'D') and forests[x][y] == 'S':
                    forests[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                elif (forests[nx][ny] == '.' or forests[nx][ny] == 'S') and forests[x][y] == '*':
                    forests[nx][ny] = '*'
                    q.append((nx, ny))
    return 'KAKTUS'

for x in range(R):
    for y in range(C):
        if forests[x][y] == 'S':
            q.append((x, y))
        elif forests[x][y] == 'D':
            Dx, Dy = x, y

for x in range(R):
    for y in range(C):
        if forests[x][y] == '*':
            q.append((x,y))

print(bfs(Dx, Dy))