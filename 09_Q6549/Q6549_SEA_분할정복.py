# 분할정복 함수. 직사각형 무리들을 반씩 나눠서(분할), 무리 내에 직사각형이 1개일 때부터 정복 시작.
def div_conq(st, en, heights):
    if st == en:
        return heights[st]
    
    # 2개 이상일 경우 mid를 구해서 양쪽을 호출시켜서 얻은 값을 비교해서 더 큰걸 취한다.
    mid = (st + en) // 2
    left_max = div_conq(st, mid, heights) # 왼쪽 영역에서 최대 넓이 구함
    right_max = div_conq(mid + 1, en, heights) # 오른쪽 영역에서 최대 넓이 구함.
    total_max = max(left_max, right_max) # 양 영역 중 최대 넓이 구함.

    # 우선 양쪽 각각에서의 영역 중 최대 넓이는 구했다. 이제 가운데 고려할 시간
    # 일단 가운데에서 두 직사각형을 선택함.
    p1 = mid 
    p2 = mid + 1

    # 이후 두 직사각형 중 높이가 낮은 것을 기준으로 넓이를 구해서 갱신함.
    total_max = max(total_max, min(heights[p1], heights[p2]) * 2)
    height = min(heights[p1], heights[p2])

    # 이제 p1이나 p2가 st나 en을 모두 넘기 전까지는 while을 돌린다.
    while st < p1 or p2 < en:
        # p1을 움직이고 싶을 때는 p1이 아직 안온 상태에서 p2가 먼저 도착한 상태거나 heights[p1 - 1] > heights[p2 - 1]일 때 가능하다. 최대한 큰쪽을 계속 선택해야 최대 넓이를 구할 수 있다.
        if st < p1 and (p2 >= en or heights[p1 - 1] > heights[p2 + 1]):
            height = min(height, heights[p1 - 1])
            p1 -= 1
        else:
            height = min(height, heights[p2 + 1])
            p2 += 1
            
        total_max = max(total_max, height * (p2 - p1 + 1))
    
    return total_max



while True:
    user_input = list(map(int, input().split()))

    n = user_input[0]

    if n == 0:
        break

    heights = user_input[1:]

    st = 0
    en = n - 1

    print(div_conq(st, en, heights))