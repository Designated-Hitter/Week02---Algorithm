N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sub_board = [[0] * M for _ in range(N)]
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnts = 0
vis = [[False] * M for _ in range(N)]

def get_zeros(x, y): # 상하좌우 0 개수 구하는 함수
    global board
    temp = 0

    # print(x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print(nx, ny)
        if board[nx][ny] == 0:
            temp += 1
    
    return temp

def bfs(x, y): # 영역 개수 구하는 함수
    global vis, board
    q = []
    q.append((x, y))
    while q:
        cur = q.pop()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 밖이면 패스
                continue

            if board[nx][ny] == 0: # 바다면 패스
                continue

            if vis[nx][ny]: # 이미 방문한 곳이면 패스
                continue

            # 그 외에는 빙하임
            vis[nx][ny] = True
            q.append((nx, ny))
    
while True:
    # 빙하 개수 체크하기
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not vis[i][j]: # 빙하고 방문 안했으면 가기
                vis[i][j] = True
                cnts += 1
                bfs(i, j)

    if cnts >= 2: # 분리 됐으면 출력
        print(ans)
        break

    elif cnts == 0: # 다 녹았으면 0 출력
        print(0)
        break

    else: # 1개면 다시 초기화
        cnts = 0
        vis = [[False] * M for _ in range(N)]
        ans += 1

        # 뺄 값 저장
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0: # 빙하면
                    sub_board[i][j] =  get_zeros(i, j) # 사방 0 개수 구하기
        
        # 값 빼기
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    board[i][j] = max(board[i][j] - sub_board[i][j], 0) # 값에서 빼주고 음수면 0 취하기

    


