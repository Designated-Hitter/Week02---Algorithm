import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

heap = []

leftHeap = []
rightHeap = []

for i in range(n):
    x = int(input())
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, (-x, x))
    else:
        heappush(rightHeap, (x, x))

    if len(leftHeap) >= 1 and len(rightHeap) >= 1 and leftHeap[0][1] > rightHeap[0][1]:
        max_value = heappop(leftHeap)[1]
        min_value = heappop(rightHeap)[1]
        heappush(leftHeap, (-min_value, min_value))
        heappush(rightHeap, (max_value, max_value))
    print(leftHeap[0][1])