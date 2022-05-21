# 6800 ms

import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K <= N // 2:
    lst = [-int(s) for s in input().split()]

    heap = lst[:K]
    heapq.heapify(heap)

    for x in lst[K:]:
        heapq.heappushpop(heap, x)
    print(-min(heap))

else:
    K = N - K + 1
    lst = [int(s) for s in input().split()]

    heap = lst[:K]
    heapq.heapify(heap)

    for x in lst[K:]:
        heapq.heappushpop(heap, x)
    print(min(heap))