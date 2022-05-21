import sys

MAX_GAP = 1000_000_000

def greedy(house_positions, gap_lower_bound, C=None):
    """
    처음부터 공유기 사이의 거리가 gap_lower_bound 이상 되도록 greedy하게 집을 선택했을 때
    최대 공유기 갯수와, 가장 가까운 두 공유기 사이의 거리를 구한다. (최대 C개 까지만)
    """
    cnt = 1
    last_idx = 0
    min_gap = MAX_GAP
    for i in range(1, len(house_positions)):
        gap = house_positions[i] - house_positions[last_idx]
        if gap >= gap_lower_bound:
            cnt += 1
            last_idx = i
            if min_gap > gap:
                min_gap = gap
            if C is not None and cnt == C:
                return C, min_gap, last_idx
    else:
        return cnt, min_gap, last_idx

def solve(house_positions, C):
    house_positions.sort()

    lower_bound = 0
    upper_bound = MAX_GAP

    while lower_bound < upper_bound:
        mid = (upper_bound - lower_bound) // 2 + lower_bound
        cnt, possible_distance, _ = greedy(house_positions, mid, C)

        #print(lower_bound, upper_bound, mid, cnt, possible_distance)

        if cnt < C:
            upper_bound = mid
        elif lower_bound < possible_distance:
            lower_bound = possible_distance
        else:
            return lower_bound


if __name__ == '__main__':
    input = sys.stdin.readline

    N, C = map(int, input().split())
    house_positions = [None] * N
    for i in range(N):
        house_positions[i] = int(input())
    
    print(solve(house_positions, C))
