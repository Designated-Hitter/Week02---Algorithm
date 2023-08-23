from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
coins.sort()
visited = [0]*(k+1)  # 방문 시 1, 미방문 시 0


queue = deque()

for coin in coins:
    if coin > k:
        continue
    queue.append((coin, 1))   # (현재까지의 총합, 동전 개수 총합)
    visited[coin] = 1

flag = False   # bfs 다 마치고 난 후에도 False이면 해당 합을 만들 수 없는 것이므로 -1 출력
while queue:
    val, cnt = queue.popleft()
    if val == k:
        print(cnt)
        flag = True
        break
    
    for coin in coins:
        if val + coin > k:
            continue
        # 해당 합에 한번도 방문한 적이 없을 경우(최단 개수를 구하기 위해)
        if visited[val + coin] == 0:
            queue.append((val + coin, cnt + 1))
            visited[val + coin] = 1

if not flag:
    print(-1)

# from sys import stdin

# n, k = map(int, stdin.readline().split())

# li =[]

# for i in range(n):
#    li.append(int(stdin.readline().rstrip()))

# dp = [10001] * (k+1)
# dp[0] = 0

# for num in li:
#    for i in range(num, k+1):
#        dp[i] = min(dp[i],dp[i-num]+1)
# if dp[k] == 10001:
#    print(-1)
# else:
#    print(dp[k])
