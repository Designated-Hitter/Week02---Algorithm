from collections import deque

stack = deque()
N = int(input())
# stack = []
inputs = [input().split() for _ in range(N)]

for i in range(len(inputs)):
    cmd = inputs[i][0]



    if cmd == "push":
        stack.append(int(inputs[i][1]))
    elif cmd == "pop":
        if len(stack) != 0: # 스택에 차 있으면 출력
            num = stack.pop()
            print(num)
        else: # 없으면 -1 출력
            print(-1)
    elif cmd == "top":
        if len(stack) != 0: # 스택에 차 있으면 출력
            print(stack[-1])
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    else: # empty
        if len(stack) == 0: # 비어 있으면 1
            print(1)
        else: # 차 있으면 0
            print(0)
