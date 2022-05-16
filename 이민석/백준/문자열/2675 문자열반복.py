import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
for i in range(n):
    a = input().split()
    b = str(a[1])
    for j in (b):
        print(j*int(a[0]), end='')
    print()
