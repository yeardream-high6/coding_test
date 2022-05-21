import sys
input = sys.stdin.readline

N, M = map(int, input().split())
state = [None] * N
for i in range(N):
    state[i] = input().strip()

X = 'X'

empty_row_cnt = 0
for i in range(N):
    for j in range(M):
        if state[i][j] == X:
            break
    else:
        empty_row_cnt += 1

empty_col_cnt = 0
for j in range(M):
    for i in range(N):
        if state[i][j] == X:
            break
    else:
        empty_col_cnt += 1

print(max(empty_row_cnt, empty_col_cnt))