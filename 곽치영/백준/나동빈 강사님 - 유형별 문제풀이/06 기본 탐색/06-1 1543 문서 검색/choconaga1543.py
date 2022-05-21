doc = input()
word = input()
len_word = len(word)

start = 0
cnt = 0
while True:
    start = doc.find(word, start)
    if start == -1:
        break
    start += len_word
    cnt += 1

print(cnt)