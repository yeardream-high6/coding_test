# 다른 사람 풀이를 보니깐 스택으로 훨씬 간단하게 풀 수 있는 문제였네요.

from collections import Counter

def solution(number, k):
    number = list(map(int, number))
    answer = []

    left = 0
    right = k

    counter = [0] * 10
    for i in range(k):
        counter[number[i]] += 1
    
    for right in range(k, len(number)):
        num = number[right]
        counter[num] += 1
        for i in range(9, 0-1, -1):
            if counter[i] != 0:
                break
        else:
            assert False
        answer.append(i)
        while number[left] != i:
            counter[number[left]] -= 1
            left += 1
        counter[number[left]] -= 1
        left += 1
    
    return ''.join(map(str,answer))
