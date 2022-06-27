def solution(n, results):
    order = [[False] * n for _ in range(n)]
    for a in range(n):
        order[a][a] = True
    for a, b in results:
        order[a-1][b-1] = True
    for k in range(n):
        for a in range(n):
            for b in range(n):
                order[a][b] |= order[a][k] and order[k][b]
    
    answer = 0
    
    for a in range(n):
        for b in range(n):
            if not order[a][b] and not order[b][a]:
                break
        else:
            answer += 1
    
    return answer
