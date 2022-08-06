# method 1 : Using list comprehension and defaultdict
import collections
import re

def mostCommonword1(self, paragraph:str, banned:list(str)) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts += 1
    return max(counts, key = counts.get)            





# method 2 : Using list comprehension and Counter
def mostCommonWord2(self, paragraph:str, banned:list(str)) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
