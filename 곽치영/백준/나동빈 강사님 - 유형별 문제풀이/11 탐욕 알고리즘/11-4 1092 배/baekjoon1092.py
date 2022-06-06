from bisect import bisect_left

# O(M log N + N log N)
def solve(cranes, boxes):
    N = len(cranes)
    M = len(boxes)

    cranes.sort()

    num_boxes_by_crane = [0] * N

    # 상자를 들 수 있는 가장 약한 크레인에 추가
    for box in boxes:
        index = bisect_left(cranes, box)
        if index < N:
            num_boxes_by_crane[index] += 1
        else:
            # 들 수 없는 상자
            return -1
    
    #print(num_boxes_by_crane)

    cum_sum = 0
    max_min = 0
    for i in range(1, N+1):
        curr = num_boxes_by_crane[-i]
        if curr > 0:
            # 현재 크레인 이상의 제한을 가진 크레인에서 처리해야하는 상자의 수
            cum_sum += curr
            # 골고루 나눠 가질 때 최솟값
            min_time = (cum_sum - 1) // i + 1

            if max_min < min_time:
                max_min = min_time
    
    return max_min

import sys
read_line = sys.stdin.readline

N = int(read_line())
cranes = list(map(int, read_line().split()))

M = int(read_line())
boxes = list(map(int, read_line().split()))

print(solve(cranes, boxes))
