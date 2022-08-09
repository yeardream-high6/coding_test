def get_start_num(n):
    return max(n - len(str(n)) * 10, 0)

def find_smallest_generator(n):
    for i in range(get_start_num(n), n + 1):
        if n == i + sum(map(int, str(i))):
            return i
    return 0

N = int(input())
a = find_smallest_generator(N)
print()