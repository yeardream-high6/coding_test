from collections import defaultdict

def reverse_dir(direction):
    return (direction + 4) % 8

def iter_clock_dir(direction):
    for i in range(8):
        yield (direction + i + 1) % 8

def solution(arrows):
    # 대각선이 만나는 점을 표현하기 위해 격자 단위를 2로 합니다.
    arrow_step = [
        [(0, 2)],
        [(1, 1), (1, 1)],
        [(2, 0)],
        [(1, -1), (1, -1)],
        [(0, -2)],
        [(-1, -1), (-1, -1)],
        [(-2, 0)],
        [(-1, 1), (-1, 1)],
    ]
    
    # edge[x, y][direction] = nx, ny, [visited]
    edge = defaultdict(lambda: [None] * 8)
    
    x, y = 0, 0
    for direction in arrows:
        for dx, dy in arrow_step[direction]:
            nx, ny = x + dx, y + dy
            edge[x, y][direction] = nx, ny, [False]
            edge[nx, ny][reverse_dir(direction)] = x, y, [False]
            x, y = nx, ny
    
    # for (x,y), arr in edge.items():
    #     print(x, y, arr)
    
    num_areas = 0
    
    for (x,y), out_arrows in edge.items():
        for direction, out_arrow in enumerate(out_arrows):
            if out_arrow is None:
                continue
            (_, _, [visited]) = out_arrow
            if not visited:
                num_areas += 1
                cx, cy, c_dir = x, y, direction
                while True:
                    nx, ny, ref_visited = edge[cx, cy][c_dir]
                    if ref_visited[0]:
                        break
                    ref_visited[0] = True
                    
                    cx, cy, c_dir = nx, ny, reverse_dir(c_dir)
                    c_out_arrows = edge[cx, cy]
                    for next_dir in iter_clock_dir(c_dir):
                        if c_out_arrows[next_dir] is not None:
                            break
                    c_dir = next_dir
    
    return num_areas - 1
