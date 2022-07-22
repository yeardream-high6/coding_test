from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
        ord_a = ord('a')
        
        n = len(s)
        jump = [[None] * len(alphabets) for _ in range(n+1)]
        for i, c in enumerate(s):
            code = ord(c) - ord_a
            for j in range(i, 0, -1):
                jump[j][code] = i + 1
                if c == s[j-1]:
                    break
            else:
                jump[0][code] = i + 1
        
        ans = 0
        for word in words:
            j = 0
            for c in word:
                j = jump[j][ord(c)-ord_a]
                if j is None:
                    break
            else:
                ans += 1
        
        return ans