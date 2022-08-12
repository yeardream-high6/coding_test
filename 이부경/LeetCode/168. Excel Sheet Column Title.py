class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = []
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            c = chr(ord('A') + columnNumber % 26)
            column.append(c)
            columnNumber = columnNumber // 26

        return ''.join(column[::-1])


# ZY
a = Solution().convertToTitle(701)
print(a)

# AB
a = Solution().convertToTitle(28)
print(a)
