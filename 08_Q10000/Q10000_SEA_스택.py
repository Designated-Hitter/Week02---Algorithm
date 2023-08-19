N = int(input())
"""
이해는 했다. 
내부 원 지름 구해서 스택에 넣고
내부합이랑 자기 지름이랑 같으면 +2, 다르면 +1. 그리고 자기 지름 스택에 넣기
"""

points = [] # [["L", 2], ["R", 8]]

for _ in range(N):
    c, r = list(map(int, input().split()))
    points.append(["L", c - r])
    points.append(["R", c + r])

# points에는 점 위치는 왼쪽에서부터 나오고, 종류는 R부터 나온다. 왜? 왼쪽 원부터 확인하기 위해서라고 일단 생각했음.
points.sort(key=lambda p: (-p[1], p[0]), reverse=True) # 점 위치: 오름차순, 점 종류: 내림차순(위치가 같으면 R->L)

stack = [] # 원의 왼쪽 끝점을 저장하는 스택 
areas = 1

for point in points:
    # 왼쪽 끝인 경우 일단 스택에 점 넣어줌
    if point[0] == "L":
        stack.append(point)
        continue

    # 오른쪽 끝이면 내 생각은 일단 같은 원이면 끝이고, 다른 원이면 내부 다 채워지는지 확인해야 함.
    
    # 일단 해당 원 내부 원 지름 길이 합 저장변수 선언
    width_sum = 0
    
    while stack:
        prev = stack.pop() # 우선 스택에는 아직은 원의 왼쪽 점만 있음. 왼쪽 점을 pop 해주고 

        # 내부에 원이 있었으면 해당 원의 너비 누적.
        if prev[0] == 'C':
            width_sum += prev[1]
        elif prev[0] == "L":
            " 원의 너비 계산"
            width = point[1] - prev[1]
            
            # 내부 원 지름 합산과 자기의 지름이 같은지 확인
            if width == width_sum:
                areas += 2
            else:
                areas += 1
            
            # 다른 원에 포함될 수 있으므로 추가.
            stack.append(["C", width])
            break

print(areas)

            





