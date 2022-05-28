# 허프만 코딩 (그리디)

from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
decks = [int(input()) for _ in range(N)]
heapify(decks)

count = 0
while len(decks) >= 2:
    new_deck = heappop(decks) + heappop(decks)
    count += new_deck
    heappush(decks, new_deck)

print(count)
