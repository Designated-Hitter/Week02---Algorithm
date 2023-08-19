import sys
input = sys.stdin.readline
import heapq

n = int(input())

card_deck = []
for _ in range(n):
    heapq.heappush(card_deck, int(input()))


if len(card_deck) == 1:
    print(0)
else:
    answer = 0
    while len(card_deck) > 1:
        temp_1 = heapq.heappop(card_deck) # 가장 작은
        temp_2 = heapq.heappop(card_deck) # 두번째 작은
        answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
        heapq.heappush(card_deck, temp_1 + temp_2) #더한 덱을 다시 넣어줌
    
    print(answer)