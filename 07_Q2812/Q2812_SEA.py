from collections import deque
import sys

N, K = map(int, input().split()) 
num = input()
stack = deque()

remained = K
ans = ""
for i in range(len(num)):
    if remained == 0: # 남은 기회 없으면 그냥 다 ans에 추가
        for j in range(len(stack)):
            ans += str(stack[j])

        ans += num[i:]
        print(int(ans))
        sys.exit(0)
    
    # 만약 스택에 아무것도 없으면 그냥 넣기
    if len(stack) == 0:
        stack.append(int(num[i]))
    
    # 있으면 top이 자기보다 작은 숫자면 remained가 0이 될 때까지 팝시키고 넣기
    else:
        while len(stack) != 0 and remained > 0 and stack[-1] < int(num[i]):
            remained -= 1
            stack.pop()
        
        # while 빠져나오면 넣기
        stack.append(int(num[i]))

for i in range(len(stack)):
    ans += str(stack[i])

if remained > 0:
    ans = ans[:len(ans) - remained]

print(int(ans))


