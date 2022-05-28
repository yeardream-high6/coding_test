from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

next_probs = [[] for _ in range(N)]
prev_cnt = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    next_probs[A].append(B)
    prev_cnt[B] += 1

heap = [i for i in range(N) if prev_cnt[i] == 0]
heapify(heap)

answer = []

while heap:
    curr_min = heappop(heap)
    answer.append(curr_min+1)
    for next_prob in next_probs[curr_min]:
        prev_cnt[next_prob] -= 1
        if prev_cnt[next_prob] == 0:
            heappush(heap, next_prob)

print(' '.join(map(str, answer)))
