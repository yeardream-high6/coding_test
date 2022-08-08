N = int(input())
t = [0] * N
p = [0] * N
for i in range(N):
    t[i], p[i] = map(int, input().split())

dp = [0] * (N+1)
for i in reversed(range(N)):
    if t[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])
print(dp[0])
