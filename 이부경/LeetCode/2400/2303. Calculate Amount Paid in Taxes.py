from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = .0       
        i = 0
        prev_upper = 0
        while(income > 0) and i < len(brackets):
            dollar = min(brackets[i][0] - prev_upper, income)
            tax_rate = brackets[i][1] / 100
            tax += dollar * tax_rate
            
            income -= dollar
            prev_upper = brackets[i][0]
            i += 1
        return tax


brackets = [[[3,50],[7,10],[12,25]],
            [[1,0],[4,25],[5,50]],
            [[2,50]]
            ]
income = [10, 2, 0]

for i in range(len(income)):
    answer = Solution().calculateTax(brackets[i], income[i])
    print(answer)    