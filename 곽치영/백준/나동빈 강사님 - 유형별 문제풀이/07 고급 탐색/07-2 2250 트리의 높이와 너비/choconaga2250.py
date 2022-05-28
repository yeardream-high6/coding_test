import sys
sys.setrecursionlimit(2000_000)
input = sys.stdin.readline

N = int(input())
parent = [None] * (N+1)
left = [None] * (N+1)
right = [None] * (N+1)
root = 1

for _ in range(N):
    p, l, r = map(int, input().split())
    if l != -1:
        parent[l] = p
        left[p] = l
    if r != -1:
        parent[r] = p
        right[p] = r

left_most = [None] * (N+1)
right_most = [None] * (N+1)
col = 0

def find_root(node):
    while parent[node]:
        node = parent[node]
    return node

def preorder_update(node, level):
    global col

    if node:
        preorder_update(left[node], level+1)
        col += 1
        if left_most[level] is None:
            left_most[level] = col
        right_most[level] = col
        preorder_update(right[node], level+1)

preorder_update(node=find_root(1), level=1)

max_idx = None
max_value = 0
for i in range(1, N+1):
    if left_most[i] is None:
        break
    width = right_most[i] - left_most[i] + 1
    if max_value < width:
        max_value = width
        max_idx = i

print(max_idx, max_value)
