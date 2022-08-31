from typing import *

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            output[i] = i.bit_count()
        
        return output

# 타인 풀이
class Solution:
    def countBits(self, n: int) -> List[int]:
        # two cases
        # if number is odd, number // 2 + one extra zero
        # 0101 -> 5
        # 0010 -> 2
        
        # if number is even, same number of ones
        # 0100 -> 4
        # 0010 -> 2
        
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1:
                a[i] = a[i // 2] + 1
            else:
                a[i] = a[i // 2]
        return a