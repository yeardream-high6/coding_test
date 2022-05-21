import sys

def solve(keylog):
    before_cursor = []
    after_cursor = []

    for key in keylog:
        if key == '-':
            if before_cursor:
                before_cursor.pop()
        elif key == '<':
            if before_cursor:
                after_cursor.append(before_cursor.pop())
        elif key == '>':
            if after_cursor:
                before_cursor.append(after_cursor.pop())
        else:
            before_cursor.append(key)

    password = ''.join(before_cursor) + ''.join(reversed(after_cursor))
    return password

if __name__ == '__main__':
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        keylog = input().strip()
        print(solve(keylog))
