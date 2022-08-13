class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        m = 1
        for c in columnTitle[::-1]:
            n = ord(c) - ord('A') + 1
            total += n * m
            m *= 26
        return total
