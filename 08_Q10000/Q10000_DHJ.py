#서로 겹치지 않는 원 N개일 때, 만들어지는 영역은 N + 1개
#만약 서로 맞닿는 경우라면 겹치는 원 당 영역 1개 ++ (즉, N + 2개)
#맞닿는 원의 판단
#각기 다른 원의 x-r, x+r이 각각 겹치는 큰 원이 존재하며, C1(x-r) == C3(x-r) and C2(x+r) == C3(x+r)
#두 원의 X-r과 X+r이 같을 경우 즉, C1(x + r) == C2(x - r)
#stack 에 임의의 (x1 + r1) 값을 넣은 후, (x2 - r2)와 일치하는 지 탐색
#만약 일치한다면, (x1 - r1) 과 (x2 + r2) 를 가지는 리스트가 있는지 탐색
#있을 때 마다 count += 1

#--------
import sys
from bisect import bisect_left

def next_circle(curr_c, next_c):
    global count
    if circles[curr_c][1] == circles[next_c][1]:
        count += 1
        return
    temp = bisect_left(circles,(circles[next_c][1],))
    if temp == len(circles):
        return
    if circles[temp][0] == circles[next_c][1]:
        next_circle(curr_c, temp)


input = sys.stdin.readline().strip()
N = int(input)
#print(N)

circles = []

count = 0

for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append([x-r, x+r])

circles.sort( key = lambda x:( x[0], -x[1])) #정렬기준: 원의 왼쪽 점은 오름차순, 원의 왼쪽 점이 같을 경우 원의 오른쪽 점은 내림차순. 즉 원이 큰 순서대로 정렬된다.

for i in range(N-1):
    if circles[i][0] == circles[i+1][0]:
        next_circle(i, i+1)

print(N + count + 1)
