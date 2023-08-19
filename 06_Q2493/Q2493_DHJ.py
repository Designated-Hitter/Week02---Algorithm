import sys
N = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().split()))

stack = []
answer = [0] * N

for i in range(N):
    tower = towers[i]
    while stack and towers[stack[-1]] < tower: #직전에 stack에 저장된 탑의 높이가 현재 탑 보다 낮다면 stack을 버림
            stack.pop()
    if stack:
          answer[i] = stack[-1] + 1 #stack[-1]은 index이므로 +1
    stack.append(i)


print(' '.join(list(map(str, answer)))) #list 에 들어있는 숫자를 문자열로 -> map으로 나눠서 list로 -> list의 원소를 공백을 기준으로 한줄로

#문제를 이해하기 쉬운 형태로 바꿔서 생각하는게 중요했다.
#오른쪽으로 이동하면서 하나씩 탑을 볼 때 이전 탑의 높이가 현재 탑의 높이보다 낮다면 버리는 형식