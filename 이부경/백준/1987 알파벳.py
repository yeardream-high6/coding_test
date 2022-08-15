from functools import cache

R, C = map(int, input().split())
mat = [list(input()) for _ in range(R)]
max_step = 0

@cache
def f(i, j, visited, step):
    global max_step
    if i < 0 or i >= R or j < 0 or j >= C:
        return
    
    if mat[i][j] in visited:
        return
    
    step += 1
    if max_step < step:
        max_step  =  step
    
    visited += mat[i][j]
    f(i - 1, j, visited, step)
    f(i + 1, j, visited, step)
    f(i, j - 1, visited, step)
    f(i, j + 1, visited, step)

f(0, 0, '', 0)
print(max_step)