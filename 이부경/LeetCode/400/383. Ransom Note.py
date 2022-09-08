from typing import *

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for k in r.keys():
            if r[k] > m[k]:
                return False
        return True