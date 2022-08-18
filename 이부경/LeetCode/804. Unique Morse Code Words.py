from typing import *

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_code_set = set() 
        for word in words:
            morse_code = ''.join(translation[ord(w) - ord('a')] for w in word)
            morse_code_set.add(morse_code)

        return len(morse_code_set)

# 타인 코드
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translate = {''.join([morse[ord(c)-97] for c in word]) for word in words}
        return len(translate)
