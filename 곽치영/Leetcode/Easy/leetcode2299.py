class Solution:
    LOWERCASE_LETTERS = {chr(i) for i in range(ord('a'), ord('z')+1)}
    UPPERCASE_LETTERS = {chr(i) for i in range(ord('A'), ord('Z')+1)}
    DIGITS = set("0123456789")
    SPECIAL = set("!@#$%^&*()-+")
    def strongPasswordCheckerII(self, password: str) -> bool:
        lowercase = 0
        uppercase = 0
        digit = 0
        special = 0
        adjacent = 0
        prev = None
        for char in password:
            if char in Solution.LOWERCASE_LETTERS:
                lowercase += 1
            if char in Solution.UPPERCASE_LETTERS:
                uppercase += 1
            if char in Solution.DIGITS:
                digit += 1
            if char in Solution.SPECIAL:
                special += 1
            if prev == char:
                adjacent += 1
            prev = char
        return (
            len(password) >= 8
            and lowercase >= 1
            and uppercase >= 1
            and digit >= 1
            and special >= 1
            and adjacent == 0
        )