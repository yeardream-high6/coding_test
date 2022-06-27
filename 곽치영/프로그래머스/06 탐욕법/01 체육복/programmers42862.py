def solution(n, lost, reserve):
    set_lost = set(lost)
    set_reserve = set(reserve)
    lost = sorted(set_lost - set_reserve)
    reserve = sorted(set_reserve - set_lost)
    len_reserve = len(reserve)

    reserve_i = 0
    answer = n - len(lost)
    for lost_idx in lost:
        while reserve_i < len_reserve and reserve[reserve_i] < lost_idx - 1:
            reserve_i += 1
        if not reserve_i < len_reserve:
            break
        if reserve[reserve_i] <= lost_idx + 1:
            reserve_i += 1
            answer += 1
    return answer
