class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print( bin(abs(n)).count('1'))
        return 

# 타인 코드
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0

a = Solution().isPowerOfTwo(4)
print(a)