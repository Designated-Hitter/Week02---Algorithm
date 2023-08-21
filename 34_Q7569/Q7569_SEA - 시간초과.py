M, N, H = map(int, input().split())
tomatos = [] # 3차원 배열 tomatos[i][j][k]: i번째 상자의 (j,k)칸 토마토

for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)] # 1이면 익, 0이면 안익
    tomatos.append(box)

days = 0

# 하 우 상 좌 위 아래
dx = [1, 0, -1, 0, 0, 0] 
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def check_all_reaped():
    global tomatos, M, N, H

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 0:
                    return False
    
    return True

def check_around(z, x, y):
    global M, N, H, tomatos, dx, dy, dz

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
            continue

        if tomatos[nz][nx][ny] == 1: # 주변이 익었으면 True
            return True
    
    return False # 6방향 다 확인했는데 다 안익었으면 False


while True:
    # 토마토 다 익었나 확인
    if check_all_reaped():
        print(days)
        break

    # 다 안익었으면 안 익은 토마토만 돌면서 주변에 익은토마토 있으면 해당 위치를 저장 배열에 넣기
    poses_saved = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 0: # 안익은 토마토면,
                    if check_around(i, j, k): # 주변 체크해서 True면 익은거 있음.
                        poses_saved.append((i, j, k)) # (z, x, y)
    
    # 익을 토마토 다 구했는데 비어있으면 -1 출력
    if not poses_saved:
        print(-1)
        break

    # 익을 토마토 있으면 적용
    for pos in poses_saved:
        tomatos[pos[0]][pos[1]][pos[2]] = 1

    # 일수 + 1
    days += 1

