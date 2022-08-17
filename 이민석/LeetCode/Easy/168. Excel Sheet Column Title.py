class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ""
        while columnNumber>0:
            columnNumber -= 1
            a += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return a[::-1]
