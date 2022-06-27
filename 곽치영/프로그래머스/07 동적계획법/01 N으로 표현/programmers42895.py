from itertools import product

def solution(N, number):
    MAX = 8
    dp = [set() for _ in range(MAX+1)]
    for i in range(1, MAX+1):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            if j <= i-j:
                dp[i].update(a + b for a, b in product(dp[j], dp[i-j]))
                dp[i].update(a * b for a, b in product(dp[j], dp[i-j]))
            dp[i].update(a - b for a, b in product(dp[j], dp[i-j]))
            dp[i].update(a // b for a, b in product(dp[j], dp[i-j]) if b != 0)
    for i in range(1,MAX+1):
        if number in dp[i]:
            break
    else:
        return -1
    return i
