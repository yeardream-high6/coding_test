def solution(answers):
    
    score = [0,0,0]
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    pattern_length = [len(pattern) for pattern in patterns]
    
    for i, answer in enumerate(answers):
        for j in range(3):
            pattern = patterns[j]
            choice = pattern[i%len(pattern)]
            if choice == answer:
                score[j] += 1
    
    max_score = max(score)
    
    return [i for i in [1,2,3] if score[i-1] == max_score]
