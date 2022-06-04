from collections import deque
import sys
input = sys.stdin.readline

M, N, K = None, None, None
farm = None
que = None
num = None

def check_and_append(y, x):
    if farm[y][x] == -1:
        farm[y][x] = num
        que.append((y, x))

def group_by_bfs(y, x):
    check_and_append(y, x)
    while que:
        y, x = que.pop()
        if y > 0:
            check_and_append(y-1, x)
        if y+1 < N:
            check_and_append(y+1, x)
        if x > 0:
            check_and_append(y, x-1)
        if x+1 < M:
            check_and_append(y, x+1)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = -1
    
    que = deque()

    num = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == -1:
                num += 1
                group_by_bfs(y, x)
    
    print(num)
