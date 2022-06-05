from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

def dijkstra(N, adj_dict, S):
    min_distance = [None] * N
    min_prev = [[] for _ in range(N)]
    pqueue = []

    # (S에서의 거리, 도착장소, 이전장소)
    hq.heappush(pqueue, (0, S, None))

    while pqueue:
        net_dist, curr, prev = hq.heappop(pqueue)

        if min_distance[curr] is None:
            min_distance[curr] = net_dist
            min_prev[curr].clear()
            min_prev[curr].append(prev)
            for next_, dist in adj_dict[curr].items():
                hq.heappush(pqueue, (net_dist + dist, next_, curr))
        elif min_distance[curr] == net_dist:
            min_prev[curr].append(prev)
        # else:
        #     assert min_distance[curr] < net_dist
    
    # 더미 None 제거
    min_prev[S].clear()

    return min_distance, min_prev

def remove_min_paths(N, adj_dict, D, min_prev):
    not_visited = [True] * N
    queue = deque()
    queue.append(D)
    not_visited[D] = False
    while queue:
        curr = queue.popleft()
        for prev in min_prev[curr]:
            del adj_dict[prev][curr]
            if not_visited[prev]:
                queue.append(prev)
                not_visited[prev] = False


def almost_min_distance(N, adj_dict, S, D):
    min_distance, min_prev = dijkstra(N, adj_dict, S)
    #print(min_distance, min_prev)

    remove_min_paths(N, adj_dict, D, min_prev)

    min_distance, min_prev = dijkstra(N, adj_dict, S)
    #print(min_distance, min_prev)
    return min_distance[D] if min_distance[D] is not None else -1

while True:
    N, M = map(int, input().split())
    if (N, M) == (0 ,0):
        break

    adj_dict = [{} for _ in range(N)]

    S, D = map(int, input().split())
    for _ in range(M):
        U, V, P = map(int, input().split())

        adj_dict[U][V] = P

    print(almost_min_distance(N, adj_dict, S, D))
