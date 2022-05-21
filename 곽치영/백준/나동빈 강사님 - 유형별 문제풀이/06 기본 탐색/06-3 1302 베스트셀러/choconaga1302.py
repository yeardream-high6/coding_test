import sys
input = sys.stdin.readline

N = int(input())

counter = {}

for _ in range(N):
    name = input().strip()

    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1

most_saled = min(counter.items(), key=lambda p: (-p[1], p[0]))
print(most_saled[0])