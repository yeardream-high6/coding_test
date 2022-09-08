class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in s:
            i = t.find(c, i)
            if i < 0:
                return False
            i += 1
        return True