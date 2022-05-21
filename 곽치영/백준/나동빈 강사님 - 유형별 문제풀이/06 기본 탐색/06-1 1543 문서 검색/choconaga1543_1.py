import re
doc = input()
word = input()
print(len(re.findall(word, doc)))