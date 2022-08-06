import collections


def groupAnagrams(self, strs:list(str)) -> list(list(str)):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


# sort() method in list data type : in-lpace-sort, override input values, no return

# sorted() method : 'key=' option
a = ['cde', 'cfc', 'abc']
sorted(a, key=lambda s:(s[0], s[-1])) # 1st : s[0], 2nd : s[-1]

