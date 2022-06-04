import sys

def solve(lst):    
    stack = []
    result = []
    i = 1
    n = len(lst)

    for target in lst:
        while not(stack and stack[-1] == target):
            if i > n:
                return "NO"
            result.append('+')
            stack.append(i)
            i += 1
        result.append('-')
        stack.pop()
    
    return '\n'.join(result)

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    lst = [None] * n

    for i in range(n):
        lst[i] = int(input())

    print(solve(lst))