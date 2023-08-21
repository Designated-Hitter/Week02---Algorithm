import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[0] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A] = B

    