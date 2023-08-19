'''
주어진 데이터에서 각 원의 왼점과 오른점을 구한다.
왼점부터 오름차순으로 정렬해서 원이 완성되는 시점에 영역의 개수를 증가시킨다.
원이 하나 만들어질 때마다 원의 안/밖이 분리되어, 영역이 1 증가한다.
원 안에 원들이 꽉 찰 경우에는, 원의 안/밖 말고도 위 아래도 분리되므로 영역이 2 증가한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
circles = []

# 1. 각 원의 왼점과 오른점을 구한다.
for _ in range(n):
    x, r = map(int, input().split())
    # '왼점인지 오른점인지 여부'와 '점의 위치'를 저장
    circles.append(("L", x-r))
    circles.append(("R", x+r))


# 2. 원의 점들을 정렬한다.
# <정렬의 기준>
# 1순위) 점의 위치를 오름차순으로 정렬
# 2순위) 점의 위치가 같을 경우, 오른점 R이 왼점 L보다 앞으로 오도록 정렬
# 원 두개가 맞닿아 있는 경우, 왼점과 오른점의 위치가 동일하다. 이때 왼쪽 원을 먼저 완성시키고 오른쪽 원을 계산해야 하므로,
# 오른쪽 점 R이 먼저 오도록 정렬하는 것이다.

# 오른점 R이 왼점 L보다 앞으로 오도록 정렬
circles.sort(key=lambda x: (x[0]), reverse=True)
# 왼점부터 오름차순으로 정렬 (이게 1순위라 뒤에 하는것)
circles.sort(key=lambda x: x[1])


# 3. 왼점의 정보를 stack에 담아둔다.
# 왼점은 원의 시작을 의미
# 이후 반복을 돌면서 오른점을 만나면 원이 완성된다.
# 이후에 만날 오른점을 위하여 stack에 담아둔다.

stack = []  # 왼점과 완성된 원의 정보를 담을 스택
count = 1   # 영역 개수

for circle in circles:
    # 현재 점이 왼점인 경우들만, stack에 담아둔다.
    if circle[0] == 'L':
        stack.append(circle)
        continue

    #### 현재 점이 '오른쪽 점'인 경우에만 아래 코드 수행 ####

    # 4. 왼점이 아닌 경우, 원을 완성시킨다.
    # circles를 돌면서 나오는 circle[0]이 L이 아닌 경우는 (else)
    # circle[0]이 R을 의미하며, 이때 가장 최근에 만난 L로 시작한 원이 완성된다. () -> 원은 교차 불가하므로 가장 최신(가장 가까운) L부터 만나야됨.

    # stack에 값이 있다는 것은, 현재 원이 시작되고 나서 아직 원이 닫히지 않았음을 의미.
    # 그러므로 stack의 요소가 있으면 실행하도록 while문 작성!

    # 현재 열린 원 안에 원이 들어있을 경우, 그 원들의 너비를 전부 더해서 담을 변수
    # -> 이게 현재 원의 크기와 같으면 현재 원을 꽉 채우고 있으므로 count를 2 증가시켜줄 예정
    total_width = 0

    while stack:
        # 스택에 가장 최근에 쌓인 것 꺼내서 이전 요소를 의미하는 prev에 담아둔다.
        prev = stack.pop()

        # 가장 최근에 만난 L을 스택에서 꺼낸다면 원이 완성된다.
        # L을 꺼낸 경우 == 스택에서 꺼낸 게 왼쪽 점인 경우 -> 원이 만들어짐
        if prev[0] == "L":

            # 원의 너비 = 현재 점(오른쪽 점) - 이전 점(왼쪽 점)
            width = circle[1] - prev[1]
            
            # (5번은 맨 밑에..)
            # 6. 현재 원을 작은 원들이 가득 채우고 있는지 확인한다.
            # 현재 만들어진 원의 지름이 이전의 원들 지름의 합과 같을 경우
            # 현재 원을 꽉 채우고 있으므로 count를 2 증가
            if total_width == width:
                count += 2
            # 다를 경우, count 1 증가 (원이 만들어져 안/밖으로 영역이 증가했으므로)
            else:
                count += 1

            # 원이 만들어졌으므로 stack에 원을 의미하는 C와 너비 추가
            stack.append(("C", width))

            # 원이 닫히면 다음으로 넘어간다.
            # 지금 원을 추가했기 때문에 stack에 값이 있어서 break를 안해주면 탈출하지 못한다!!
            break
        
        
        # 5. stack에서 원을 꺼낸 경우, 너비를 검증한다.
        # stack에서 원을 꺼낸 경우, 현재 원 안에 원이 또 존재하는 것을 의미.
        # 현재 원 안에 있는 원이 여러개인 경우, 이 원들이 현재 원을 가득 채우고 있는지 확인해야함. (6번에서 할 예정)
        # 현재 원을 가득 채우고 있는지 검증할 때 사용하기 위해 원을 꺼낼 때마다(stack에서 C를 꺼낼 때마다) total_width에 꺼낸 원의 width를 추가한다.

        # C를 꺼낸 경우 == 스택에서 꺼낸 게 원인 경우 -> 현재 원 안에 존재하는 원을 의미
        elif prev[0] == "C":
            total_width += prev[1]

print(count)



# # 원이 들어오는 모양을 괄호로 변환하여 공간 계산
# import sys

# input = sys.stdin.readline

# n = int(input())
# circles = []

# # 원의 왼쪽은 '(' 모양의 괄호 오른쪽은 ')' 모양의 괄호로 만든다.
# for i in range(n):
#   x, r = map(int, input().split())
#   circles.append((x-r, '('))
#   circles.append((x+r, ')'))

# # 좌표기준으로 오름 차순으로 정렬하되 좌표가 같으면 ')'모양이 앞에 오게 정렬한다.
# circles = sorted(circles, key= lambda x:(x[0], -ord(x[1])))

# stack = []
# # 스택에는 좌표, 괄호 모양, 상태값이 들어감
# answer = 1
# for i in range(n*2):
#   position, bracket = circles[i]
#   if len(stack) == 0:
#     stack.append({'pos':position,'bracket':bracket,'status':0})
#     continue
  
#   # status 0: 기본값 ->
#   # status 1: 원 안의 원이 연결 되어 있는 지 확인
#   # 괄호가 닫히면 status 값을 확인하고 0 이면 +1 1이면 +2
#   if bracket == ')':
#     if stack[-1]['status'] == 0:
#       answer +=1
#     elif stack[-1]['status'] == 1:
#       answer +=2
#     stack.pop()
#     # 원이 이어져 있는지 확인
#     if i != n*2-1:
#       if circles[i+1][0] != position:
#         stack[-1]['status'] = 0
#   else:
#     if stack[-1]['pos'] == position:
#       # 좌표값이 같으면 원이 접해있는 상태
#       stack[-1]['status'] = 1
#       stack.append({'pos':position,'bracket':bracket,'status':0})
#     else:
#       # 좌표값이 같지 않으면 원이접하지 않음
#       stack.append({'pos':position,'bracket':bracket,'status':0})

# print(answer)