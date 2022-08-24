class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(s) for s in str(num))
        return num