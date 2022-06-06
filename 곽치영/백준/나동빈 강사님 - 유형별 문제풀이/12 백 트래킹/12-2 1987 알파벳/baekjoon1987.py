R, C = map(int, input().split())
map = [None] * R
for i in range(R):
    map[i] = [ord(alphabet) - ord('A') for alphabet in input()]

def get_heuristic_bound(map, R, C):
    alphabets = set()
    for k in range(1, R+C):
        # for i in range(max(0,k-C), min(k, R)):
        #     print(i, k-i-1)
        # print()
        alphabets |= set(map[i][k-i-1] for i in range(max(0,k-C), min(k, R)))
        if len(alphabets) < k:
            return len(alphabets)
    else:
        return len(alphabets)

heuristic_bound = get_heuristic_bound(map, R, C)

check_alphabet = [True] * (ord('Z') - ord('A') + 1)
cnt = 0
max_cnt = 0

class MaxBoundFound(Exception):
    pass

def dfs(i, j):
    global cnt, max_cnt
    if check_alphabet[map[i][j]]:
        cnt += 1
        check_alphabet[map[i][j]] = False
        if i > 0:
            dfs(i-1, j)
        if j > 0:
            dfs(i, j-1)
        if i < R-1:
            dfs(i+1, j)
        if j < C-1:
            dfs(i, j+1)
        cnt -= 1
        check_alphabet[map[i][j]] = True
    elif max_cnt < cnt:
        max_cnt = cnt
        if max_cnt == heuristic_bound:
            raise MaxBoundFound()

try:
    dfs(0,0)
except MaxBoundFound:
    pass
print(max_cnt)
