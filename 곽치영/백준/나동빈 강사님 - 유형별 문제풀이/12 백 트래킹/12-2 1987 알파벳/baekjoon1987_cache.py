# https://www.acmicpc.net/source/44232946 를 참고했습니다.

from functools import cache
R, C = map(int, input().split())
map = [input() for _ in range(R)]

max_length = 0

@cache
def dfs(i, j, string):
    global max_length
    if max_length < len(string):
        max_length = len(string)
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < R and 0 <= nj < C and map[ni][nj] not in string:
            dfs(ni, nj, string + map[ni][nj])

dfs(0, 0, map[0][0])

print(max_length)
