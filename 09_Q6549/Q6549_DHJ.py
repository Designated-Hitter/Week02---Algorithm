import sys
while True:

    input = sys.stdin.readline()
    test_case = list(map(int, input.split()))

    n = test_case[0]

    if n == 0:
        break
    
    result = 0
    heights = test_case[1:]

    stack = []

    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack[-1]]
            stack.pop()
            width = i
            if stack:
                width = (i - stack[-1] - 1)
            result = max(result, width * height)
        stack.append(i)

    while stack:
        height = heights[stack[-1]]
        stack.pop()
        width = n
        if stack:
            width = (n - stack[-1] - 1)
        result = max(result, width * height)

    print(result)