# 개수 제일 많은 문자 찾는 걸로 착각했는데, 코딩마저 실수해서?! 
# 실수 + 실수 = 통과했습니다.
class Solution:
    def greatestLetter(self, s: str) -> str:
        letter_counter = {c: 0 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}

        greatest_num = 0
        greatest_ltter = ''
        for c in s:
            letter_counter[c] += 1
        
        for u, l in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'):
            if letter_counter[u] > 0 and letter_counter[l] > 0:
                cnt = letter_counter[u] + letter_counter[l]
                if cnt > greatest_num:
                    cnt = greatest_num # 이 부분 코딩 실수로 인해 통과됨
                    # 원래 의도는 greatest_num = cnt
                    greatest_ltter = u
        
        return greatest_ltter

    # 타인 코드
    def greatestLetter2(self, s: str) -> str:
        result = ""
        chars = set(s)
        
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch.upper() in chars and ch in chars:
                result = ch
        return result.upper()
