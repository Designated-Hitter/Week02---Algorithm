#검은 벽을 통과할 때 마다 비용 카운트를 +1 올리고 끝에 도착 했을 때 통과한 검은 벽의 수(비용)를 계산하는 다익스트라 알고리즘
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(input().strip()))

print(maze)