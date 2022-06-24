from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    incompletion_count = participant_count - completion_count

    answer = incompletion_count.most_common(1)[0][0]

    return answer

import sys

if __name__ == '__main__':
    read_line = sys.stdin.readline
    N = int(read_line())
    participant = [None] * N
    completion = [None] * (N-1)
    for i in range(N):
        participant[i] = read_line().strip()
    for i in range(N-1):
        completion[i] = read_line().strip()
    print(solution(participant, completion))
