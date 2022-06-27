def solution(array, commands):
    answer = []
    for i, j, k in commands:
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])
    return answer
