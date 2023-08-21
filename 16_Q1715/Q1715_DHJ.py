import sys
import heapq
N = int(sys.stdin.readline())
heap = []
count = 0
for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)

while len(heap) > 1:
    # print('first heap')
    # print(heap)
    card_A = heapq.heappop(heap)
    # print('card_A')
    # print(card_A)
    # print('card_A_popped')
    # print(heap)
    card_B = heapq.heappop(heap)
    # print('card B')
    # print(card_B)
    # print('card_B popped')
    # print(heap)
    mixed_card = card_A + card_B
    # print('count up!')
    count += mixed_card
    # print(count)
    heapq.heappush(heap, mixed_card)
    # print('end heap')
    # print(heap)


print(count)