import re
alphabet_matchs =re.compile('c=|c-|dz=|d-|lj|nj|s=|z=|[a-z]').findall(input())
print(len(alphabet_matchs))