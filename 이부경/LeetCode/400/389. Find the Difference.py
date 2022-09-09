from typing import *

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(t) - Counter(s)
        return counter.most_common()[0][0]
    
# 타인 풀이
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s+t:
            ans ^= ord(c)
        return chr(ans)    