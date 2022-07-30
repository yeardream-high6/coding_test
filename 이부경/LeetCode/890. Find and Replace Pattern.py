from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        
        for word in words:
            # pattern, word 각각 dict를 만들어서 서로 dict에서 일치하는지 확인하였습니다.
            p_dict = {}
            w_dict = {}
            for p, w in zip(pattern, word):
                # p_dict
                if w in p_dict:
                    if p_dict[w] != p:
                        break
                else:
                    p_dict[w] = p

                # w_dict
                if p in w_dict:
                    if w_dict[p] != w:
                        break
                else:
                    w_dict[p] = w
                    
            else:
                output.append(word)
        return output
    
# Output: ["mee","aqq"]
a = Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb")
print(a)

a = Solution().findAndReplacePattern(words = ["a","b","c"], pattern = "a")
print(a)