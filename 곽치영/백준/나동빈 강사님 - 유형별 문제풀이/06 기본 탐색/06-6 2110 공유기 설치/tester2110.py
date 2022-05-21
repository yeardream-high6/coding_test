import choconaga2110
import random

MAX_GAP = 1000_000_000
N = 200_000

for i in range(1):
    random.seed(i)

    house_positions = random.choices(range(MAX_GAP), k=N)
    house_positions.sort()

    C = random.randint(2, N)

    min_gap = choconaga2110.solve(house_positions, C)