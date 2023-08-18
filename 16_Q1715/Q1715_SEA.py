import heapq

N = int(input())
nums = [int(input()) for _ in range(N)]
hq = []
cnts = 0

for n in nums:
    heapq.heappush(hq, n)

while len(hq) > 1:
    n1 = heapq.heappop(hq)
    n2 = heapq.heappop(hq)
    
    heapq.heappush(hq, n1 + n2)
    cnts += n1 + n2

print(cnts)
    

