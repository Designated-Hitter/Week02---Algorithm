K = int(input())
nums = [int(input()) for _ in range(K)]

stack = []

for n in nums:
    if n != 0: # 0이 아니면 stack에 넣기
        stack.append(n)
    else: # 0 이면 맨 위에 있는 숫자 제거
        stack.pop()

stack_sum = 0

for n in stack:
    stack_sum += n

print(stack_sum)