# import heapq

# N = int(input())
# # hq1 = []
# hq = []

# for i in range(N):
#     n = int(input())
#     heapq.heappush(hq, n)

#     mid = len(hq) // 2

#     if len(hq) % 2 == 0: # 짝수라면
#         print(min(hq[mid - 1], hq[mid]))
#     else: # 홀수라면
#         print(hq[mid])    


import sys, heapq
input = sys.stdin.readline
N = int(input())
max_hq = []
min_hq = []

for _ in range(N):
    num = int(input())

    # 맥스힙 민힙 크기가 같으면 맥스힙에 넣기
    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, -num)
    
    # 맥스힙이 더 크면 민힙에 넣기
    elif len(max_hq) > len(min_hq):
        heapq.heappush(min_hq, num)

    # 맥스힙 탑이랑 민힙 탑이랑 비교해서 맥스힙 탑이 더 크면 민힙탑이랑 교체
    # 왜? 항상 맥스힙 탑보다 민힙 탑이 커야 맥스힙에서 탑을 제외한 나머지 수의 개수 == 민힙 내 수의 개수일 때 맥스힙 탑이 중간값이 되기 때문

    if len(min_hq) > 0 and -max_hq[0] > min_hq[0]:
        max_top = heapq.heappop(max_hq)
        min_top = heapq.heappop(min_hq)

        heapq.heappush(max_hq, -min_top)
        heapq.heappush(min_hq, -max_top)
    
    print(-max_hq[0])
