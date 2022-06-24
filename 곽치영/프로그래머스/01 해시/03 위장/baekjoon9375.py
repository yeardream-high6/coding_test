def solution(clothes):
    counter = {}
    for [_, part] in clothes:
        if part in counter:
            counter[part] += 1
        else:
            counter[part] = 1
    answer = 1
    for part, count in counter.items():
        answer *= count + 1
    answer -= 1
    return answer

import sys
read_line = sys.stdin.readline

T = int(read_line())
for _ in range(T):
    N = int(read_line())
    clothes = [read_line().split() for _ in range(N)]
    print(solution(clothes))
