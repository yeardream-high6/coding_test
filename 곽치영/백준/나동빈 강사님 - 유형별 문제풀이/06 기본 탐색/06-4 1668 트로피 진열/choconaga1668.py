import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

def cnt_view(iter):
    max_height = 0
    cnt = 0
    for height in iter:
        if height > max_height:
            max_height = height
            cnt += 1
    return cnt

print(cnt_view(height))
print(cnt_view(reversed(height)))