from collections import deque

N = int(input())
heights = list(map(int, input().split())) # 6 9 5 7 4
hash = {}

for i in range(len(heights)):
    hash[heights[i]] = i

stack = deque()

result = []
for i in range(len(heights)):
    if len(stack) == 0: # 일단 스택이 비어있으면 앞에 아무것도 없기 때문에 0 저장 
        result.append(0)
        # 스택에 넣기
        stack.append(heights[i])
    
    else: # 있는 경우 우선 자기보다 작은건 다 팝시킴
        flag = False
        while len(stack) > 0:
            front = stack.pop() # 우선 꺼내서
            
            if front >= heights[i]: # 나보다 같거나 크면 이 탑이 답
                result.append(hash[front] + 1) # 해시에 저장했던 인덱스 반환
                stack.append(front) # 다시 넣어주기
                flag = True
                break
            else: # 작으면 그냥 다음거 확인하러감.
                continue
        
        # while 탈출했는데 flag False면 다 팝된거라서 0 넣기
        if not flag:
            result.append(0)

        stack.append(heights[i])


for n in result:
    print(n, end= ' ')



        
    

        