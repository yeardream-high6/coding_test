from typing import *

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            tax += (min(income, upper) - prev) * percent / 100
            prev = upper
        return tax