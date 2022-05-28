import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W = [None] * N
V = [None] * N

for i in range(N):
    W[i], V[i] = map(int, input().split())

maximum_value = [[None] * (K+1) for _ in range(N)]

#numpy가 그립습니다.
#maximum_value[0][:W[0]] = 0
#maximum_value[0][W[0]:] = V[0]

for k in range(min(W[0], K+1)):
    maximum_value[0][k] = 0
for k in range(W[0], K+1):
    maximum_value[0][k] = V[0]

for n in range(1, N):
    # W[n] >= 1 의존
    maximum_value[n][:W[n]] = maximum_value[n-1][:W[n]]
    for k in range(W[n], K+1):
        maximum_value[n][k] = max(maximum_value[n-1][k], maximum_value[n-1][k-W[n]] + V[n])

print(maximum_value[N-1][K])
