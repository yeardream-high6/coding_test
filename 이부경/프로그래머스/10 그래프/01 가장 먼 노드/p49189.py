from collections import deque

def solution(n, edge):
    # 초기화
    distances = {} # 거리
    connections = {} # 연결 정보
    for a, b in edge:
        if a not in distances:
            distances[a] = 1e9
        if b not in distances:
            distances[b] = 1e9
        
        if a not in connections:
            connections[a] = set()
        if b not in connections:
            connections[b] = set()
        
        connections[a].add(b)
        connections[b].add(a)
    distances[1] = 0
    
    
    # 방문 한 적 없는 곳만 DFS 방식으로 순회
    visited = set()
    dq = deque()
    visited.add(1)
    dq.append(1)
    distance = 1
    while dq:
        u = dq.popleft()
        for v in connections[u]:
            distances[v] = min(distances[u] + distance, distances[v])
            if v not in visited:
                visited.add(v)
                dq.append(v)


    max_distance = 0
    for d in distances.values():
        max_distance = max(max_distance, d)

    # 가장 거리가 먼 노드의 개수 세기
    answer = len([x for x in distances if distances[x] == max_distance])
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])