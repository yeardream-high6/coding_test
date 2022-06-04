from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (N+1)

que = deque()
que.append(1)
visited[1] = True

cnt = 0
while que:
    cnt += 1
    a = que.pop()
    for b in adj_list[a]:
        if not visited[b]:
            visited[b] = True
            que.append(b)

print(cnt-1)
