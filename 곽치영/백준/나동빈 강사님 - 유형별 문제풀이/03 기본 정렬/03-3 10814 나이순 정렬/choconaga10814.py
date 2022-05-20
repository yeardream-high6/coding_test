import sys
input = sys.stdin.readline

N = int(input())
members = [None] * N

for i in range(N):
    age, name = input().split()
    members[i] = (int(age), name)

# python sort는 stable합니다. (Timsort: https://d2.naver.com/helloworld/0315536)
print(*map(
    lambda p: f"{p[0]} {p[1]}",
    sorted(members, key=lambda m: m[0])
    ), sep='\n')