# 157ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        digits = []
        
        while x:
            digits.append(x % 10)
            x //= 10
        for a, b in zip(digits, reversed(digits)):
            if a != b:
                break
        else:
            return True
        return False

# 150ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for a, b in zip(s, reversed(s)):
            if a != b:
                return False
        return True

# 115ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True

# 72ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        h = len(s) // 2
        return s[:h] == s[-1:n-1-h:-1]

# 80ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
