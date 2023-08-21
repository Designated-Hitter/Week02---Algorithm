import sys
from collections import deque
N = int(sys.stdin.readline())

card_list = deque()
for i in range(1,N + 1):
    card_list.append(i)

flip_flop = 0

while len(card_list) > 1:
    if flip_flop == 0:
        card_list.popleft()
        flip_flop = 1
    else:
        top_card = card_list.popleft()
        card_list.append(top_card)
        flip_flop = 0

print(card_list[0])

#메모리: 51024KB
#시간: 304ms