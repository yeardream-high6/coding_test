from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target_length = sum(matchsticks) // 4
        
        if target_length % 1 > 0:
            return False
        
        if any(map(lambda x: x > target_length, matchsticks)):
            return False
        
        def f(matchsticks, target_length):
            if len(matchsticks) == 0:
                return True

            combi_list = []
            for i in range(2 ** len(matchsticks)):
                on_off = bin(i)[2:].zfill(len(matchsticks)) # index bit mask
                #print(on_off)
                combi = []
                for j in range(len(matchsticks)):
                    if on_off[j:j+1] == '1':
                        combi.append(matchsticks[j])
                if target_length == sum(combi):
                    #print(combi)
                    if not combi in combi_list:
                        combi_list.append(combi)
                        m = matchsticks.copy()
                        for c in combi:
                            m.remove(c)
                        if f(m, target_length):
                            return True        
            return False
        
        matchsticks = sorted(matchsticks, reverse = True)
        return f(matchsticks, target_length)

matchsticks  = [
    [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100], #f
    [13,11,1,8,6,7,8,8,6,7,8,9,8], #t
    [2,2,2,3,4,4,4,5,6], #t
    [5,5,5,5,4,4,4,4,3,3,3,3], #t
    [1,1,2,2,2], #t
    [3,3,3,3,4] #f
    ]


for i in range(len(matchsticks)):
    match_times = 0
    answer = Solution().makesquare(matchsticks[i])
    print(answer)
