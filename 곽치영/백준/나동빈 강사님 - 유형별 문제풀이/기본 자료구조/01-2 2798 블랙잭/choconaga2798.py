import sys
input = sys.stdin.readline

import itertools

N, M = map(int, input().split())
number = list(map(int, input().split()))

max_ = 0
for i, j, k in itertools.combinations(range(N), 3):
    sum_ = number[i] + number[j] + number[k]
    if sum_ <= M:
        max_ = max(max_, sum_)

print(max_)