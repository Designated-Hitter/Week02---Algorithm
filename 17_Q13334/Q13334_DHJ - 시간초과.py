import sys
import heapq
N = int(sys.stdin.readline())

road_info = []
for _ in range(N):
    x = list((sys.stdin.readline().split()))
    #계산하기 편하게 출근 방향이 반대인 사람도 똑같이 바꿈
    if int(x[0]) > int(x[1]):    
        x = [x[1], x[0]]
    road_info.append(x)
d = int(sys.stdin.readline())

roads = [] #[출발점, 도착점]
for road in road_info:
    #애초에 거리가 d보다 멀어서 지하철을 이용할 수 없는 경우를 제외
    if abs(int(road[0]) - int(road[1])) <= d:
        #좌표정보를 오름차순으로 저장
        road = sorted(road)
        roads.append(road)
#철로의 시작점을 가장 작은것부터 할 수 있도록 roads를 본인의 원소 중 큰 원소를 기준으로 오름차순 정렬        
roads.sort(key = lambda x:x[1])

answer = 0
heap = []

for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        #철로의 시작점을 가장 작은것부터 순회하면서 heappush
        #이 때, heap에 존재하는 가장 작은 값이 철로의 끝 점안에 존재하는 지 확인해 철로 내에 있지 않다면 heappop
        while int(heap[0][0]) < int(road[1]) - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
