from collections import deque

M, N, H = map(int, input().split())
tomatos = []

unreaped_cnts = 0
q = deque()
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for k in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0: # 익지 않은 토마토면 unreaped_cnts에 추가
                unreaped_cnts += 1
            elif box[i][j] == 1: # 익은 토마토면 큐에 추가
                q.append((k, i, j, 0)) # z, x, y, 시간
    
    tomatos.append(box)

# 익은걸 큐 돌면서 주변 6방향 안익은거 익히고 익은거 또 큐에 넣고
# 익혔을 때 unreaped_cnts = 0 되면 그때 시간 출력하고
# 큐에서 나왔는데 unreaped_cnts가 0 아니면 -1 출력하고

def bfs():
    global q, tomatos, dx, dy, dz, unreaped_cnts, M, N, H

    while q:
        cur = q.popleft()
        z, x, y, due_time = cur

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 상자 밖이면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue

            # 익은 토마토거나 비어있으면 패스
            if tomatos[nz][nx][ny] == 1 or tomatos[nz][nx][ny] == -1:
                continue

            # 그 외에는 안익은 토마토다
            unreaped_cnts -= 1
            tomatos[nz][nx][ny] = 1

            # 익혔는데 카운트 0되면 시간 출력
            if unreaped_cnts == 0:
                return due_time + 1
            
            # 카운트 아직 0 아니면 큐에 넣기
            q.append((nz, nx, ny, due_time + 1))
    
    # while 빠져나왔는데 카운트 0 아니면 다 못익히는거니까 -1 리턴
    return -1

if unreaped_cnts == 0:
    print(0)
else:    
    print(bfs())
    
