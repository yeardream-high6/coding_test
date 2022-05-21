# 3824 ms

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
print(sorted(map(int, input().split()))[K-1])