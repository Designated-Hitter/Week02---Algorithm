N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

normals = []

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for i in range(1, N + 1):
    if not graph[i]:
        normals.append(i)

"""
우선 완제품으로부터 뻗어나가는 모양으로 그래프를 만든다.
그리고 dfs로 돌면서 필요한 기본 부품이 개수를 구해서 배열에 저장한다. 
기본 부품은 outdegree가 없는 노드다.
"""
cnts = [0] * (N + 1)

# 인자에 부품 번호가 들어감.
def dfs(toy_number, added):
    # 기본 부품이면 리턴
    if not graph[toy_number]:
        cnts[toy_number] += added
        return

    # 해당 toy_number 부품을 만드는 데 필요한 기본 부품의 개수
    
    # 기본 부품이 아니면 해당 부품의 서브 부품들을 순회한다.
    for nxt in graph[toy_number]:
        # dfs 결과에 필요한 개수를 구한다.
        dfs(nxt[0], added * nxt[1])

dfs(N, 1)

for idx in normals:
    print(f"{idx} {cnts[idx]}")
    