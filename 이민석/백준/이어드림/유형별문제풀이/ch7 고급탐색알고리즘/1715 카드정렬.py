import sys
sys.stdin=open("input.txt", "rt")
import heapq


n = int(input())
deck = []

for _ in range(n):
    card = int(input())
    heapq.heappush(deck, card)

if len(deck) == 1:  # 1개일 경우 비교x
    print(0)
else:
    ans = 0
    while len(deck) > 1:
        deck_1 = heapq.heappop(deck)  # 제일 작은 덱
        deck_2 = heapq.heappop(deck)  # 두번째로 작은 덱
        ans += deck_1 + deck_2  # 가장 작은 덱 과 두번째로 작은 덱을 더해준다
        heapq.heappush(deck, ans)  # 더한 덱을 다시 넣어준다

    print(ans)