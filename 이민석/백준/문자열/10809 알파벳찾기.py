import sys
sys.stdin=open("input.txt", "rt")

s = input()

abc = list('abcdefghijklmnopqrstuvwxyz')

for i in abc:
    if i in s:
        print(s.index(i),end=' ')
    else:
        print("-1",end=' ')


