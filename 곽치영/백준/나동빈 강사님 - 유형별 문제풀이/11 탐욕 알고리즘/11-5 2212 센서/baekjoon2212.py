import heapq as hq
import sys

# 인접한 센서의 거리 중 가장 큰 K-1개 만큼 절약 할 수 있다.
# iter_sensor는 정렬된 상태
def solve(K, iter_sensor):
    iter_sensor = iter(iter_sensor)
    prev = next(iter_sensor)

    min_pos = prev
    min_heap = []

    for pos in iter_sensor:
        diff = pos - prev
        prev = pos
        if len(min_heap) < K-1:
            hq.heappush(min_heap, diff)
        else:
            hq.heappushpop(min_heap, diff)
    
    max_pos = prev
    
    # min_heap에 남은 것이 가장 큰 K-1개 간격, N=1이면 비어있음
    saving = 0 if not min_heap else sum(min_heap)

    #print(f'{max_pos=} {min_pos=} {saving=}')
    return max_pos - min_pos - saving


if __name__ == '__main__':
    read_line = sys.stdin.readline

    N = int(read_line())
    K = int(read_line())

    sensors = sorted(map(int, read_line().split()))
    print(solve(K, sensors))
