def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        bin1 = bin(a1)[2:].zfill(n)
        bin2 = bin(a2)[2:].zfill(n)
        
        line = []
        for b1, b2 in zip(bin1, bin2):
            line.append('#' if int(b1) | int(b2) else ' ')
        answer.append(''.join(line))
        
    return answer