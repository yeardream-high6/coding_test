class Solution:
    def __init__(self):
        self.memo = [0] * 46
        self.memo[1] = 1
        self.memo[2] = 2
        for i in range(3, 46):
            self.memo[i] = self.memo[i-2] + self.memo[i-1]
    
    def climbStairs(self, n: int) -> int:
        return self.memo[n]

        
a = Solution().climbStairs(4)
print(a)

a = Solution().climbStairs(5)
print(a)