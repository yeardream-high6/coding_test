import heapq as hq
from math import sqrt
import sys

def minimum_spanning_tree(dist):
    n = len(dist)
    min_dist = [None] * n
    not_visited = [True] * n
    min_dist[0] = 0
    not_visited[0] = False
    net_dist = 0
    for i in range(n):
        min_dist[i] = dist[0][i]
    for _ in range(1, n):
        min_idx = None
        min_value = None
        for i in range(n):
            if not_visited[i] and (min_value == None or min_value > min_dist[i]):
                min_idx = i
                min_value = min_dist[i]

        not_visited[min_idx] = False
        net_dist += min_value
        #print(min_idx, min_value)

        for j in range(n):
            if not_visited[j]:
                min_dist[j] = min(min_dist[j], dist[min_idx][j])
    return net_dist


input = sys.stdin.readline

n, m = map(int, input().split())

x = [None] * n
y = [None] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

dist = [
    [
        sqrt((x[a]-x[b])**2 + (y[a]-y[b])**2)
        for b in range(n)
    ]
    for a in range(n)
]
#print(dist)

for _ in range(m):
    a, b = map(int, input().split())
    dist[a-1][b-1] = 0
    dist[b-1][a-1] = 0

print(f'{minimum_spanning_tree(dist):.2f}')
