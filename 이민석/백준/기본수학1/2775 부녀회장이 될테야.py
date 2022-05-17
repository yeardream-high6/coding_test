import sys
sys.stdin=open("input.txt", "rt")


n = int(input())

for _ in range(n):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for i in range(floor):
        for j in range(1, num):
            f0[j] += f0[j-1]
    print(f0[-1])