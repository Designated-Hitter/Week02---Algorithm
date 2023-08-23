import heapq
import sys

'''
이 문제의 핵심은
"답이 여러 개일 경우에는 사전 순으로 제일 앞서는 것을 출력한다."
## 최소힙 사용시 반례
4
0011
0000
0000
0100

오답: 1 4 2 3
정답: 1 3 4 2
##

indegree 아닌 outdegree 사용해서 answer의 배열을 1부터 넣지말고 n부터 넣기
-> 간선방향 뒤집어주기
'''


input = sys.stdin.readline

def topology_sort():
  q = []
  for i in range(1, n+1):
    if indegree[i] == 0:
      # heapq.heappush(q,i)
      # 최대힙
      heapq.heappush(q,-i)
  
  N = n
  while q:
    now = -heapq.heappop(q)
    answer[now] = N
    
    for i in node[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(q, -i)
    # N+=1
    N -=1

n = int(input())
node = [[] for _ in range((n+1))]
indegree = [0] * (n+1)

# 인접행렬 입력 ->인접리스트로 변경
for v in range(1, n+1):
  temp = [0]+ list(map(int, input().strip()))
  for i in range(1, n+1):
    if temp[i] == 1:
      node[i].append(v)
      indegree[v] += 1

answer = [0]*(n+1)

topology_sort()
if answer.count(0) > 1:
  print(-1)
else:
  print(*answer[1:])