import sys
input = sys.stdin.readline

n = int(input())

stack = [int(input())]

for i in range(n-1):
    h = int(input())
    if stack[-1] > h:
        stack.append(h)
        continue
    else:
        while len(stack) > 0:
            if stack[-1] <= h:
                stack.pop()
                continue
            else:
                break
        stack.append(h)

print(len(stack))