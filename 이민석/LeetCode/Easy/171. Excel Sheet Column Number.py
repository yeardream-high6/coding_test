class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        len_t=len(columnTitle)
        for i in range(0,len_t):
            num = ord(columnTitle[i])-64 
            ans = 26*ans + num
        return ans
