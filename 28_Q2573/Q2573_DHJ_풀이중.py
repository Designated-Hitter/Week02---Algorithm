import sys
input = sys.stdin.readline

N, M = map(int, input().split())
iceberg = []
for _ in range(N):
    iceberg.append(list(map(int, input().split())))

print(iceberg)
count = 0

def melt(iceberg):
         #상, 하, 좌, 우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    global count
    for x in range(1, len(iceberg)):
        for y in range(len(iceberg[x])):
            if iceberg[x][y] < 0:
                iceberg[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #평면 너머는 계산하지 않음
                if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                    continue
                if iceberg[x][y] == 0:
                    iceberg[nx][ny] = iceberg[x][y] - 1

    count += 1
    return iceberg

visited = [False] * (N + 1)
cut = 0
def dfs(iceberg, start):
    melt(iceberg)
    if visited[start] != 0:
        #해당 노드를 방문 체크
        visited[start] = True
    else:
         dfs(iceberg, start + 1)
    #해당 시작점을 기준으로 계속 dfs 탐색
    for i in iceberg[start]:
        if not visited[i]:
            dfs(iceberg, i + 1)

for i in range(1, N + 1):
    if cut == 2:
        print(count)
        break
    if not visited[i]: #i번째 인덱스 노드를 방문하지 않았다면
        if not iceberg[i]: #해당 노드가 연결된 그래프가 없다면
            cut += 1 
            visited[i] = True
        else:
            dfs(iceberg, 1)
            cut += 1
    