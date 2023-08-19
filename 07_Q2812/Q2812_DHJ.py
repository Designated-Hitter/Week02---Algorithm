import sys
N, K = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().strip()))

stack = []

for number in numbers:
    while stack and stack[-1] < number and K > 0:
        stack.pop()
        K -= 1
    stack.append(number)
if K > 0:
    print(''.join(list(map(str, stack[:-K]))))
else:
    print(''.join(list(map(str, stack))))