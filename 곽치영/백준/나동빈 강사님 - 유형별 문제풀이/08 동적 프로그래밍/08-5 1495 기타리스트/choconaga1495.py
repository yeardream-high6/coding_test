import sys
import heapq as hq

input = sys.stdin.readline

N, S, M = map(int, input().split())
volume_diffs = list(map(int, input().split()))
possible_volumes = [S]

for v_diff in volume_diffs:
    down_volume = (v - v_diff for v in possible_volumes if v - v_diff >= 0)
    up_volume = (v + v_diff for v in possible_volumes if v + v_diff <= M)
    new_volumes = []
    prev = None

    # drop duplicates
    for volume in hq.merge(down_volume, up_volume):
        if prev != volume:
            prev = volume
            new_volumes.append(volume)
    
    possible_volumes = new_volumes

#print(possible_volumes)
print(max(possible_volumes) if possible_volumes else -1)
