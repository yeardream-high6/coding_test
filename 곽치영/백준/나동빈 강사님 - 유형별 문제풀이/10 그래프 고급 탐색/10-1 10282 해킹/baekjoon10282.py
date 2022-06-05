import heapq as hq
import sys

def infect(trusted, c):
    n = len(trusted)

    # (infected_time, computer_idx)
    time_pqueue = []
    infected_time = [None] * n

    infected_time[c] = 0
    hq.heappush(time_pqueue, (0, c))
    
    while time_pqueue:
        b_infected_time, b = hq.heappop(time_pqueue)
        if b_infected_time > infected_time[b]:
            #print(f'skip time: {b_infected_time} b: {b}')
            continue
        #print(f'time: {b_infected_time} b: {b}')

        for a, s in trusted[b]:
            a_infected_time = b_infected_time + s
            if infected_time[a] is None or infected_time[a] > a_infected_time:
                infected_time[a] = a_infected_time
                hq.heappush(time_pqueue, (a_infected_time, a))

    return infected_time


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    c = c-1
    trusted = [[] for _ in range(n)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        a, b = a-1, b-1
        trusted[b].append((a, s))
    
    infected_time = infect(trusted, c)

    infected_num = len(infected_time) - infected_time.count(None)
    max_infected_time = max(infected_time, key=lambda t: -1 if t is None else t)

    print(infected_num, max_infected_time)
