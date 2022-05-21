def solve(N, r, c):
    if N == 0:
        return 0
    sub_length = 2**(N-1)
    cnt = 0
    if r >= sub_length:
        r -= sub_length
        cnt += sub_length**2 * 2
    if c >= sub_length:
        c -= sub_length
        cnt += sub_length**2
    return cnt + solve(N-1, r, c)

N, r, c = map(int, input().split())
print(solve(N, r, c))