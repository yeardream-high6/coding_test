import sys
sys.stdin=open("input.txt", "rt")

def trophy(t):
    max = 0
    cnt = 0
    for i in t:
        if max < i:
            max = i
            cnt += 1
    return cnt


N = int(input())
t = []

for i in range(N):
    t.append(int(input()))

print(trophy(t))
print(trophy(reversed(t)))