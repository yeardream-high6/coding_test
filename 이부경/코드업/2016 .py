n = int(input())
s = input()
stack = []
for i, n in enumerate(s[::-1]):
    if i > 1 and i % 3 == 0:
        stack.append(',')
    stack.append(n)
while stack:
    print(stack.pop(), end='')
print()