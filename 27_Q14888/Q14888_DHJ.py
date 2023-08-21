import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
plus, minus, multiply, divide = map(int, sys.stdin.readline().split())
operator_list = []
visited = [False] * (len(num_list) - 1)

for _ in range(plus):
    operator_list.append('plus')
for _ in range(minus):
    operator_list.append('minus')
for _ in range(multiply):
    operator_list.append('multiply')
for _ in range(divide):
    operator_list.append('divide')

#----------------------------------------------------------------------------------------------
possible_list = [0] * (len(num_list) - 1)
answer_list = []
def perm(n, k):
    if n == k:
        #가능한 리스트를 구하고 바로 결과를 계산하기
        temp_value = num_list[0]
        for i in range(0, len(possible_list)):
            if possible_list[i] == 'plus':
                temp_value = temp_value + num_list[i + 1]
            elif possible_list[i] == 'minus':
                temp_value = temp_value - num_list[i + 1]
            elif possible_list[i] == 'multiply':
                temp_value = temp_value * num_list[i + 1]
            else:
                if temp_value < 0:
                    temp_value = temp_value * -1
                    temp_value = (temp_value // num_list[i + 1]) * -1
                else:
                    temp_value = temp_value // num_list[i + 1]

        answer_list.append(temp_value)
            
    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_list[k] = operator_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False
    
perm(len(operator_list), 0)
#------------------------------------------------------------------------
print(max(answer_list))
print(min(answer_list))