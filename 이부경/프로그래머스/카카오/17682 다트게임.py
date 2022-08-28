def solution(dartResult):
    sums = [0, 0, 0]
    s = -1
    i = 0
    d = dartResult
    while i < len(d):
        if d[i] in '0123456789':
            s += 1
            if d[i+1] == '0':
                sums[s] = 10
                i += 1
            else:
                sums[s] = int(d[i])
        else:
            if d[i] == 'D':
                sums[s] = sums[s] ** 2
            elif d[i] == 'T':
                sums[s] = sums[s] ** 3
            elif d[i] == '*':
                sums[s] = sums[s] * 2
                if s > 0:
                    sums[s-1] = sums[s-1] * 2
            elif d[i] == '#':
                sums[s] = -sums[s]
        i += 1
    return sum(sums)

dartResult = '1S2D*3T'
print(solution(dartResult))


