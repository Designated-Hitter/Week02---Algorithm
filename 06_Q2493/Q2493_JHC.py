n = int(input())
tower_heights = list(map(int, input().split()))

reception = ['0']*n
# stack에는 idex가 들어감
stack = [0]

'''
reception = ['0','0','2','0','0']
stack = [1, ]
'''

for i in range(1, n):

    while tower_heights[stack[-1]] < tower_heights[i]:
        stack.pop()
        if len(stack) == 0:
            break

    if len(stack) != 0:
        reception[i] = str(stack[-1]+1)
    stack.append(i)

print(' '.join(reception))