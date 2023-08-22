import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(input().strip()))

print(maze)