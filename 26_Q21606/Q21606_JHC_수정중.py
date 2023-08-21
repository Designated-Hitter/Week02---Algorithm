import sys
input = sys.stdin.readline

n = int(input())
group_lst = [-1] + list(map(int, input().rstrip()))    # 0:실외/ 1:실내


graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start, visited, group, start_idx):
    global cnt
    if start != start_idx and group == 1:
        cnt += 1
        return True

    visited[start] = group

    for v in graph[start]:
        if visited[v] == -1:
            result = dfs(v, visited, group_lst[v], start_idx)
            if not result:
                return False
            print(v, end = ' ')

        else:
            continue
    
    return True

cnt = 0
for i in range(1, n+1):
    if group_lst[i] == 1:
        visited = [-1] * (n+1)
        start_idx = i
        result = dfs(i, visited, group_lst[i], start_idx)
        if not result:
            continue
        print(i, end=' ')
        print()

# print(cnt)