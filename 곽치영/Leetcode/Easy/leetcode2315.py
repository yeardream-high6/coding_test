class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        for i, substr in enumerate(s.split('|')):
            if i % 2 == 0:
                answer += substr.count('*')
        return answer