count = 0
for i in range(24*60*60):
    s = i % 60
    m = i // 60 % 60
    h = i // 60 // 60

    if s == 3 or m == 3 or h == 3:
        count +=1
print(count)

# 책 풀이
n = int(input())
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h)+str(m)+str(s)
            if '3' in time:
                cnt += 1
