from typing import *
from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def get_time(led_on):
            led = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
            h, m = 0, 0
            for i in led_on:
                if i > 5:
                    h += led[i]
                else:
                    m += led[i]
            
            if h < 12 and m < 60:
                return str(h) + ":" + str(m).zfill(2)
            else:
                return None

        output = []
        for led_on in combinations(range(10), turnedOn):
            t = get_time(led_on)
            if t:
                output.append(t)
        return output
    
# 타인 풀이
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        res=[]
        a=[bin(i).count("1")for i in range(60)]
        for h in range(12):
            hb=a[h]
            for m in range(60):
                mb=a[m]
                if hb+mb==turnedOn:
                    res.append(f"{h}:{m:02d}")      
    
    # 타인 풀이
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if str(bin(h)).count("1") + str(bin(m)).count("1") == turnedOn:
                    # 02d: Min two digits, and append 0 char at the left in case of less than 2 digits
                    result.append(f'{h}:{m:02d}')
        return result
    
    