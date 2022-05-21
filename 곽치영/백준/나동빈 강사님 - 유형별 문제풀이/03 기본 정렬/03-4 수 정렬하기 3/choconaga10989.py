import sys
input = sys.stdin.readline

MAX = 10000

N = int(input())
value_counts = [0] * (MAX+1)

for _ in range(N):
    x = int(input())
    value_counts[x] += 1

for x, cnt in enumerate(value_counts):
    for _ in range(cnt):
        print(x)