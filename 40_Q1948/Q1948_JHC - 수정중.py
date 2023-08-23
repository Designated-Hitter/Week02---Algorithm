import sys
from collections import deque

input = sys.stdin.readline

'''
임의의 특정 정점까지 최장경로(최대 비용)를 구하는 법을 구현.
(출발점에서 그 정점까지 갈 때 비용 + 도착점에서 역으로 그 정점까지 갈 때 비용)이
첫번째 출력값인 최대 비용과 동일하면, 그 정점은 우리가 지날 도시인 것 맞음.
'''

# n : 도시의 개수, m : 도로의 개수
n = int(input())
m = int(input())

graph = [[] * (n + 1) for _ in range(n + 1)]    # 정방향
back_graph = [[] * (n + 1) for _ in range(n + 1)]   # 역방향

indegree = [0] * (n + 1)    # 진입차수
visited = [0] * (n + 1)     # 역방향(백트래킹)시 큐에 중복 삽입 방지
result = [0] * (n + 1)  # 각 도시로 이동하는 임계 경로 저장을 위한 변수

# graph[출발 도시] = (도착 도시, 걸리는 시간)
# back_graph[도착 도시] = (출발 도시, 걸리는 시간)
# 진입 차수 초기화
for _ in range(m):
    start_city, target_city, weight = map(int, input().split())
    graph[start_city].append((target_city, weight))
    back_graph[target_city].append((start_city, weight))
    indegree[target_city] += 1

start, target = map(int, input().split())

queue = deque()
queue.append(start)

# 위상 정렬
def topology_sort():
    while queue:
        now = queue.popleft()
        for next, weight in graph[now]:
            # 현재 도시를 거쳐가느데 걸리는 시간과 이전의 다른 경로의 걸리는 시간을
            # 비교하여 큰 값을 임계 경로로 설정
            result[next] = max(result[next], result[now] + weight) 
            indegree[next] -= 1
            # 위상 정렬 수행 과정에서 진입차수가 0인 도시 발생시 큐에 삽입
            if indegree[next] == 0:
                queue.append(next)

    # 백트래킹
    queue.append(target)
    count = 0

    while queue:
        now = queue.popleft()
        for pre, weight in back_graph[now]:
            # ( 현재 도시까지의 임계경로 ) 과 
            # ( 현재 도시에서 인접한 도시까지의 임계 경로 + 현재 도시의 인접 도시에서 현재 도시로 이동하는데 걸리는 시간 )
            # 이 같으면 그 인접 도시는 임계 경로의 한 도시이다.
            if result[now] == result[pre] + weight:
                count += 1
                # 임계 경로의 도로 중복 카운트 방지
                if visited[pre] == 0:
                    queue.append(pre)
                    visited[pre] = 1
                    
    # 결과 출력
    print(result[target])
    print(count)

topology_sort()