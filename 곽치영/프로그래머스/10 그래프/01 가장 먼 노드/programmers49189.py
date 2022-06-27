from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n)]
    for i, j in edge:
        i, j = i-1, j-1
        adj_list[i].append(j)
        adj_list[j].append(i)
    
    
    visited = [False] * n
    
    # (node, dist)
    que = deque()
    que.append((0,0))
    visited[0] = True
    max_dist = 0
    max_count = 0
    while que:
        i, dist = que.popleft()
        if dist > max_dist:
            max_dist = dist
            max_count = 0
        max_count += 1
        for j in adj_list[i]:
            if not visited[j]:
                que.append((j, dist+1))
                visited[j] = True
    
    return max_count
