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

        # 같은 변에서 성냥 순서는 상관없으므로 직전i 보다 작은 i는 볼 필요가 없음
        # start_i로 시작 위치를 넘겨줌. 약간 빨라짐.
        def dfs(mask, start_i, num_sides, curr_rem):
            if visited[mask]:
                return False
            
            if curr_rem == 0:
                curr_rem = target
                num_sides -= 1
                start_i = 0

            if num_sides == 1:
                return True

            for i in range(start_i, n):
                if mask & 1 << i and sticks[i] <= curr_rem:
                    if dfs(mask ^ 1 << i, i + 1, num_sides, curr_rem - sticks[i]):
                        return True
                    # 핵심1. 새로운 변에 처음 넣은 성냥은 바꿔볼 필요가 없음. 어차피 어딘가 넣어야함.
                    # 핵심2. 남은 크기와 딱 맞는 성냥을 해봤으면 나머지는 해볼 필요가 없음. 어차피 손해.
                    # 여기서 10배정도 빨라짐
                    if curr_rem == target or curr_rem == sticks[i]:
                        return False

            visited[mask] = True
            return False
        
        return dfs((1 << n) - 1, 0, 4, target)

# 913 us
print(Solution().makesquare([132, 131, 130, 7,  122, 121, 120, 37,  112, 111, 110, 66,  102, 101, 100, 98]))
# 576 us
print(Solution().makesquare([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]))