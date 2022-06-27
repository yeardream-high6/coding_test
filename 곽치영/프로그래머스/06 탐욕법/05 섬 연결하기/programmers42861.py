def solution(n, costs):
    cost = [[None] * n for _ in range(n)]
    for i, j, c in costs:
        cost[i][j] = c
        cost[j][i] = c
    
    add_cost = [None] * n
    added = [False] * n
    add_cost[0] = 0
    total_cost = 0

    for _ in range(n):
        min_add_cost = min(c for c in add_cost if c is not None)
        total_cost += min_add_cost
        i = add_cost.index(min_add_cost)
        add_cost[i] = None
        added[i] = True

        for j in range(n):
            if not added[j] and cost[i][j] is not None \
                and (add_cost[j] is None or add_cost[j] > cost[i][j]):
                add_cost[j] = cost[i][j]
    
    return total_cost
