import sys
N = int(sys.stdin.readline())
command_list = []
for i in range(N):
    command_list.append(list((sys.stdin.readline().split())))

stack = []
for command in command_list:
    if len(command_list) == 2:
        command[1] = int(command[1])
    if command[0] == 'push':
        stack.append(command[1])
    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            result = stack.pop()
            print(result)
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

#메모리: 33300KB
#시간: 56ms

