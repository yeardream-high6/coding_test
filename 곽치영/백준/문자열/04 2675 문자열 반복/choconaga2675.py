T = int(input())
for _ in range(T):
    line = input()
    R, S = line.split()
    R = int(R)
    print("".join([c * R for c in S]))