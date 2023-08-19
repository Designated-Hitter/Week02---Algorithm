"""
우선 막대 높이를 다 스택에 차례대로 넣고, top을 하나 빼서 값 X를 저장하고 ans = 1을 해준 후,
X값보다 큰 경우 ans += 1 해주면 된다.
python3: 시간초과
pypy3: 220ms
"""

from collections import deque

N = int(input())
nums = [int(input()) for _ in range(N)]

stack = deque() # 220ms
# stack = [] # 232ms
for n in nums:
    stack.append(n)

val = stack.pop() # 기준 값
ans = 1
while len(stack): # 스택이 비어있지 않으면 계속 수행
    candidate = stack.pop() # 스택 맨 위 값을 뺀다.

    if candidate > val: # val보다 더 크면 보인다.
        ans += 1
        
        # 이제 candiate보다 더 왼쪽에 있는 것들은 candidate보다 더 커야 하기 때문에 val값 갱신
        val = candidate

print(ans)