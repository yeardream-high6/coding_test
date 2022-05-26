import sys
sys.stdin=open("input.txt", "rt")

N = int(input())
book={}

for _ in range(N):
    a=input()
    if a not in book:
        book[a]=1
    else:
        book[a]+=1

list = []
ans=max(book.values())

for i in book:
    if ans==book[i]:
        list.append(i)
list.sort()
print(list[0])
