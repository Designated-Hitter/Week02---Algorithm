import sys
str_list = list(sys.stdin.readline().strip())

stack = []
answer = 0
temp = 1

for i in range(len(str_list)):
    if str_list[i] == '(' :
        stack.append(str_list[i])
        temp *= 2
    elif str_list[i] == '[':
        stack.append(str_list[i])
        temp *= 3
    elif str_list[i] ==')':
        if not stack or stack[-1] =='[':
            answer = 0
            break
        if str_list[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    else: 
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if str_list[i-1] == "[":
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)

# 메모리: 31256KB
# 시간: 48ms    

# for i in range(len(str_list) - 1):
#     if str_list[i] == '(' and str_list[i + 1] == ')':
#         del str_list[i:i + 2]
#         str_list.insert(i, 2)
#         i = 0
#         print('loop return1')
#         print(str_list)
#         print(f'i = {i}')
#         continue
#     elif str_list[i] == '['and str_list[i + 1] == ']':
#         del str_list[i:i + 2]
#         str_list.insert(i,3)
#         i = 0
#         print('loop return2')
#         print(str_list)
#         print(f'i = {i}')
#         continue
#     elif str_list[i] == '(' and str(type(str_list[i + 1])) == "<class 'int'>" and str_list[i + 2] == ')':
#         integer - str_list[i + 1]
#         del str_list[i:i + 3]
#         str_list.insert(i, integer * 2)
#         i = 0
#         print('loop return3')
#         print(str_list)
#         print(f'i = {i}')
#         continue
#     elif str_list[i] == '[' and str(type(str_list[i + 1])) == "<class 'int'>" and str_list[i + 2] == ']':
#         integer = str_list[i + 1]
#         del str_list[i:i + 3]
#         str_list.insert(i, integer * 3)
#         i = 0
#         print('loop return4')
#         print(str_list)
#         print(f'i = {i}')
#         continue
#     elif str(type(str_list[i])) == "<class 'int'>" and str(type(str_list [i + 1])) == "<class 'int'>":
#         plus = str_list[i] + str_list[i + 1]
#         del str_list[i:i + 2]
#         str_list.insert(i, plus)
#         i = 0
#         print('loop return5')
#         print(str_list)
#         print(f'i = {i}')
#         continue

# if len(str_list) != 0:
#     print(0)
# else:
#     print(str_list[0])

