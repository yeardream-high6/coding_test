from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_ = sum(matchsticks)
        if sum_ % 4 != 0:
            return False

        sticks = sorted(matchsticks, reverse=True)

        target = sum_ // 4
        caps = [target] * 4
        n = len(sticks)

        def dfs(i):
            if i < n:
                for j in range(4):
                    if caps[j] >= sticks[i]:
                        caps[j] -= sticks[i]
                        if dfs(i+1):
                            return True
                        caps[j] += sticks[i]
                return False
            return True
        
        if caps[0] >= sticks[0]:
            caps[0] -= sticks[0]
            return dfs(1)
        else:
            return False

print(Solution().makesquare([9,9,9,9,9,9,9,9,9,9,9,9,9,9,2]))