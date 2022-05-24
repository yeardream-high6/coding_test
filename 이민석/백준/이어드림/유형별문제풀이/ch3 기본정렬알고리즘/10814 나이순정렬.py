import sys
sys.stdin=open("input.txt", "rt")


n = int(input())
arr = []

for _ in range(n):

    age, name = input().split(' ')
    arr.append((int(age), name))

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
    print(i[0], i[1])