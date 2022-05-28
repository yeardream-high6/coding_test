import sys
input = sys.stdin.readline

nodes = {}

def preorder(node):
    if node != '.':
        return node + preorder(nodes[node][0]) + preorder(nodes[node][1])
    return ''

def inorder(node):
    if node != '.':
        return inorder(nodes[node][0]) + node + inorder(nodes[node][1])
    return ''

def postorder(node):
    if node != '.':
        return postorder(nodes[node][0]) + postorder(nodes[node][1]) + node
    return ''

N = int(input())

for _ in range(N):
    x, l, r = input().split()
    nodes[x] = (l, r)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))