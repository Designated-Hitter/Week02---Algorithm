#구슬의 무게를 기준으로 최소힙, 최대힙을 계산한 후, 어떤 구슬의 자기 이하의 값을 가진 구슬의 개수가 총 구슬의 과반수 이상일때 그 구슬은 중간이 절대로 될 수 없음
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph1 = [[] for _ in range(N + 1)] #최소힙
graph2 = [[] for _ in range(N + 1)] #최대힙

for i in range(M):
    x, y = map(int, input().split())
    graph1[x].append(y)
    graph2[y].append(x)

visited = [False] * (N + 1)
count = [0] * (N + 1)

def dfs(init_node, node, graph):
    global visited, count
    visited[node] = True

    for nxt in graph[node]:
        if visited[nxt]:
            continue

        count[init_node] += 1
        dfs(init_node, nxt, graph)

answer = set()

for i in range(1, N + 1):
    dfs(i, i, graph1)

    #dfs 결과 i 이하의 구슬의 개수가 과반수를 넘었다면 set에 추가
    for j in range(len(count)):
        if count[j] >= (N + 1) // 2:
            answer.add(j)

    #방문기록 초기화, 카운트 초기화
    for j in range(1, N + 1):
        visited[j] = False
        count[j] = 0
    
    dfs(i, i, graph2)
    
    # dfs 결과 과반수를 넘으면 그 값을 set에 넣기
    for j in range(len(count)):
        if count[j] >= (N + 1) // 2:
            answer.add(j)

    # 방문기록 초기화 해주기
    # 카운트배열 초기화
    for j in range(1, N + 1):
        visited[j] = False
        count[j] = 0

print(len(answer))
