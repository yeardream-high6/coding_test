import sys
input = sys.stdin.readline

mincount_3_in_mod5 = [0, 2, 4, 1, 3]

def solve(N):
    if mincount_3_in_mod5[N % 5] * 3 > N:
        return -1
    else:
        count5 = (N - mincount_3_in_mod5[N % 5] * 3) // 5
        # assert (N - mincount_3_in_mod5[N % 5] * 3) % 5 == 0
        return mincount_3_in_mod5[N % 5] + count5

N = int(input())
print(solve(N))
