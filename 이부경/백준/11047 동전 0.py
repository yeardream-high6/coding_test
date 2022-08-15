N, k = map(int, input().split())
coins = [int(input()) for i in range(N)]

total_cnt = 0
for c in sorted(coins, reverse=True):
    if k - c >= 0:
        cnt = k // c
        k -= c * cnt
        total_cnt += cnt

print(total_cnt)