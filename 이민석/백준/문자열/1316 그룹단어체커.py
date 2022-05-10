import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
cnt = n

for _ in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)