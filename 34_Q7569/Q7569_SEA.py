from collections import deque

M, N, H = map(int, input().split())
tomatos = [] # 3차원 배열 tomatos[i][j][k]: i번째 상자의 (j,k)칸 토마토

for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)] # 1이면 익, 0이면 안익
    tomatos.append(box)

days = 0

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

"""
익은 토마토만 큐에 일단 넣고 하나씩 뺀다. 이후 6방향 보면서 안익은 토마토 있으면 익히고 큐에 넣는다.
완전탐색과 다른점은 바로 익은게 반영되지 않는다는 거다.
"""

# 우선 안 익은 토마토의 개수를 구한다.
unreaped_cnts = 0
q = deque()

# 이후 큐에 익은 토마토를 넣는다.(익은 토마토 위치, 경과일수)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0: # 안 익었으면 개수 더하기
                unreaped_cnts += 1
            elif tomatos[i][j][k] == 1: # 익었으면 큐에 저장.
                q.append((i, j, k, 0)) # (z, x, y, 경과일수)

# 하나씩 빼서 봤을 때 지금까지 익힌 토마토 개수가 안 익은 토마토의 개수와 같으면 경과일수를 출력한다.
flag = False

if unreaped_cnts == 0:
    print(0)

while q:
    cur = q.popleft()
    z, x, y, days = cur

    # 다 안익었으면 6방향 확인
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H: # 범위 밖이면 패스
            continue
        
        if tomatos[nz][nx][ny] == 0: # 안익은거면
            # 익은걸로 바꾸고
            tomatos[nz][nx][ny] = 1 

            # unreaped 빼주고
            unreaped_cnts -= 1
            
            if unreaped_cnts == 0:
                print(days + 1)
                flag = True
                break

            # 큐에 넣기
            q.append((nz, nx, ny, days + 1))
    
    if flag:
        break

if unreaped_cnts != 0: # 큐에서 나왔는데 안익은거 남았으면 -1 출력
    print(-1)
            
            


