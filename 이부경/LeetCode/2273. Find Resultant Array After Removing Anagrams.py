from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer = []
        
        prev_w = ''
        for w in words:
            if prev_w != sorted(w):
                answer.append(w)
            
            prev_w = sorted(w)
        return answer