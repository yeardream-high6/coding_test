
# 시간초과
import random
import sys

def k_smallest(lst, k):
    start = 0
    stop = len(lst)
    while True:
        #print(lst, start, stop)
        pivot = lst[start]
        left = start + 1
        right = stop - 1
        while True:
            while lst[right] > pivot:
                right -= 1
            while left < right and lst[left] <= pivot:
                left += 1
            if left < right:
                lst[left], lst[right] = lst[right], lst[left]
            else:
                lst[start], lst[right] = lst[right], lst[start]
                break
        if k < right:
            stop = right
        elif right < k:
            start = right + 1
        else:
            return lst[right]

if __name__ == '__main__':
    input = sys.stdin.readline

    N, K = map(int, input().split())
    lst = [int(s) for s in input().split()]

    random.seed(42)
    random.shuffle(lst)

    print(k_smallest(lst, K-1))