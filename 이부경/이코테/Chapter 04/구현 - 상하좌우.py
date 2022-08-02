def f(n, plan):
    i = 1
    j = 1
    for p in plan:
        if p == 'L':
            j = max(j - 1, 1)
        if p == 'R':
            j = min(j + 1, n)
        if p == 'U':
            i = max(i - 1, 1)
        if p == 'D':
            i = min(i + 1, n)
    return i, j

n = 5
plan = 'LRUD'
print(f(n, plan))