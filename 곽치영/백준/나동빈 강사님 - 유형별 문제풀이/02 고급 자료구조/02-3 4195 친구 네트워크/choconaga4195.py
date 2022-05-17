import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = self
        self.height = 1
        self.size = 1


nodes = None

def find_root(node):
    # root 찾기
    root = node
    while root is not root.parent:
        root = root.parent
    # 경로 압축
    while node is not node.parent:
        node.parent, node = root, node.parent
    return root

def union(a, b):
    a = find_root(a)
    b = find_root(b)

    if a is b:
        return a

    # a.height >= b.height 이도록 순서 바꿈
    if a.height < b.height:
        a, b = b, a
    
    # a의 자식으로 b 추가
    b.parent = a
    a.height = max(a.height, b.height + 1)
    a.size += b.size

    return a

T = int(input())

for _ in range(T):
    F = int(input())
    nodes = {}
    for _ in range(F):
        a, b = input().split()

        if a not in nodes:
            nodes[a] = Node()

        if b not in nodes:
            nodes[b] = Node()
        
        root = union(nodes[a], nodes[b])
        print(root.size)
