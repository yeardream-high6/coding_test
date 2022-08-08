import math

# 참고:
# https://leetcode.com/problems/mirror-reflection/discuss/2376355/Python3-oror-4-lines-geometry-w-explanation-oror-TM%3A-9281
# https://leetcode.com/problems/mirror-reflection/discuss/2377070/Pseudocode-Explain-Why-Odd-and-Even-Matter
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        
        L = math.lcm(p, q)
        
        if (L // p) % 2 == 0: # stacked box is even
            return 0
        
        if (L // q) % 2 == 0:
            return 2
        else:
            return 1
        

# 타인 코드
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        L = math.lcm(p,q)
        if (L//q)%2 == 0:
            return 2
        return (L//p)%2