from itertools import permutations

def solution(numbers):
    length = len(numbers)
    N = 10**length

    is_prime = [True] * N
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, N):
        if not is_prime[p]:
            continue
        for x in range(2*p, N, p):
            is_prime[x] = False
    
    primes = set()

    for perm in permutations(numbers+' '):
        cut = perm.index(' ')
        if cut == 0:
            continue
        num = int(''.join(perm[:cut]))
        if is_prime[num]:
            primes.add(num)
    
    return len(primes)

print(solution("4906078"))