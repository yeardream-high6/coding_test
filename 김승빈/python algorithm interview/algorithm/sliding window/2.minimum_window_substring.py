from typing import *


# method 1: brute-force
def minWindow1(self, s: str, t: str) -> str:
    def contains(s_substr_lst: List, t_lst: List):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True
    
    if not s or not t:
        return ''
    
    window_size = len(t)

    for size in range(window_size, len(s) + 1):
        for left in range(len(s) - size + 1):
            s_substr = s[left:left + size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''


# method 2: two-pointer
import collections
def minWindow2(self, s: str, t: str) -> str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    # move right pointer
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]


# method 3: Counter
def minWindow3(self, s: str, t: str) -> str:
    t_count = collections.Counter(t)
    current_count = collections.Counter()

    start = float('-inf')
    end = float('inf')

    left = 0
    # move right pointer
    for right, char in enumerate(s, 1):
        current_count[char] += 1
        # move left pointer as a result of AND operation
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1
    
    return s[start:end] if end - start <= len(s) else ''