class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pd = ''.join(i for i in s if i.isalnum())
        return pd == pd[::-1]
