from collections import deque
N = int(input())
q = deque([])

for i in range(1, N + 1):
    q.append(i)    

while len(q) >= 2:
    q.popleft()
    val = q.popleft()
    q.append(val)

print(q[0])