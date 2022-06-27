def solution(name):
    n = len(name)

    cost_dict = {chr(ord('A') + i): i for i in range(0, 13+1)}
    cost_dict.update({chr(ord('Z') - (i-1)): i for i in range(1, 12+1)})
    vertical_cost = sum(map(cost_dict.get, name))

    best_horizontal_cost = n - 1

    i = 1
    start_A = None
    for i in range(1, n+1):
        if i < n and name[i] == 'A':
            if start_A is None:
                start_A = i
        else:
            if start_A is not None:
                stop_A = i
                horizontal_cost = min(
                    (start_A-1) * 2 + (n-stop_A),
                    (start_A-1) + (n-stop_A) * 2,
                )
                if best_horizontal_cost > horizontal_cost:
                    best_horizontal_cost = horizontal_cost
                
                start_A = None
    
    return vertical_cost + best_horizontal_cost

print(solution("JEROEN"))