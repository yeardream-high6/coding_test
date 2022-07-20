from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        num_matching = 0
        for word in words:
            index = 0
            for w in word:
                index = s.find(w, index)
                if index == -1:
                    break
                index += 1
            if index >= 0:
                num_matching += 1
                #print(word)
        return num_matching



s = "abcde"
words = ["a","bb","acd","ace"]
a = Solution().numMatchingSubseq(s, words)
print(a)