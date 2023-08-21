N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

ans = [-1000000000, 1000000000]

def dfs(order, num_sum, target): # (더해진 숫자 개수, 총합, 더할 숫자 개수)
    if order == target: # 다 연산했으면 갱신
        ans[0] = max(ans[0], num_sum)
        ans[1] = min(ans[1], num_sum)
        return
    
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            
            if i == 0: # +
                dfs(order + 1, num_sum + nums[order], target)
            elif i == 1: # -
                dfs(order + 1, num_sum - nums[order], target)
            elif i == 2: # *
                dfs(order + 1, num_sum * nums[order], target)
            else: # %
                if num_sum < 0:
                    dfs(order + 1, -(abs(num_sum) // nums[order]), target)
                else:
                    dfs(order + 1, num_sum // nums[order], target)
            
            ops[i] += 1
    
dfs(1, nums[0], N) 
for n in ans:
    print(n)