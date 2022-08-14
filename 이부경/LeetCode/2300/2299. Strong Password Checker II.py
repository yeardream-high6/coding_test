class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        one_lowercase = False
        one_uppercase  = False
        one_digit  = False
        one_special_character  = False

        prev_p = ''
        for p in password:
            if not one_lowercase:
                if 97 <= ord(p) <= 122:
                    one_lowercase = True
            if not one_uppercase:
                if 65 <= ord(p) <= 90:
                    one_uppercase = True
            if not one_digit:
                if 48 <= ord(p) <= 57:
                    one_digit = True
            if not one_special_character:
                if p in "!@#$%^&*()-+":
                    one_special_character = True
            
            if prev_p == p:
                return False
            prev_p = p

        return one_lowercase & one_uppercase & one_digit & one_special_character

answer = Solution().strongPasswordCheckerII("11A!A!Aa")
print(answer)
    
input_list = ["IloveLe3tcode!",
    "Me+You--IsMyDream",
    "1aB!",
    "a1A!A!A!",
    "11A!A!Aa"
    ]
for s in input_list:
    answer = Solution().strongPasswordCheckerII(s)
    print(answer)