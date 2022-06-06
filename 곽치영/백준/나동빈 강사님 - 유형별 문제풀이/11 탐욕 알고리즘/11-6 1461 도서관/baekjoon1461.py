import sys

# books: descending
def get_sum_walk(books):
    sum_walk = 0
    cnt_books = M

    for pos in books:
        if pos < 0:
            break

        cnt_books += 1
        if cnt_books > M:
            cnt_books -= M
            sum_walk += pos
    
    return sum_walk

read_line = sys.stdin.readline

N, M = map(int, read_line().split())
books = sorted(map(int, read_line().split()))

walks = get_sum_walk(reversed(books)) + get_sum_walk(map(lambda x: -x, books))
save_last_return = max(-min(books), max(books))
walks = walks * 2 - save_last_return

print(walks)
