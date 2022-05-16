def ceil_div(n, d):
    return -(-n//d)

def solve(A, B, V):
    if V <= A:
        return 1
    else:
        return ceil_div(V - A, A - B) + 1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    A, B, V = tuple(map(int, input().split()))
    print(solve(A, B, V))