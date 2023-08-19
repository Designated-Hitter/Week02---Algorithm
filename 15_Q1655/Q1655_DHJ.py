import sys
import heapq

N = int(sys.stdin.readline())
heap = []

answer = []
for _ in range(N):
    x = int(sys.stdin.readline())
    
    heapq.heappush(heap, x)
    print('heap_now')
    print(heap)
    if len(heap) % 2 == 0:
        mid_value_index = (len(heap) // 2) - 1
    else:
        mid_value_index = len(heap) // 2
    mid_value = heap[mid_value_index]
    print('mid value')
    print(mid_value)
    answer.append(mid_value)

print(answer)