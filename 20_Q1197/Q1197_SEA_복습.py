"""
일단, 스패닝 트리라는 것은, 모든 정점이 하나의 간선으로 서로 연결되어 있는 걸 의미하고, 사이클이 없어야 한다.
이중에 최소 스패닝 트리는 이런 스패닝 트리들 중 간선의 합이 최소인 스패닝 트리를 말한다.
보통 최소 스패닝 트리를 구하기 위해 크루스칼 알고리즘을 사용하고, 크루스칼 알고리즘은 유니온파인드 기법을 이용해서 구현한다.
유니온 파인드는 각각 유니온, 파인드 이렇게 두 가지 함수가 필요한데, 유니온은 두 정점의 그룹을 하나로 합치는 것이고, 파인드는 해당 정점의 그룹을 구하는 것이다. 개념은 이렇고, 파인드를 할 때 최적화해주는 방법이 있는데, 그건 바로 파인드 결과를 그 경로에서 거쳐갔던 노드들의 그룹으로 할당해주는 것이다. 이렇게 하면 나중에 해당 정점의 그룹이 무엇인지 파인드를 했을 때 거슬러 올라가는 과정이 최소화되기 때문에 더 적은 시간이 걸린다. 마찬가지로, 유니온 과정에서도 랭크라는 배열을 도입할 수 있는데, 만약 랭크가 같은 정점이 합쳐져야 할 때, 임의로 한쪽의 랭크를 더 높이고, 나머지 정점의 그룹을 랭크가 높은 정점의 그룹으로 변경한다.
"""

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda edge: edge[2]) # 가중치를 기준으로 오름차순 정렬

weights = 0
groups = [0] * (V + 1)
ranks = [0] * (V + 1)

# 우선 초기 그룹은 자기 자신의 번호다.
for i in range(1, V + 1):
    groups[i] = i

def find(node):
    # 만약 자기 번호랑 그룹이랑 같으면 아직 합쳐지지 않았거나 가장 큰 그룹이기 때문에 바로 리턴해준다.
    if groups[node] == node:
        return node
        
    # 그 외에는 타고 올라간다.
    # 근데 끝까지 올라가서 얻은 최고그룹을 내려가면서 다 할당해준다.
    groups[node] = find(groups[node])
    return groups[node]


def union(node1, node2):
    # 지금 인자를 받을 때부터 다른 그룹끼리 합치는게 가정되어 있어서 바로 합쳐주면 된다.
    node1_group = find(node1)
    node2_group = find(node2)

    # 지금 더 큰 무리가 뭔지를 모르기 때문에 랭크 배열을 도입한다.

    # node1의 랭크가 더 크면 node2의 그룹을 node1의 그룹으로 옮기고 node2 랭크를 + 1 해준다.
    if ranks[node1_group] > ranks[node2_group]:
        groups[node2_group] = node1_group
    # 그 반대도 마찬가지로 수행한다.
    else:
        groups[node1_group] = node2_group

        # 만약 두 노드가 랭크가 같으면 한쪽을 임의로 잡아서 랭크를 높이고 랭크가 높은 쪽이 그룹이 된다.
        if ranks[node1_group] == ranks[node2_group]:
            ranks[node2_group] += 1

# 간선을 순회한다.
for edge in edges:
    u, v, w = edge

    # 두 정점의 그룹을 찾는다.
    u_group = find(u)
    v_group = find(v)

    # 그룹이 다르다면 같게 한다.
    if u_group != v_group:
        union(u_group, v_group)

        # 가중치를 추가한다.
        weights += w

    # 그룹이 같다면 패스한다.
    
print(weights)

    

