# 솔루션 설명보고 풀었습니다.
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        
        memo = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            memo[i][0] = 1
            for j in range(1, k + 1):
                memo[i][j] = sum(memo[i-1][max(0, j - i + 1):j + 1]) % MOD
        return memo[n][k]

import itertools    
class Solution2:
    # Time Limit Exceeded (n = 10, k = 2)
    def kInversePairs(self, n: int, k: int) -> int:
        M = 1_000_000_007
        
        answer = 0
        for arr in itertools.permutations(range(1, n + 1), n):
            count = 0
            for i, j in ((i, j) for i in range(n - 1) for j in range(i + 1, n)):
                if arr[i] > arr[j]:
                    count += 1
                if count > k:
                    break
            
            if count == k:
                answer = (answer + 1) % M
                #print(arr)
        
        return answer

answer = Solution().kInversePairs(n = 3, k = 0)
print(answer)
answer = Solution().kInversePairs(n = 3, k = 1)
print(answer)
answer = Solution().kInversePairs(n = 10, k = 2)
print(answer)
