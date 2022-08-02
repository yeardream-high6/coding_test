def f(position):
    x = int(position[1])
    y = ord(position[0].upper()) - ord('A') + 1
    
    count = 0
    
    # 8가지 경우의 수(up, down, left, right)
    dx = [-2, -2, +2, +2, -1, +1, -1, +1]
    dy = [-1, +1, -1, +1, -2, -2, +2, +2]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            count += 1
    return count 
    
position = 'a1'
print(f(position))


# 책 풀이
def f2():
    location = input()
    x = int(location[1])
    y = ord(location[0]) - ord('a') + 1

    count = 0
    directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for d in directions:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        else:
            count += 1