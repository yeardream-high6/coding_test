nums = map(int, list(input()))
count = [0] * 9
for n in nums:
    if n == 9:
        n = 6
    count[n] += 1

count[6] = (count[6] + 1) // 2
print(max(count))