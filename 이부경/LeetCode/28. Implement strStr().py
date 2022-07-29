class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

a = Solution().strStr(haystack = "hello", needle = "ll")
print(a)