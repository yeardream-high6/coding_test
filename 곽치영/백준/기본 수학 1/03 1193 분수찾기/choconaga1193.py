# 대각선 1: 1 번 이하
# 대각선 2: 1 + 2 번 이하
# ...
# 대각선 k: 1 + 2 + ... + k 번 이하

# X가 대각선 k에 위치: X <= k(k+1)/2 인 최소 k
# 2X <= k^2 + k
# 2X <= (k + 1/2)^2 - 1/4
# sqrt(2X+1/4) <= k + 1/2
# sqrt(2X+1/4) - 1/2 <= k
# k = ceil( sqrt(2X+1/4) - 1/2 )
# k = ceil( (sqrt(8*X+1) - 1) / 2 )

import math

# float 오차를 회피하기 위해 정수로 구현합니다. (X가 작으므로 필수 아님)

# sqrt(n)의 올림값을 정확하게 구하는 함수 (단 n은 1이상의 양의 자연수)
def ceil_isqrt(n):
    return 1 + math.isqrt(n - 1)

# n/d의 올림값을 정확하게 구하는 함수 (단, n, d는 1이상의 양의 자연수)
def ceil_idiv(n, d):
    return -(-n // d)

def solve(X):
    k = ceil_idiv( (ceil_isqrt(8*X+1) - 1), 2 )

    a = X - k*(k-1)//2
    b = k - a +1

    if k % 2 == 1:
        a, b = b, a

    return a, b

def main():
    import sys
    input = sys.stdin.readline

    X = int(input())
    a, b = solve(X)

    print(f"{a}/{b}")

if __name__ == '__main__':
    main()