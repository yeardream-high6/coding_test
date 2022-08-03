import math

class Solution:
    def mySqrt(self, x: int) -> int:
        def f(start, last):
            i = (last - start) // 2 + start
            if last == start:
                return i if i * i == x else i - 1
            if i * i > x:
                return f(start, i)
            else:
                return f(i+1, last)
        return f(0, x)
    
import time
start = time.time()  # 시작 시간 저장
for i in range(2**20):
    a = math.floor(math.sqrt(i))
    b = Solution().mySqrt(i)
    if a != b:
        print(i, a, b, sep=', ')
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간