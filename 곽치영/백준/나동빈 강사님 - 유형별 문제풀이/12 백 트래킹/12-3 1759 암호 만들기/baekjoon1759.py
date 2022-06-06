from itertools import combinations

L, C = map(int, input().split())
alphabets = sorted(input().split())

for substr in combinations(alphabets, L):
    cnt_vowel = sum(1 if char in 'aeiou' else 0 for char in substr)
    cnt_consonant = L - cnt_vowel
    if cnt_vowel >= 1 and cnt_consonant >= 2:
        print(''.join(substr))
