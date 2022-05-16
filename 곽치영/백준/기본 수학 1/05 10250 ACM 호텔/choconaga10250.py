def solve(H, W, N):
    N = N - 1
    X = N // H
    Y = N % H
    return Y + 1, X + 1

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for t in range(T):
        H, W, N = tuple(map(int, input().split()))
        Y, X = solve(H, W, N)
        print(f"{Y:d}{X:02d}")

if __name__ == '__main__':
    main()