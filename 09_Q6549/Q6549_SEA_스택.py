import sys

while True:
    user_input = list(map(int, input().split()))

    if user_input[0] == 0:
        break
    
    N = user_input[0]
    heights = [0] + user_input[1:]
    heights.append(0)
    ans = 0

    stack = [[0, 0]] # (몇번째, 높이)
    
    for rec_num in range(1, N + 2):
        # i번째 직사각형 높이보다 스택에 있는게 더 높으면
        # 스택의 탑이 현재 직사각형보다 큰 순간부터 넓이를 계산하는 방식이다.
        # 그전까지는 계속 높이가 같거나 큰 순서대로 스택에 쌓였을 것이고, 아래 while 조건을 만족하는 순간부터 이제 스택의 top부터 맨 밑까지 높이가 되고 폭은 1씩 증가시키면서 높이*폭을 계산해서 정답을 갱신하는 방식이다.
        while stack[-1][1] > heights[rec_num]:
            # 팝을 해주고
            temp_rect = stack.pop()

            # 그리고 면적을 계산한다.    
            # 같은 높이의 직사각형이 여러개 있는 경우도 처리가 된다.
            temp_area = max((rec_num - stack[-1][0] - 1) * temp_rect[1], temp_rect[1])
            
            # 기존 면적보다 크면 갱신.
            if temp_area > ans:
                ans = temp_area
        
        # while 처리 끝나면 이제 rec_num보다 작은 직사각형들만 스택에 있고 다시 스택에 rect_num을 넣는다.
        stack.append((rec_num, heights[rec_num]))
    print(ans)

