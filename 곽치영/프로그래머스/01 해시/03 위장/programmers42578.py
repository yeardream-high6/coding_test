def solution(clothes):
    counter = {}
    for [_, part] in clothes:
        if part in counter:
            counter[part] += 1
        else:
            counter[part] = 1
    answer = 1
    for part, count in counter.items():
        answer *= count + 1
    answer -= 1
    return answer
