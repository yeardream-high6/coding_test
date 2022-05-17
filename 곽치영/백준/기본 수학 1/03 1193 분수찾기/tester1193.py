import choconaga1193

X = 0
for k in range(1,3_300+1):
    for i in range(1, k+1):
        j = k - i + 1
        X += 1
        if k % 2 == 0:
            a, b = i, j
        else:
            a, b = j, i
        assert a,b == choconaga1193.solve(X)
