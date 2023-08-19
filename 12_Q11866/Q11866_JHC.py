# from collections import deque

# n, k = map(int, input().split())

# seq = list(range(1, n+1))
# no = n
# front = 0
# rear = n-1

# removed = []

# while True:
#     target_idx = (front + k-1) % no 
#     removed.append(str(seq.pop(target_idx)))
#     front = target_idx 
#     rear = front - 1
#     no -= 1
#     if no == 0:
#         break

# print('<'+', '.join(removed)+'>')


N, K = map(int,input().split())

answer = []
arr = list(range(1,N+1))

idx = 0
for i in range(N):
    idx += (K-1)
    if idx >= len(arr):
        idx %= len(arr)
    answer.append(str(arr.pop(idx)))

print("<",', '.join(answer),">", sep="")
