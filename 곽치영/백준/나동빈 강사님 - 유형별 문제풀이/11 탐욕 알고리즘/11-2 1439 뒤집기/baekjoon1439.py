def count_groups(string: str) -> int:
    prev = None
    cnt = 0
    for char in string:
        if char != prev:
            prev = char
            cnt += 1
    return cnt

S = input()
answer = count_groups(S) // 2
print(answer)
