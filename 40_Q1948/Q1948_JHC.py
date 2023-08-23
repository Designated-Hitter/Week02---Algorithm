
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 도로의 개수

time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
bgraph = [[] for _ in range(N+1)]    # backward of graph
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    # a: 출발 도시, b: 도착 도시, c: 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    bgraph[b].append(a)
    in_degree[b] += 1

src, dst = map(int, input().split())

q = deque([])
# 도시, 지나온 경로 개수
q.append(src)

while q:
    # now: 도시, c: 지나온 경로의 개수
    now = q.popleft()
    # i[0]: 비용, i[1]: 도시
    for i in graph[now]:
        in_degree[i[1]] -= 1
        # 비용이 갱신 될 때
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            # 달려야 하는 도로의 수 갱신
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        # 선행 도로를 모두 지나갔을 때
        if in_degree[i[1]] == 0:
            q.append(i[1])

q = deque([dst])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[dst])
print(len(route))

# import sys
# from collections import deque
# sys.stdin = open("input.txt","r")
# n=int(input()) #노드, 도시 개수
# m=int(input()) #도로의 개수
# graph=[[]*(n+1) for _ in range(n+1)]
# back_graph=[[]*(n+1) for _ in range(n+1)]
# indegree=[0]*(n+1) #진입차수
# result=[0]*(n+1)
# check=[0]*(n+1)
# q=deque()
# for _ in range(m):
#     a,b,t=map(int,input().split())
#     graph[a].append((b,t))
#     back_graph[b].append((a,t))
#     indegree[b]+=1
# start,end=map(int,input().split())

# q.append(start)

# def topologysort():
#     while q:
#         cur=q.popleft()
#         for i,t in graph[cur]:
#             indegree[i]-=1
#             result[i]=max(result[i],result[cur]+t)
#             if indegree[i]==0:
#                 q.append(i)

#     #백트래킹
#     cnt=0 #임계경로에 속한 모든 정점의 개수
#     q.append(end)
#     while q: #도착점에서 시작점으로
#         cur=q.popleft()
#         for i,t in back_graph[cur]:
#             #도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면
#             if result[cur]-result[i]==t:
#                 cnt+=1
#                 if check[i]==0: #큐에 한번씩만 담을 수 있도록,중복방문제거 
#                     q.append(i)
#                     check[i]=1

#     print(result[end])
#     print(cnt)

# topologysort()

''''''
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# indegree = [0]*(n+1)
# graph = [[] for i in range(n+1)]


# for _ in range(m):
#     s, e, w = map(int, input().split())
#     graph[s].append((e, w))
#     indegree[e] += 1

# def topology_sort():
#     result = 