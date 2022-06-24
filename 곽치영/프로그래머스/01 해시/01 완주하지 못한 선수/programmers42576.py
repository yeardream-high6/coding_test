from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    incompletion_count = participant_count - completion_count

    answer = incompletion_count.most_common(1)[0][0]

    return answer