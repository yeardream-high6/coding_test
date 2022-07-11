from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(target)
        return min(map(lambda c: counter_s[c] // counter_t[c], counter_t))


s = ["ilovecodingonleetcode", # 2 
    "abcba", # 1
    "abbaccaddaeea" # 1
    ]
target = ["code" ,
    "abc",
    "aaaaa"
    ]
for i in range(len(s)):
    answer = Solution().rearrangeCharacters(s[i], target[i])
    print(answer)