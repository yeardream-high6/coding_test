class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1줄 풀이
        # return bin(int(a, 2) + int(b, 2))[2:] 
        
        def to_int(s):
            total = 0
            for i, n in enumerate(s[::-1]):
                total += int(n) * 2**i
            return total
        
        def to_bin(n):
            if n == 0:
                return '0'
            s = ''
            while n > 0:
                s += '1' if n & 1 else '0'
                n = n // 2
            return s[::-1]
        
        n = to_int(a) + to_int(b)
        return to_bin(n)

a = Solution().addBinary(a = "11", b = "1")
print(a)

a = Solution().addBinary(a = "1010", b = "1011")
print(a)