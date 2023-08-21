import sys
import heapq
N = int(sys.stdin.readline())
command_list = []

for _ in range(N):
    x = int(sys.stdin.readline())
    command_list.append(x)

heap = []
for i in command_list:
    if i != 0:
        heapq.heappush(heap, (-i, i)) #python heapq 로 기본적으로 만들어지는 heap은 최소힙(가장 작은 수가 root로 가는 형식)이므로
                                      #숫자에 -1을 곱해서 실제 값이 클수록 튜플의 0번 인덱스가 작아지게 바꿈
    else:
        if len(heap) <= 0:
            print(0)
        else:
            maximum = heapq.heappop(heap)[1] #최대heap 구현을 위한 인덱스가 아닌 실제 값을 출력해야 하므로 [1]인덱스를 출력
            print(maximum)

#메모리: 47180KB
#시간: 172ms