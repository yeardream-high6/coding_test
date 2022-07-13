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

        def dfs(mask):
            # 이미 해본 조합인 경우 실패
            if visited[mask]:
                return False

            # 전체 남은 크기 계산
            rem = sum(
                stick
                for i, stick in enumerate(sticks)
                if mask & 1 << i
            )

            # 1개 변만 남았으면 성공
            if rem == target:
                return True

            # 현재 변의 남은 크기 계산
            rem %= target
            if rem == 0:
                rem = target

            # 남은 성냥 중 하나 선택해서 재귀호출
            for i, stick in enumerate(sticks):
                if mask & 1 << i and stick <= rem:
                    if dfs(mask ^ 1 << i):
                        return True

            visited[mask] = True
            return False
        
        return dfs((1 << n) - 1)

# 48.5 ms
print(Solution().makesquare([132, 131, 130, 7,  122, 121, 120, 37,  112, 111, 110, 66,  102, 101, 100, 98]))
# 11.3 ms
print(Solution().makesquare([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]))