import heapq

N = int(input())
lines_temp = [list(map(int, input().split())) for _ in range(N)]
d = int(input())

lines = []
for line in lines_temp:
    h, o = line
    
    if abs(h - o) <= d:
        if h > o:
            line.reverse()

        lines.append(line)

lines.sort(key= lambda x: x[1]) # 끝점 기준 오름차순 정렬

hq = []
ans = 0

for line in lines:
    # 철로의 시작점이 선의 시작점보다 크면 포함 안되니까 없애주기
    # 철로의 끝을 line 끝에 딱 맞춘 상태
    # lines는 끝점이 작은거일수록 앞에 있기 때문에 힙에 있는 선들은 다 철로보다 끝점이 앞에 있음. 그래서 현재 line 끝에 딱 맞춘다음 시작점만 비교해주면 된다. 힙은 시작점이 작을수록 먼저 튀어나오기 때문에 while 조건문이 false인 순간부터
    # 선의 시작점은 철로의 시작점보다 같거나 크고, 선의 끝점은 철로의 끝점보다 같거나 작게 된다.

    while hq and hq[0][0] < line[1] - d: 
        heapq.heappop(hq)
    heapq.heappush(hq, line) # 지금 보고 있는 선 넣기

    ans = max(ans, len(hq))

print(ans)



    
            
# # 확인하다가 철로 시작점보다 라인 시작점이 바깥에 있으면 그냥 가고 안에 있으면 다시 넣기
# for line in lines: # 라인 순회하면서 대보기
#     cnts = 1

#     saved = []
#     while hq: # 힙큐에 선 있으면
#         cur = heapq.heappop(hq) # 하나 빼내서
        
#         # 철로 안쪽에 있나 확인
#         if cur[1] >= line[1] - d:
#             cnts += 1 # 있으면 추가
#             saved.append(cur)
#         # 안쪽에 없으면 힙에 뭐있나 더이상 안봐도 됨. 
#         else:
#             break
        
#     ans = max(ans, cnts)    
#     heapq.heappush(hq, (line[1], line[0])) # 지금 라인 추가하고

#     # 조건 만족했던거 다시 넣기
#     for save in saved:
#         heapq.heappush(hq, save)
    
