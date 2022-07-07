class Solution:
    def countAsterisks(self, s: str) -> int:
        return ''.join(s for i, s in enumerate(s.split('|')) if i % 2 == 0).count('*')


input_list = ["l|*e*et|c**o|*de|",
    "iamprogrammer",
    "yo|uar|e**|b|e***au|tifu|l"
    ]
for s in input_list:
    answer = Solution().countAsterisks(s)
    print(answer)