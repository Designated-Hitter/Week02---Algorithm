from collections import deque
N = int(input())
q = deque([])
res = []

for _ in range(N):
    user_input = input().split()
    cmd = user_input[0]

    if cmd == "push":
        q.append(int(user_input[1]))
    
    elif cmd == "pop":
        if len(q) != 0:
            val = q.popleft()
            res.append(val)
        else:
            res.append(-1)
    
    elif cmd == "size":
        res.append(len(q))
    
    elif cmd == "empty":
        if len(q) != 0:
            res.append(0)
        else:
            res.append(1)
    
    elif cmd == "front":
        if len(q) != 0:
            res.append(q[0])
        else:
            res.append(-1)
    
    else:
        if len(q) != 0:
            res.append(q[-1])
        else:
            res.append(-1)
for n in res:
    print(n)