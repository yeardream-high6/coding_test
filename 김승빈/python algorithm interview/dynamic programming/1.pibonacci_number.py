# method 1: recursive structure, brute-force
def fib(self, N: int) -> int:
    if N <= 1:
        return N
    return self.fib(N - 1) + self.fib(N - 2)


# method 2: memoization
import collections
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]


# method 3: tabulation
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]


# method 4: using only two variables
def fib(self, N: int) -> int:
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x
    

# method 5: matrix
import numpy as np
def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]