from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices) + [0]
        min_price = prices[0]
        for i in range(len(prices)):
            dp[i] = prices[i] - min_price
            if min_price > prices[i]:
                min_price = prices[i]

        return max(dp)
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if max_profit < profit:
                max_profit = profit
            if min_price > prices[i]:
                min_price = prices[i]

        return max_profit

prices = [5, 10, 4, 8]
a = Solution().maxProfit(prices)
print(a)