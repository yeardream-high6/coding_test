class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c1_dict = dict()
        c2_dict = dict()
        
        for c1, c2 in zip(s, t):
            if c1 not in c1_dict:
                c1_dict[c1] = c2
            if c2 not in c2_dict:
                c2_dict[c2] = c1
            
            if c1_dict[c1] != c2 or c2_dict[c2] != c1:
                return False
        return True
    
# 타인 풀이
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))