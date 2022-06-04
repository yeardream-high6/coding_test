from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trusted = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    trusted[B].append(A)

not_visited = [True] * N
net_trusted = [0] * N

for c in range(N):
    for a in range(N):
        not_visited[a] = True
    
    que = deque()
    que.append(c)
    not_visited[c] = False
    cnt = 1
    while que:
        b = que.popleft()
        for a in trusted[b]:
            if not_visited[a]:
                que.append(a)
                not_visited[a] = False
                cnt += 1
    net_trusted[c] = cnt

max_net_trusted = max(net_trusted)
print(' '.join([str(c+1) for c in range(N) if net_trusted[c] == max_net_trusted]))