import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []

answer = []
for _ in range(N):
    x = int(sys.stdin.readline())
    
    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, (-x, x))
    else:
        heapq.heappush(max_heap, (x, x))

    if max_heap and min_heap[0][1] > max_heap[0][0]:
        min = heapq.heappop(max_heap)[0]
        max = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (-min, min))
        heapq.heappush(max_heap, (max, max))

    answer.append(min_heap[0][1])

for j in answer:
    print(j)