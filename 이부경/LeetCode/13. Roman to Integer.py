class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10, 
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
        
        prev = roman_nums[s[-1]]
        total = 0
        oper = '+' # '+' or '-'
        for c in reversed(s):
            current = roman_nums[c]
            if current < prev:
                oper = '-'
            elif current > prev:
                oper = '+'
            
            if oper == '+':
                total += current
            elif oper == '-':
                total -= current
            prev = current
        
        return total
    
# 타인 코드
class Solution2:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    
a = Solution().romanToInt("MCMXCIV")
print(a)