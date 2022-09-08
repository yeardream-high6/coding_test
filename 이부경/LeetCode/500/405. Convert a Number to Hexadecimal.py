class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        hex = "0123456789abcdef"
        output = []
        for i in range(8):
            mask = 0xf << i * 4
            digit = (num & mask) >> i * 4
            output.append(hex[digit])
        while output[-1] == '0':
            output.pop()
        return ''.join(output[::-1])


#타인 풀이
class Solution:
    def toHex(self, num: int) -> str:
        if num==0: 
            return '0'
        s = '0123456789abcdef' 
        
        ans = ''
        for i in range(8):
            x=num & 15      
            temp =s[x]           
            ans = temp + ans
            num = num >> 4
            
        return ans.lstrip('0')