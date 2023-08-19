import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple_list = []
for _ in range(K):
    apple_list.append(list(sys.stdin.readline().split()))

print(apple_list)
L = int(sys.stdin.readline())
turn_list = []
for _ in range(L):
    turn_list.append(list(sys.stdin.readline().split()))
print(turn_list)