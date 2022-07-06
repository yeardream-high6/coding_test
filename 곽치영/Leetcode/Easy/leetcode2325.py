from typing import List

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        for c in key:
            if c not in mapping:
                mapping[c] = chr(ord('a') + i)
                i += 1
        return ''.join(map(lambda c: mapping[c], message))

print(Solution().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))