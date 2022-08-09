class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if len(stack) == 0:
                    return False
                bracket = stack.pop() + c
                if bracket not in "(){}[]":
                    return False
        return len(stack) == 0

a = Solution().isValid(s = "()[]{}")
print(a)