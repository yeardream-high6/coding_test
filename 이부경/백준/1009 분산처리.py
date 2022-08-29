T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    c = 1
    for _ in range(b):
        c = (c * a) % 10
    print(10 if c == 0 else c)