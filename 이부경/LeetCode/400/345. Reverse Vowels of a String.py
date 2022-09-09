class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        vowel_index = [i for i, c in enumerate(s) if c in vowels]
        vowel_index_reversed = vowel_index[::-1]
        n = len(vowel_index) // 2
        s_list = list(s)
        for i, j in zip(vowel_index[:n], vowel_index_reversed[:n]):
            s_list[i], s_list[j] = s_list[j], s_list[i]
        
        return ''.join(s_list)