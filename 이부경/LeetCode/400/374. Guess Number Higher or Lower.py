from bisect import bisect_left

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        last = 2 ** 31 - 1
        
        while True:
            ret = guess(n)
            if ret < 0:
                last = n - 1
                n = (start + last) // 2
            elif ret > 0:
                start = n + 1
                n = (start + last) // 2
            else:
                break
            
        return n
    
class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(1, n + 1), 0, key=lambda x: guess(x)) + 1