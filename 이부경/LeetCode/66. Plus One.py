from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        else:
            return [1] + digits
        
        return digits

a = Solution().plusOne([4,3,2,2])
print(a)