class Solution:
    def isHappy(self, n: int) -> bool:
        
        if len(str(n)) == 1:
            if n ==1 or n==7:
                return True
            else:
                return False
            
        ans = 0    
        for i in str(n):
            ans += int(i) ** 2
        return self.isHappy(ans)    
        
