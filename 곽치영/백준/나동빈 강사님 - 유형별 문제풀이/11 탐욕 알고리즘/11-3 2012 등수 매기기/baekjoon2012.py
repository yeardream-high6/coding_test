import sys
sys.stdin.readline()
arr = sorted(map(int, sys.stdin.read().split()))
answer = sum(i+1 - v if i+1 > v else v - (i+1) for i, v in enumerate(arr))
print(answer)
