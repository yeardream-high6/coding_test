import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    que = deque(pair for pair in enumerate(map(int, input().split())))
    
    for i in range(1, N+1):
        max_ = max(map(lambda p: p[1],que))
        while que[0][1] != max_:
            #print(max_, que[0])
            que.append(que.popleft())
        if que.popleft()[0] == M:
            break
    
    print(i)