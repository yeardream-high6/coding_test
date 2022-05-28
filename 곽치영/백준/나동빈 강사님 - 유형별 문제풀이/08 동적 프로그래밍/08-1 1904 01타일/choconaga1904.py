# fibo(2n+1), fibo(2n) = fibo(n+1)^2 + fibo(n)^2, fibo(n-1) (2 fibo(n) - fibo(n-1))

def fibo_pair(n):
    """
    return fibo(n), fibo(n+1) pair
    """
    if n == 0:
        return 0, 1

    m = n // 2
    fm, fm1 = fibo_pair(m)
    f2m, f2m1 = fm * (fm1 + fm1 - fm), fm1*fm1 + fm*fm

    if n % 2 == 0:
        fn, fn1 = f2m, f2m1
    else:
        fn, fn1 = f2m1, f2m1 + f2m
    
    return fn % 15746, fn1 % 15746

# fibo(N+1)
print(fibo_pair(int(input()))[1])
