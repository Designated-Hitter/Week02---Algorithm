import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    array = list(input())

    stack = []
    flag = 0
    for j in range(len(array)):
        if array[j] == '(':
            stack.append(array[j])
        elif array[j] == ')':
            if len(stack) == 0:
                flag = 1
                break
            stack.pop()


    if len(stack) != 0 or flag == 1:
        print("NO")
    else:
        print("YES")