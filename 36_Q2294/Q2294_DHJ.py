import sys

input = sys.stdin.readline

n, k = map(int, input().split()) #n = 동전의 종류, k = 만들려고 하는 가치
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
coins.sort()

dp = [10001] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])