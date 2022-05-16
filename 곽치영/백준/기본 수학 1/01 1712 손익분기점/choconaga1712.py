import sys
import math
input = sys.stdin.readline

# Cx > A + Bx 인 최소 x 찾기
# C > B이면
    # x > A/(C-B) 인 최소 x 찾기
    # 즉, x = 내림( A/(C-B) ) + 1
# 아니면 손익분기점 없음

A, B, C = tuple(map(int, input().split()))

if C > B:
    print( A // (C-B) + 1 )
else:
    print(-1)