from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for i in range(min(map(len, strs))):
            c = strs[0][i]
            if any(map(lambda x: x[i] != c, strs[1:])):
                return output
            output += c
        
        return output

a = Solution().longestCommonPrefix(["flower"])
print(a)