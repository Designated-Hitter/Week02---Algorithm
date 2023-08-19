import sys
input = sys.stdin.readline

array = list(input())


# def confirm(array):
#     stack = []
#     flag = 0
#     for j in range(len(array)):
#         if array[j] == '(':
#             stack.append(array[j])
#         elif array[j] == ')':
#             if len(stack) == 0:
#                 flag = 1
#                 break
#             stack.pop()

#     if len(stack) != 0 or flag == 1:
#         print("NO")
#     else:
#         print("YES")

# '''
# (( x
# ()  
# )) 기존 * 2
# )( x 기존 + 

# '''


# stack = []          # 괄호
# num_record = []     # 완성숫자 저장
# mul = []            # 추후 곱해야할 내용들
# num = 0
# num_candidate = 0

# for i in range(len(array)):
#     if array[i] == '(':
#         if stack[-1] == ')':
#             # num 완성되었다.
#             # 완성된 num에 더할 새로운 num을 시작하겠다.

#             num_record.append(num)
#             num = 0
#         elif stack[-1] == '(':
#             mul.append(2)

#     if array[i] == ')':
#         if stack[-1] == '(':
#             num_candidate



#         num = 0
#         mul_stack.append(2)
###############

'''
(()[[]])([])
괄호시작할때 마다 내부 요소에 분배법칙으로 곱하기 적용
'''

stack = []
answer = 0
tmp = 1

for i in range(len(array)):
    if array[i] == '(':
        stack.append(array[i])
        tmp *= 2
    elif array[i] == '[':
        stack.append(array[i])
        tmp *= 3
    elif array[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if array[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    elif array[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if array[i-1] == '[':
            answer += tmp
        
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)