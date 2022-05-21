import math

def max_k(N):
    return (math.isqrt(8*N+1)-1) // 2

N = int(input())

cnt = 0
while N > 0:
    K = max_k(N)
    cnt += K
    N -= K*(K+1)//2

print(cnt)