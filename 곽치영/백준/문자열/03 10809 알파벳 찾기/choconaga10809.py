string = input()
count = [string.find(chr(i)) for i in range(ord('a'), ord('z')+1)]
print(*count)