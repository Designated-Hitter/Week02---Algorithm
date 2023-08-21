import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

# group은 1 or -1로 visited에 자정됨/ 방문안했으면 visited는 0
def dfs(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장

    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            # -group : 현재 노드의 그룹과 다른 값 전달
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False
    return True


for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 그래프가 이어지지 않고 끊어져 있는 경우가 있을 수 있기 때문에 모든 노드에서 dfs 탐색 진행.
    for i in range(1, V+1):
        if visited[i] == 0:
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")