import sys

A = sys.stdin.readline()[:-1]
B = sys.stdin.readline()[:-1]

if len(A) > len(B):
    A, B = B, A

lcs_length = [0] * len(A)
for i in range(len(B)):
    b = B[i]
    a = A[0]
    prev = lcs_length[0]
    if a == b and lcs_length[0] < 1:
        lcs_length[0] = 1
    for j in range(1, len(A)):
        a = A[j]
        max_ = max(lcs_length[j], lcs_length[j-1])
        if a == b:
            max_ = max(max_, prev+1)
        prev = lcs_length[j]
        lcs_length[j] = max_

print(lcs_length[-1])