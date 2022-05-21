import sys
input = sys.stdin.readline

parent = None
height = None

def find(idx):
    root = idx
    while root != parent[root]:
        root = parent[root]        
    while idx != parent[idx]:
        parent[idx], idx = root, parent[idx]
    return root

def union(a, b):
    a = find(a)
    b = find(b)
    if height[a] < height[b]:
        a, b = b, a
    if a != b:
        parent[b] = a
        height[a] = max(height[a], height[b]+1)

N, M = map(int, input().split())
edges = [None] * M
parent = list(range(N+1))
height = [1] * (N+1)

for i in range(M):
    A, B, C = map(int, input().split())
    edges[i] = C, A, B

X, Y = map(int, input().split())

edges.sort(reverse=True)

for C, A, B in edges:
    union(A, B)
    if find(X) == find(Y):
        break

print(C)