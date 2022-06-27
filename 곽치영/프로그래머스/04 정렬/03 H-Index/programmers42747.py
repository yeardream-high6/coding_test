def solution(citations):
    citations = sorted(citations, reverse=True)
    for i, citation in enumerate(citations):
        if i+1 > citation:
            break
    else:
        i = len(citations)
    return i

solution([10] * 5)