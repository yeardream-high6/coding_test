def solution(progresses, speeds):
    if not progresses or not speeds:
        return []

    end_times = [(100 - progress - 1) // speed + 1
                for progress, speed in zip(progresses, speeds)]

    answer = []

    iterator = iter(end_times)

    last_release_time = next(iterator)
    curr_release_cnt = 1

    for end_time in iterator:
        if end_time <= last_release_time:
            curr_release_cnt += 1
        else:
            answer.append(curr_release_cnt)
            last_release_time = end_time
            curr_release_cnt = 1

    answer.append(curr_release_cnt)

    return answer
