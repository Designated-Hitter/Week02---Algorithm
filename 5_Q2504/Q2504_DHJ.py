import sys
str = sys.stdin.readline()
print(str)
str_list = []
for i in range(len(str)):
    str_list.append(str[i])
str_list.pop()
print(str_list)

for i in range(len(str_list) - 1):
    if str_list[i] == '(' and str_list[i + 1] == ')':
        del str_list[i:i + 2]
        str_list.insert(i, 2)
        i = 0
        print('loop return1')
        print(str_list)
        print(f'i = {i}')
        continue
    elif str_list[i] == '['and str_list[i + 1] == ']':
        del str_list[i:i + 2]
        str_list.insert(i,3)
        i = 0
        print('loop return2')
        print(str_list)
        print(f'i = {i}')
        continue
    elif str_list[i] == '(' and str(type(str_list[i + 1])) == "<class 'int'>" and str_list[i + 2] == ')':
        del str_list[i:i + 3]
        str_list.insert(i, int * 2)
        i = 0
        print('loop return3')
        print(str_list)
        print(f'i = {i}')
        continue
    elif str_list[i] == '[' and str(type(str_list[i + 1])) == "<class 'int'>" and str_list[i + 2] == ']':
        del str_list[i:i + 3]
        str_list.insert(i, int * 3)
        i = 0
        print('loop return4')
        print(str_list)
        print(f'i = {i}')
        continue
    elif str_list[i] == int and str_list [i + 1] == int:
        plus = str_list[i] + str_list[i + 1]
        del str_list[i:i + 2]
        str_list.insert(i, plus)
        i = 0
        print('loop return5')
        print(str_list)
        print(f'i = {i}')
        continue

if len(str_list) != 0:
    print(0)
else:
    print(str_list[0])

