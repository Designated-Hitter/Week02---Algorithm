# 6분
from collections import deque

N, K = map(int, input().split())

ans = []

q = deque()
for i in range(1, N + 1):
    q.append(i)

remained = K
while q:
    cur = q.popleft()
    remained -= 1

    if remained == 0:
        ans.append(cur)
        remained = K
    
    else:
        q.append(cur)
print('<', end = '')

for i in range(len(ans) - 1):
    print(ans[i], end = ', ')
print(ans[-1], end='')
print('>')