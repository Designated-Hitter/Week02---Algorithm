import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 맵 안벗어났는지.
def check_range(y, x):
    return (0 <= y < n) and (0 <= x < n)

def dijkstra(y, x):
    hq = []
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[0]*n for _ in range(n)]
    # (가중치-비용, 노드y좌표, 노드x좌표) 
    heapq.heappush(hq, (0, y, x))
    visited[y][x] = 1
    while hq:
        weight, cy, cx = heapq.heappop(hq)
        if cy == n-1 and cx == n-1:
            return weight

        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if check_range(ny, nx) and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if graph[ny][nx]:
                    heapq.heappush(hq, (weight, ny, nx))
                else:
                    heapq.heappush(hq, (weight + 1, ny, nx))

answer = dijkstra(0, 0)
print(answer)