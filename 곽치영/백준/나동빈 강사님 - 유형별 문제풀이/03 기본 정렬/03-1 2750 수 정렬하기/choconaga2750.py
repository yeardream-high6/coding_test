import sys
N = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.read().split()))
print(*arr, sep='\n')
