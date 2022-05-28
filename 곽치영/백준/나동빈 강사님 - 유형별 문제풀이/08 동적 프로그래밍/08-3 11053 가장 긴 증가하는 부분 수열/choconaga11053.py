from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# min_last_of_length[length] = min(last value of subseq where length=length)
min_last_of_length = []

for a in A:
    idx = bisect_left(min_last_of_length, a)
    if idx == len(min_last_of_length):
        min_last_of_length.append(a)
    else:
        min_last_of_length[idx] = a

print(len(min_last_of_length))
