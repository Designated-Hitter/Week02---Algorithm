import sys
while True:
    input = sys.stdin.readline()
    user_input = list(map(int, input.split()))

    n = user_input[0]

    if n == 0:
        break

    heights = user_input[1:]

    stack = [heights[0]]
    answers = [n]
    for i in range(1, len(heights)):
        if heights[i] > 1:
            if stack and min(stack) > heights[i]:
                answers.append(min(stack) * len(stack))
                stack = []
                stack.append(heights[i])
            else:
                stack.append(heights[i])
        elif stack and heights[i] <= 1:
            #print('1이 나온 경우')
            answers.append(min(stack) * len(stack))
            stack = []
    
    if stack:
        #print('반복이 끝나고도 스택이 남아있나')
        answers.append(min(stack) * len(stack))
    
    print(max(answers))