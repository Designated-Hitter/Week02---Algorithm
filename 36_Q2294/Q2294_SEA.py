import sys
from collections import deque

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
checks = [0] * (K + 1)

if K < min(nums):
    print(-1)
    sys.exit(0)

q = deque()
q.append((nums[0], 0, 1))
for i in range(1, len(nums)):
    if nums[i - 1] != nums[i]:
        q.append((nums[i], i, 1))

ans = sys.maxsize
flag = False
while q:
    cur = q.popleft()
    num_sum, idx, cnts = cur

    if num_sum == K:
        ans = min(ans, cnts)
        break

    for i in range(idx, len(nums)):
        if num_sum + nums[i] == K: # K가 되었으면 답과 비교 후 작으면 넣기
            ans = min(ans, cnts + 1)
            flag = True
            break

        elif num_sum + nums[i] > K: # K보다 더 크면 이후는 볼 필요 없음.
            break
        
        else:
            # K보다 작으면 큐에 넣어 돌리기
            # 숫자가 1 5 12라고 칠 때, 1이 들어가서 생기는 숫자들이 먼저 이 조건을 통과해서 checks를 1로 체크해주면,이후 5에서 그 전에 생겼던 값과 똑같은 값에 대한 모든 경우의 수는 이미 1에서 가지치기 되면서 만들었기 때문에, 다시 확인할 필요가 없다.
            if checks[num_sum + nums[i]] == 0:
                checks[num_sum + nums[i]] = 1
                q.append((num_sum + nums[i], i, cnts + 1))
    
    if flag:
        break

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)