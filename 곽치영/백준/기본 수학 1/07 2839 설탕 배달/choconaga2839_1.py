import sys
input = sys.stdin.readline

head = [0, -1, -1, 1, -1, 1, 2, -1]
mod5_diff = [0, 1, 2, 1, 2]

N = int(input())
if N < 8:
    print(head[N])
else:
    print(N // 5 + mod5_diff[N % 5])
