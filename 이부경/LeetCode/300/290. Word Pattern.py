class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p_dict = dict()
        w_dict = dict()
        for p, w in zip(pattern, words):
            if p not in p_dict:
                p_dict[p] = w
            if w not in w_dict:
                w_dict[w] = p
            if p_dict[p] != w or w_dict[w] != p:
                return False
        return True
                

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p, w = pattern, s.split()
        return len(p) == len(w) and len(set(p)) == len(set(w)) == len(set(zip(p, w)))