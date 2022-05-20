import functools

@functools.cache
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n>1 else n

n = int(input())
print(fibo(n))