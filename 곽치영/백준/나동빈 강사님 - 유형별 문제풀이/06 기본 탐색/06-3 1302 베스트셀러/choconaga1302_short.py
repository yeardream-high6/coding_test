import sys
next(sys.stdin)
counter = {}
for name in map(str.strip,sys.stdin):
    counter[name] = counter.get(name, 0) + 1
print(min(counter.items(), key=lambda p:(-p[1], p[0]))[0])
