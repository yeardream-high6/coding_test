import sys
input = sys.stdin.readline

def solve(lst):
    for i in range(1, len(lst)):
        if not lst[i-1] < lst[i]:
            break
    else:
        return 'ascending'
    
    for i in range(1, len(lst)):
        if not lst[i-1] > lst[i]:
            break
    else:
        return 'descending'
    
    return 'mixed'

lst = list(map(int, input().split()))
print(solve(lst))
