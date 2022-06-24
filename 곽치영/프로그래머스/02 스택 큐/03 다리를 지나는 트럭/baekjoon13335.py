from collections import deque

def solution(bridge_length, weight, truck_weights):
    curr_time = 0
    curr_weight = 0

    que = deque()

    for truck_weight in truck_weights:

        curr_time += 1

        while not curr_weight + truck_weight <= weight:

            curr_time = que[0][0]
            curr_weight -= que[0][1]
            #print(f"t:{curr_time:>3} w:{curr_weight:>3} pop {que[0][1]}")
            que.popleft()

        curr_weight += truck_weight
        #print(f"t:{curr_time:>3} w:{curr_weight:>3} append {truck_weight}")

        # (end_time, weight)
        que.append((curr_time + bridge_length, truck_weight))

        if que[0][0] == curr_time:
            curr_weight -= que[0][1]
            #print(f"t:{curr_time:>3} w:{curr_weight:>3} pop {que[0][1]}")
            que.popleft()

    answer = que[-1][0]
    return answer

import sys
read_line = sys.stdin.readline

num_trucks, bridge_length, weight = map(int, read_line().split())
truck_weights = map(int, read_line().split())
print(solution(bridge_length, weight, truck_weights))
