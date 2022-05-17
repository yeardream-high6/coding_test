import sys
input = sys.stdin.readline

N = input()
A = set(map(int, input().split()))

M = input()
B = map(int, input().split())

for b in B:
    print(1 if b in A else 0)