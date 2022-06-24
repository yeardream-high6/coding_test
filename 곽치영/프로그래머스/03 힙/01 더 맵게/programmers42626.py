from heapq import heapify, heappop, heappush

def solution(scoville, K):
    N = len(scoville)

    heapify(scoville)

    for i in range(N-1):
        a = heappop(scoville)
        if a >= K:
            return i
        b = heappop(scoville)
        # print(a, b, a + 2 * b)
        heappush(scoville, a + 2 * b)

    a = heappop(scoville)
    if a >= K:
        return N - 1
    else:
        return -1
