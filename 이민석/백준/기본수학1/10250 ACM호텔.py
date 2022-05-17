import sys
sys.stdin=open("input.txt", "rt")

k = int(input())
for _ in range(k):
    h,w,n=map(int, input().split())
    x = n // h + 1
    y=n%h
    if y==0:
        y=h
        x-=1
    print(y*100+x)

