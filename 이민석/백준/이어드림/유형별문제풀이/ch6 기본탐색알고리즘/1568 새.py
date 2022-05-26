import sys
sys.stdin=open("input.txt", "rt")

N = int(input())
ans = 0

while N > 0:
    i = 1
    while N - i >= 0:
        N -= i
        i += 1
        ans += 1

print(ans)