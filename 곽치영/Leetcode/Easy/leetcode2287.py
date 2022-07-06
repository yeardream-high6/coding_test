from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counter = Counter(s)
        return min(s_counter[c] // count for c, count in Counter(target).items())
