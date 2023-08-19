import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

def queue_func(order):
    if order[0] == 'push':
        queue.append(order[-1])
        return

    if order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
        return

    if order[0] == 'size':
        print(len(queue))
        return

    if order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
        return

    if order[0] == 'front':
        if len(queue) == 0:
            print(-1)
            return
        print(queue[0])
        return

    
    if order[0] == 'back':
        if len(queue) == 0:
            print(-1)
            return
        print(queue[-1])
        return


queue = deque()

for i in range(n):
    order = input().strip().split()
    queue_func(order)



