import sys
sys.stdin=open("input.txt", "rt")

n,r,c=map(int,input().split())

def solve(n,r,c):
    size = (2**n)**2
    block = int(size/4) #배열을 4등분하여 블럭을 구분
    cnt = 0
    route = 2**(n-1)
    if n==1:
        if r==0 and c==0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3
    else:
        if r < (2**(n-1)):
            if c < (2**(n-1)):  # 1block
                cnt += 0
                cnt += solve(n - 1, r, c)
            else:  # 2block
                cnt += block
                cnt += solve(n - 1, r, c - route)
        else:
            if c < (2**(n-1)):  # 3block
                cnt += (2 * block)
                cnt += solve(n - 1, r - route, c)
            else:  # 4block
                cnt += (3 * block)
                cnt += solve(n - 1, r - route, c - route)
        return cnt


print(solve(n,r,c))
