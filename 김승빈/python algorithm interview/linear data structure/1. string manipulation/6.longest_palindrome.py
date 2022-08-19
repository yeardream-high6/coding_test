# A solution expanding around the center
# different from 'longest commom substring' using dynamic programming
# 2 two-pointer for both even and odd size of array

def longestPalindrome(self, s:str) -> str:
    def expand(left:int, right:int) -> str:
        if left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 and s == s[::-1]:
        return s
    
    result = ''
    for i in range(len(s) -1):
        result = max(result,
                        expand(i, i+1),
                        expand(i, i+2),
                        key = len)
    return result


