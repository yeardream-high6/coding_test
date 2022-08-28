import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

d = [0] * 1001

# 다이나믹 프로그래밍 진행 bottom-up
d[1] =1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])