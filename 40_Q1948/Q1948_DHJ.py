#출발 -> 도착 가중치
#가장 오래 걸리는 경로
#가장 오래 걸리는 경로가 몇 개 인지

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 도로의 개수

time = [0] * (N + 1)
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
bgraph = [[] for _ in range(N+1)]    # backward of graph
cnt = [[] for _ in range(N+1)]