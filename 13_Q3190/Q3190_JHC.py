import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

apples = [list(map(int, input().split())) for _ in range(k)]

L = int(input())
directionChange = [input().split() for _ in range(L)]

while True:
    