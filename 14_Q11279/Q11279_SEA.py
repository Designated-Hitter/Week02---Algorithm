import heapq

N = int(input())
nums = [int(input()) for _ in range(N)]

hq = []

for n in nums:
    if n == 0:
        if len(hq) == 0:
            print(0)
        else:
            val = heapq.heappop(hq)
            print(-val)
    else:
        # 파이썬 우선순위큐는 기본이 최소힙이라서 - 부호 붙여서 가장 작은게 pop되게 하고 사용할 때는 -를 붙여서 사용한다.
        heapq.heappush(hq, -n)

    