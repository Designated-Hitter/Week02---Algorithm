from collections import deque

N, K = map(int, input().split())
q = deque([])
vis = [False] * (N + 1)
for i in range(1, N + 1):
    q.append(i)

ptr = 0
remained = K
ans = []
while len(ans) < N:
    # vis[ptr%N] = True 이면 remained 감소 안하고 False면 감소하면서 ptr += 1
    # remained = 1이었는데 False 방문했으면 거기 두기
    if vis[ptr % N]:
        ptr += 1
    else:
        if remained == 1:
            vis[ptr % N] = True
            ans.append(ptr % N + 1)
            remained = K
        else:
            remained -= 1
            ptr += 1

print("<", end='')
for n in ans[:-1]:
    print(n, end=', ')
print(ans[-1], end='>')

            
    
