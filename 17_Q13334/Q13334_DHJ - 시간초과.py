import sys
import heapq
N = int(sys.stdin.readline())

home_n_office = []
for _ in range(N):
    x = list((sys.stdin.readline().split()))
    #계산하기 편하게 출근 방향이 반대인 사람도 똑같이 바꿈
    if int(x[0]) > int(x[1]):    
        x = [x[1], x[0]]
    home_n_office.append(x)
d = int(sys.stdin.readline())

possible_commuter = [] #[출발점, 도착점]
for i in home_n_office:
    #애초에 거리가 d보다 멀어서 지하철을 이용할 수 없는 경우를 제외
    if abs(int(i[0]) - int(i[1])) <= d:
        heapq.heappush(possible_commuter,([int(i[0]), int(i[1])])) #시작점 기준으로 heappush

departure_point = []
for possible in possible_commuter:
    departure_point.append(possible[0])
    departure_point = list(set(departure_point)) #출발 가능한 지점의 중복 삭제

answer = [0]

#이중for문을 어떻게 줄이기만 하면 될거 같음
#근데 이걸 어떻게 줄임
for point in departure_point:
    count = 0
    for commuter in possible_commuter:
        if point <= commuter[0] and point + d >= commuter[1]:
            count += 1
    answer.append(count)

# print(f'answer = {answer}')
print(max(answer))
# print(f'N = {N}')
# print(f'home_n_office = {home_n_office}')
# print(f'possible_commuter = {possible_commuter}')
# print(f'departure_point = {departure_point}')
# print(f'd = {d}')
