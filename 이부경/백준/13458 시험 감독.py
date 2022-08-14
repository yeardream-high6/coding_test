from math import ceil

N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())

cnt = 0
for a in A:
    cnt += max(0, ceil((a - B) / C)) + 1
print(cnt)