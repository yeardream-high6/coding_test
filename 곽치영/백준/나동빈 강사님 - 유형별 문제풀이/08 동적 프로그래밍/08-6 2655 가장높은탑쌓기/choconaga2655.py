import sys
input = sys.stdin.readline

N = int(input())

# bricks[i] = (area, height, weight, index)
AREA = 0
HEIGHT = 1
WEIGHT = 2
INDEX = 3
bricks = [None] * N

for i in range(N):
    area, height, weight = tuple(map(int, input().split()))
    bricks[i] = area, height, weight, i+1

bricks.sort(key=lambda brick: brick[AREA], reverse=True)

best_heights = [None] * N
best_prevs = [None] * N

for i in range(N):
    curr_height = bricks[i][HEIGHT]
    curr_weight = bricks[i][WEIGHT]

    curr_best_height  = curr_height
    curr_best_prev = None

    for j in range(i):
        if bricks[j][WEIGHT] > curr_weight and curr_best_height < best_heights[j] + curr_height:
            curr_best_height = best_heights[j] + curr_height
            curr_best_prev = j
    
    best_prevs[i] = curr_best_prev
    best_heights[i] = curr_best_height

max_best_height = max(best_heights)
max_best_index = best_heights.index(max_best_height)

answer = []
i = max_best_index
while i is not None:
    answer.append(bricks[i][INDEX])
    i = best_prevs[i]

print(len(answer))
print(*answer, sep='\n')
