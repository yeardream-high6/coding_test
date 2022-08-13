class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(c.lower() for c in s if c.isalnum())
        return s2 == s2[::-1]

print(Solution().isPalindrome("0P"))

# 타인 코드
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = deque(filter(str.isalnum, s.lower()))
        while len(s) >=2:
            left, right = s.popleft(), s.pop()
            if left != right:
                return False
        return True