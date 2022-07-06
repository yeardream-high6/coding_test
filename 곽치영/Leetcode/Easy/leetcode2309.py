from typing import List

class Solution:
    alphabets = [(chr(i), chr(i).lower()) for i in range(ord('A'), ord('Z')+1)]
    def greatestLetter(self, s: str) -> str:
        for upper, lower in reversed(self.alphabets):
            if upper in s and lower in s:
                break
        else:
            return ""
        return upper

print(Solution().greatestLetter("lEeTcOdE"))