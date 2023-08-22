import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []
for _ in range(N):
    line = list(map(int, input().split()))
    box.append(line)
print(box)
deck = []
