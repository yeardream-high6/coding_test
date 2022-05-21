import sys
input = sys.stdin.readline

N = int(input())
sorted_pairs = sorted(tuple(map(int, input().split())) for _ in range(N))
for pair in sorted_pairs:
    print(pair[0], pair[1])