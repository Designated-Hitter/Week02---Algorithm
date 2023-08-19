T = int(input())
V, E, graph = 0, 0, 0
group = [-1] * 20002

def solve():
    global V, E, graph, group
    
    # 배열 초기화
    for i in range(1, V + 1):
        group[i] = -1
    
    for i in range(1, V + 1):
        if group[i] != -1:
            continue

        q = []
        q.append(i)
        group[i] = 0

        while q:
            cur = q.pop()

            for nxt in graph[cur]:
                if group[nxt] != -1:
                    if group[nxt] == group[cur]:
                        return False
                    else:
                        continue
            
                group[nxt] = (group[cur] + 1) % 2
                q.append(nxt)

    return True
    
for _ in range(T):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if solve():
        print("YES")
    else:
        print("NO")

    
        

        
            
    


    

    
    