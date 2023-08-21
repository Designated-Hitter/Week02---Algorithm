V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

parents = [0] * 10005
ranks = [0] * 10005 # 랭킹 매기는 배열. 높을수록 더 상위 그룹

for i in range(len(parents)):
    parents[i] = i
    ranks[i] = 0

def find(v):
    # 초기에는 정점은 각자 다른 그룹이라서 자기자신을 반환하도록 함.
    if parents[v] == v:
        return v
    
    # x의 부모의 부모의 이런식으로 계속 찾으러 가서 최고부모를 리턴해서 배열에 넣어주고 리턴.
    parents[v] = find(parents[v])
    return parents[v]

def is_diff_group(u, v):
    u = find(u)
    v = find(v)

    # 둘이 같은 그룹이면 False 리턴
    if u == v:
        return False
    
    # 다른 그룹이면 그룹 갱신하고 True 리턴
    if ranks[u] < ranks[v]:
        parents[u] = v
    else:
        parents[v] = u

        if ranks[u] == ranks[v]:
            ranks[u] += 1
    
    return True
    
edges.sort(key= lambda edge: edge[2])

cnts = 0
ans = 0

for i in range(len(edges)):
    u, v, w = edges[i]
    
    if is_diff_group(u, v): # 다른 그룹이면
        ans += w
        cnts += 1

        if cnts == V - 1:
            break

print(ans)
