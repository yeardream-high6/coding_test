import sys
sys.stdin=open("input.txt", "rt")


n = int(input())

ans = 1
x = 0

for _ in range(n):
    temp = ans % 15746
    ans = (ans + x) % 15746
    x = temp

print(ans)