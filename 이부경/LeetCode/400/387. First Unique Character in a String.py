from collections import Counter
from math import inf

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
    
# 타인 코드    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        res = inf
        for letter in abc:
            found = s.find(letter);
            if (found != -1 and found == s.rfind(letter)):
                res = min(res, found)
        return res if res < inf else -1
    
