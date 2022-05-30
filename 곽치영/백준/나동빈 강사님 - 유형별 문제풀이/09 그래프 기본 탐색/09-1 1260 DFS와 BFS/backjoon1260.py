from collections import deque
import sys

def dfs(N, adj_list, V):
    result = []

    check = [True] * N
    stack = []
    
    result.append(V+1)
    check[V] = False
    stack.append(iter(adj_list[V]))

    while stack:
        try:
            b = next(stack[-1])
        except StopIteration:
            stack.pop()
        else:
            if check[b]:
                result.append(b+1)
                check[b] = False
                stack.append(iter(adj_list[b]))
    
    return result

def bfs(N, adj_list, V):
    result = []

    check = [True] * N
    que = deque()

    check[V] = False
    que.append(V)

    while que:
        a = que.popleft()
        result.append(a+1)

        for b in adj_list[a]:
            if check[b]:
                check[b] = False
                que.append(b)
    
    return result

input = sys.stdin.readline
N, M, V = map(int, input().split())
V -= 1

adj_list = [[] for _ in range(N)]

for _ in range(M):
    a, b = (int(s)-1 for s in input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(N):
    adj_list[i] = sorted(set(adj_list[i]))

print(' '.join(map(str, dfs(N, adj_list, V))))
print(' '.join(map(str, bfs(N, adj_list, V))))
