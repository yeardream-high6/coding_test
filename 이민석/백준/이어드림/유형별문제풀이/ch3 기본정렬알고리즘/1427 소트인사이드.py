import sys
sys.stdin=open("input.txt", "rt")

arr = input()

for i in range(9, -1, -1):
    for j in arr:
        if int(j) == i:
            print(i, end='')