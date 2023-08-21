from collections import deque

K = int(input())

def solve():
    global V, E, graph, groups


    # 지금 문제에서 모든 정점이 서로 연결되어 있다고 하지 않았기 때문에, 모든 정점을 순회해야 한다.
    for i in range(1, V + 1):
        if groups[i] != -1:
            continue
 
        q = deque()
        q.append(i)
        groups[i] = 0 # 0이나 1중 아무나 줘도 되는 이유는, 다시 여기까지 오게 되는 경우는 노드간 서로 연결되어 있지 않은 다른 영역일 것이므로, 나머지 영역과 연결된 것이 없어서 그렇다.

        while q:
            cur = q.popleft()

            for nxt in graph[cur]:
                # 아직 그룹화 안됐으면 그룹화해주고 큐에 넣기.
                if groups[nxt] == -1:
                    groups[nxt] = (groups[cur] + 1) % 2
                    q.append(nxt)
                
                # 그룹화 됐었을 경우
                else:
                    # cur과 nxt가 같은 그룹이면 False 리턴
                    if groups[cur] == groups[nxt]:
                        return False
                    
                    # 다른 그룹인 경우 그냥 패스
                    else:
                        continue
        
    return True

for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u) # 얘를 깜빡했다.

    groups = [-1] * (V + 1)
    
    if solve():
        print("YES")
    else:
        print("NO")