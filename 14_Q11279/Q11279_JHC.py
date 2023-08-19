import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
heap = []
max_hq = []


for _ in range(n):
    n = int(input())
    if n == 0:
        if len(heap) == 0:
            max_hq.append(0)
            continue
        max_hq.append(heappop(heap)[1])
        continue
    heappush(heap, (-n, n))

for i in range(len(max_hq)):
    print(max_hq[i])