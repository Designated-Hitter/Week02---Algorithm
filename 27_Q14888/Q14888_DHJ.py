import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

# 최솟값과 최댓값 초기화
min_value = int(1e9)
max_value = int(-1e9)

#------------------------------------------------------------------------
def dfs(order, num_sum, target): # (더해진 숫자 개수, 총합, 더할 숫자 개수)
    if order == target: # 다 연산했으면 갱신
        global max_value
        global min_value
        max_value = max(max_value, num_sum)
        min_value = min(min_value, num_sum)
        return
    
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            
            if i == 0: # +
                dfs(order + 1, num_sum + num_list[order], target)
            elif i == 1: # -
                dfs(order + 1, num_sum - num_list[order], target)
            elif i == 2: # *
                dfs(order + 1, num_sum * num_list[order], target)
            else: # %
                if num_sum < 0:
                    dfs(order + 1, -(abs(num_sum) // num_list[order]), target)
                else:
                    dfs(order + 1, num_sum // num_list[order], target)
            
            operator[i] += 1
#------------------------------------------------------------------------

dfs(1, num_list[0], N)

print(max_value)
print(min_value)