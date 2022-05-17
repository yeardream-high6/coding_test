import sys
input = sys.stdin.readline

MAX_K = 14
MAX_N = 14

people_counts = [[None] * (MAX_N+1) for _ in range(MAX_K+1)]

for n in range(MAX_N+1):
    people_counts[0][n] = n

for k in range(1, MAX_K+1):
    people_counts[k][0] = 0
    for n in range(1, MAX_N+1):
        people_counts[k][n] = people_counts[k-1][n] + people_counts[k][n-1]

# for k in range(MAX_K):
#     print(people_counts[k])

T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    print(people_counts[k][n])