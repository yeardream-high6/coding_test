import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))
meetings = sorted(meetings)

cnt = 0
time = 0
for m in meetings:
    if time <= m[1]:
        time = m[0]
        cnt += 1
print(cnt)