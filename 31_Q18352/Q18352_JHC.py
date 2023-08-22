import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0     # 출발 도시까지의 거리는 0으로 설정

def bfs(graph, x, distance):
    queue = deque([x])

    while queue:
        now = queue.popleft()
        # 혀재 도시에서 이동할 수 있는 모든 도시를 확인
        for next_node in graph[now]:
            # 아직 방문하지 않은 도시라면
            if distance[next_node] == -1:
                # 최단거리 갱신
                distance[next_node] = distance[now] + 1
                queue.append(next_node)
                
bfs(graph, x, distance)

# 최단거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m, k, x = map(int, input().split())

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# def bfs(graph, x, visited):
#     queue = deque([x])
#     visited[x] = 1

#     city_num = []
#     flag = 0
#     while queue:
#         v = queue.popleft()
#         # print(v, end = ' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = visited[v] + 1
#                 if visited[i] == k+1:
#                     city_num.append(i)
#                     flag = 1
#         if flag == 1:
#             break
#     return city_num

# visited = [0] * (n+1)

# result = bfs(graph, x, visited)
# if len(result) == 0:
#     print(-1)
# else:
#     result.sort()
#     for x in result:
#         print(x)