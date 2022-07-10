from functools import cache

# 8845 ms, faster than 5.02%
class Solution:
    def get_sub_p(self, p):
        i = 0
        non_asterisk = ''
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == '*':
                if len(non_asterisk) > 0:
                    return non_asterisk
                
                return '*' + p[i]
            else:
                non_asterisk += p[i]
                i += 1
        return non_asterisk
    
    def isMatch(self, s: str, p: str) -> bool:
        if (not s ) or len(s) == 0:
            return False
        
        i, j = 0, 0
        while j < len(p):
            sub_p = self.get_sub_p(p[j:])            
            
            if sub_p[:1] == '*': # asterisk pattern
                c = sub_p[1]                
                k = 0
                while k + i < len(s) and (s[k + i] == c or c =='.'):
                    k += 1
                for k2 in reversed(range(k + 1)):
                    if self.isMatch(s[i + k2:], p[j+2:]):
                        return True
                i += k
            else: # non asterisk pattern
                if len(s) - i < len(sub_p):
                    return False
                for k, c in enumerate(sub_p):
                    if c == '.':
                        continue
                    if s[i+ k] != c:
                        return False
                i += len(sub_p)
            j += len(sub_p)
            
        return i == len(s) and j == len(p)

# 타인 코드 27ms
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            if j+1 < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))

            return match and dfs(i+1, j+1)
        
        return dfs(0, 0)

s = ["a", # T
    "aaba" # F
    ]
p = ["ab*", 
    "ab*a*c*a"
    ]
# *...
for i in range(len(s)):
    answer = Solution().isMatch(s[i], p[i])
    print(answer)