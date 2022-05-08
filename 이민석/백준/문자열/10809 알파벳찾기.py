import sys
sys.stdin=open("input.txt", "rt")

str=list(map(int, input().split()))
s=[]
for i in range(ord('a'),ord('z')+1):
    for j in ord('z')-ord('a')+1:
        if i==ord(str[j]):



