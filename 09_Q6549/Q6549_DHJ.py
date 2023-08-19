while True:
    user_input = list(map(int, input().split()))

    n = user_input[0]

    if n == 0:
        break

    heights = user_input[1:]

    stack = [heights[0]]
    answers = [n]
    for i in range(1, len(heights)):
        if stack and min(stack) > heights[i]:
            print(f"min stack = {min(stack)}")
            print(f'heights = {heights[i]}')
            answers.append(min(stack) * len(stack))
            stack.clear()
        else:
            stack.append(heights[i])
    
    if stack:
        print('반복이 끝나고도 스택이 남아있나')
        print(f"min stack = {min(stack)}")
        print(f'len(stack) = {len(stack)}')
        answers.append(min(stack) * len(stack))
    
    print(max(answers))