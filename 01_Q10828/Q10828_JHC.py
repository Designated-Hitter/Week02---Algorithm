import sys
input = sys.stdin.readline


n = int(input())

def stack_func(order):
    if order[0] == 'push':
        stack.append(order[-1])
        return

    if order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        return

    if order[0] == 'size':
        print(len(stack))
        return

    if order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        return

    if order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        return

stack = []

for i in range(n):
    order = input().strip().split()
    stack_func(order)
