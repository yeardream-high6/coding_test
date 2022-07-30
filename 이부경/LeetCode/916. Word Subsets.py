from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        output = []
        w2_counter = Counter()
        for counter in [Counter(w2) for w2 in words2]:
            for c in counter:
                w2_counter[c] = max(w2_counter[c], counter[c])
                
        for word1 in words1:
            w1_counter = Counter(word1)
            for w2 in w2_counter:
                if w2_counter[w2] > w1_counter[w2]:
                    break
            else:
                output.append(word1)
        return output
    
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]
# Output: ["google","leetcode"]
a = Solution().wordSubsets(words1, words2)
print(a)