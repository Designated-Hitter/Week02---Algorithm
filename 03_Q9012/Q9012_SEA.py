"""
우선 순회했을 때 두 (와 )의 개수가 다르면 NO
그후 (인 경우 스택에 넣고, )인 경우 스택이 비어있으면 NO, 차 있으면 하나 빼기
"""
N = int(input())
parenthesises = [input() for _ in range(N)]

for i in range(len(parenthesises)): # ()() 케이스 1개씩 순회
    flag = True # 플래그 만들기
    stack = [] # 스택

    for j in range(len(parenthesises[i])): # 케이스 1개를 한 인덱스씩 순회
        if parenthesises[i][j] == '(': # (면 스택에 넣기
            stack.append('(')
        
        else: # )인 경우
            # 스택에 남은 (가 없는데 )가 나오면 짝이 없어서 NO
            if len(stack) == 0:
                print("NO")
                flag = False
                break
            else:
                stack.pop()


    # 중간에 이미 불가능한 경우 패스
    if not flag:
        continue

    # 스택을 나왔을 때 스택에 아직 (가 있으면 안됨
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
