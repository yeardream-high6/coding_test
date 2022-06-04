import sys
sys.stdin=open("input.txt", "rt")


n = int(input())
A = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
    print(dp)

print(max(dp))
