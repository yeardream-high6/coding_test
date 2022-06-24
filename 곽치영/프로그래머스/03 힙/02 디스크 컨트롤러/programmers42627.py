# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리한다.
# 1. 따라서 귀납적으로 각 시점에 디스크가 휴식하는지 여부는 작업순서와 무관하게 결정된다.
# 2. 각 시점에 가장 짧은 작업부터 수행하는 게 최적이다.
#   - 왜냐하면 다른 작업을 수행했다면 언젠가 가장 짧은 작업을 수행하게 되고 (1)에 의해
#     두 수행 사이에는 휴식이 없다. 따라서 두 작업의 순서를 바꾸면 대기시간이 무조건 좋아진다.

from heapq import heappush, heappop


def solution(jobs):

    n = len(jobs)
    jobs.sort()
    print(jobs)

    # (task_size, index)
    size_heap = []

    i = 0
    end_time = 0
    total = 0

    while True:
        if i < n:
            job = jobs[i]
            if end_time >= job[0]:
                heappush(size_heap, (job[1], i))
                i += 1
            else:
                if size_heap:
                    (size, idx) = heappop(size_heap)
                    end_time += size
                    total += end_time - jobs[idx][0]
                    #print(f"{i}: {jobs[idx][0]} - {end_time}")
                else:
                    end_time = job[0]
                    heappush(size_heap, (job[1], i))
                    i += 1
        else:
            if size_heap:
                (size, idx) = heappop(size_heap)
                end_time += size
                total += end_time - jobs[idx][0]
                #print(f"{i}: {jobs[idx][0]} - {end_time}")
            else:
                break

    return total // n
