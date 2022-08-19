class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n > 1:
            if n in history:
                return False
            history.add(n)
            
            n = sum(int(c) * int(c) for c in  str(n))
        
        return True