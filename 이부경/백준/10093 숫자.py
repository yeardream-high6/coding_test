a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(max(b - a - 1, 0))
print(*[i for i in range(a + 1, b)])