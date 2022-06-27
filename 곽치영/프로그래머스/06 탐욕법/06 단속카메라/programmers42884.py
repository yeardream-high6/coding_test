# 이 문제도 다른사람 풀이를 보니 route[1]로 정렬하면 더 쉽게 풀 수 있는 문제네요.

def solution(routes):
    routes = sorted(routes)
    n = len(routes)

    min_out_after = [None] * n
    curr_min_out = routes[-1][1]
    for i in range(-1, -n-1, -1):
        curr_out = routes[i][1]
        if curr_min_out > curr_out:
            curr_min_out = curr_out
        min_out_after[i] = curr_min_out
    
    i = 0
    num_camera = 0

    while True:
        num_camera += 1
        camera_pos = min_out_after[i]
        while i < n:
            if routes[i][0] > camera_pos:
                break
            i += 1
        else:
            break
    
    return num_camera

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))