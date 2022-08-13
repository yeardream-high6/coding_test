def f(n):
    dp = [-1, -1, -1, 1, -1, 1, 2, -1, 2, 3, 2, 3, 4] + [0] * n
    for i in range(13, n + 1):
        if dp[i-5] > dp[i-3]:
            dp[i] = dp[i-3] + 1
        else:
            dp[i] = dp[i-5] + 1
    return dp[n]
n = int(input())
print(f(n))


def f2(n):
    if n == 4 or n == 7:
        return -1
    
    cnt = 0
    while n > 0:
        if n % 5 == 0:
            cnt += n // 5
            break
        n -= 3
        cnt += 1

    return cnt 
    
# n = int(input())
# print(f(n))
for i in range(3, 41):
    a1 = f(i)
    a2 = f2(i)
    if a1 != a2:
        print(i, a1, a2)