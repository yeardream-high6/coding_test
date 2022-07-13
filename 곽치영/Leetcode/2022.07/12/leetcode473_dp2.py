from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        sticks = sorted(matchsticks, reverse=True)

        target = total // 4
        n = len(sticks)

        visited = [False] * (1 << n)

        # sum을 매번 새로 계산하는 대신 차이로 계산해서 인자로 넘겨줌. 2배 빨라짐.
        def dfs(mask, num_sides, curr_rem):
            if visited[mask]:
                return False
            
            if curr_rem == 0:
                curr_rem = target
                num_sides -= 1

            if num_sides == 1:
                return True

            for i, stick in enumerate(sticks):
                if mask & 1 << i and stick <= curr_rem:
                    if dfs(mask ^ 1 << i, num_sides, curr_rem - stick):
                        return True

            visited[mask] = True
            return False
        
        return dfs((1 << n) - 1, 4, target)

# 26.2 ms
print(Solution().makesquare([132, 131, 130, 7,  122, 121, 120, 37,  112, 111, 110, 66,  102, 101, 100, 98]))
# 5.89 ms
print(Solution().makesquare([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]))