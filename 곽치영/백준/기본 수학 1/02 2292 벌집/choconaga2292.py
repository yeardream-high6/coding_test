import sys
input = sys.stdin.readline

# 1층: 1
# 2층: ~ 1 + 1 * 6
# 3층: ~ 1 + (1 + 2) * 6
# 4층: ~ 1 + (1 + 2 + 3) * 6

# k층: ~ 1 + (1 + 2 + 3 + ... + (k-1)) * 6
#      = 1 + k(k-1)/2 * 6

# 즉, N <= 1 + k(k-1)/2 * 6 인 최소 k 찾기
#     N <= 1 + 3(k^2 - k)
#        = 1 + 3[(k - 1/2)^2 - 1/4]
#        = 3(k - 1/2)^2 + 1/4
# (N-1/4)/3 <= (k - 1/2)^2
# sqrt((N-1/4)/3) <= k - 1/2 인 최소 k 찾기
# sqrt((12N-3))/6 + 1/2 <= k 인 최소 k 찾기

import math

# float 오차를 회피하기 위해 정수로 구현합니다.

# sqrt(n)의 올림값을 정확하게 구하는 함수 (단 n은 1이상의 양의 자연수)
def ceil_isqrt(n):
    return 1 + math.isqrt(n - 1)

# n/d의 올림값을 정확하게 구하는 함수 (단, n, d는 1이상의 양의 자연수)
def ceil_idiv(n, d):
    return -(-n // d)

N = int(input())

k = ceil_idiv(ceil_isqrt(12*N-3)+3, 6)

print(k)