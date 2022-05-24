import sys
sys.stdin=open("input.txt", "rt")

# 시간초과
n = int(input())

def Fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)

print (Fibo(n))