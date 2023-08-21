import sys
from collections import deque
N = int(sys.stdin.readline())
num_list = deque()

for i in range(N):
    command = list((sys.stdin.readline().strip().split(" ")))
    if command[0] == 'push':
        num_list.append(command[1])
    elif command[0] == 'pop':
        if len(num_list) <= 0:
            print(-1)
        else:
            pop_value = num_list.popleft()
            print(pop_value)
    elif command[0] == 'size':
        print(len(num_list))
    elif command[0] == 'empty':
        if len(num_list) <= 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(num_list) <= 0:
            print(-1)
        else: 
            print(num_list[0])
    elif command[0] == 'back':
        if len(num_list) <= 0:
            print(-1)
        else: 
            print(num_list[-1])
            
#메모리: 175092 KB
#시간: 1892 ms

