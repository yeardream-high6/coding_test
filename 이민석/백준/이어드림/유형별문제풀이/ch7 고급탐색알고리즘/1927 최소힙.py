import sys
sys.stdin=open("input.txt", "rt")
import heapq

input = sys.stdin.readline

min_heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(min_heap)>0:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)



