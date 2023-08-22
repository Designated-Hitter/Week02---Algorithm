import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort()
print(coins)