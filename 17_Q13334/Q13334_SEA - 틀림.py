from collections import defaultdict
import heapq

"""
우선, 각 사람의 집 위치를 순회한다.
다른 집으로 가는 조건은 최소힙에서 꺼내서 이게 철로에 속하는지 봤을 때 속하지 않는 경우이다.
속하지 않을 때 이 값을 다시 푸시하고 다음 선으로 간다.
그리고 동시에, 각 선을 방문할 때 해당 점에 딱 맞게 배치했을 때 몇명이나 내부에 있는지를 담는 배열을 만들어 넣는다.
이 배열은 다음 선으로 갔을 때 새롭게 갈 수 있게 되는 사람 + ans에 추가될 값이다. 
"""


N = int(input())
sorted_hq = sorted([sorted(tuple(map(int, input().split()))) for _ in range(N)], key= lambda x: (x[1], x[0]))
d = int(input())

hq = []
for i in range(N):
    heapq.heappush(hq, tuple(reversed(sorted_hq[i])))

dic = defaultdict(int)

ans = 0

for i in range(len(sorted_hq)):
    st = sorted_hq[i][0]
    en = st + d
    # if i > 0 and 

    temp = 0
    while True:
        # 힙에서 하나 꺼낸다.
        if len(hq) != 0:
            cur = heapq.heappop(hq)
        else:
            break

        if st == cur[1]: # 같은 줄에 있을 때
            if en < cur[0]: # 벗어나면 패스
                # print("HI", en, cur[1], en == cur[1])
                continue

            # 내부에 있으면 temp +1 
            if cur[0] <= en:
                temp += 1

        elif cur[0] <= en: # 경계 말고 완전 내부에 있는 선이면
            temp += 1
            dic[i] += 1
        
        # 내부에 없으면 지금까지 답을 ans에 갱신하고 cur은 다시 힙에 넣기
        else:
            ans = max(ans, (temp + dic[i - 1]) if i > 0 else temp)
            heapq.heappush(hq, cur)
            # saved.append(temp)
            break
        
print(ans)