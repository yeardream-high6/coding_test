N = int(input())
A = set(map(int, input().split()))
M = int(input())

for n in map(int, input().split()):
    print(int(n in A))
