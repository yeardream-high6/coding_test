def is_group(word):
    occurred = set()
    last = ''
    for c in word:
        if c == last:
            continue
        if c in occurred:
            return False
        occurred.add(c)
        last = c
    return True

N = int(input())
cnt = 0
for _ in range(N):
    if is_group(input()):
        cnt += 1
print(cnt)