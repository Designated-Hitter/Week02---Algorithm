import heapq

n = int(input())
circles = []

for _ in range(n):
    c, r = map(int, input().split())
    end = c + r
    dia = 2 * r
    circles.append((end, dia)) # 원 리스트에 (끝점, 지름)

circles.sort() # 끝점기준 오름차순, 지름기준 오름차순. 끝점이 왼쪽에 있는거부터, 끝점 같을 시 작은 원부터

h = [] # 우선순위큐 생성
cnts = 1

for i in range(n):
    end, dia = circles[i]

    start = end - dia # 시작점
    can_fill = False # 해당 원 내부를 채울 수 있는지 유무
    last_point = end # 초기 끝점을 자신의 끝점으로 잡음

    while h: # 우선순위 큐 빌 때까지 반복
        prev_end, prev_dia = heapq.heappop(h) # 원 하나 뽑는다. 이 원은 우큐에 있는 원 중에서 가장 끝점이 오른쪽에 있는 원이다.
        prev_end = -prev_end # 원래값으로 변경

        if prev_end <= start: # i번째 원은 prev보다 바깥에 있음. 처음에 원을 끝점기준 오름차순 정렬했기 때문에 prev의 오른쪽에 위치함.
            heapq.heappush(h, [-prev_end, prev_dia])
            break

        # 이제 i번째 원의 시작점은 < prev_end
        # 근데 prev_end랑 last_point랑 다르면 접하지는 않는 상황임.
        if prev_end != last_point and prev_end - prev_dia >= start: # 
            continue

        # 이제 내부에서 접하는지 확인
        if prev_end - prev_dia >= start: # i번째 원의 start보다 prev원의 start가 더 크면 
            last_point = prev_end - prev_dia # prev의 왼쪽점을 확인해야할 last_point로 갱신

        if last_point == start: # 끝점 위에서 계속 갱신하다가 start 도달했으면 i번째원 내부를 원으로 다 채울 수 있는 것.
            can_fill = True
    
    cnts += 1 # 우선 원 그리면 무조건 +1 됨
    
    if can_fill: # 원 내부를 채울 수 있으면 +1
        cnts += 1
    
    heapq.heappush(h, [-end, dia]) # 파이썬 우선순위큐는 기본이 최소힙이라 end에 - 붙여서 최대힙으로 변경.

print(cnts)
