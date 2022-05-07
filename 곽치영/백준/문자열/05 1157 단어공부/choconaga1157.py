line = input()

def sol(line):
    length = ord('Z') - ord('A') + 1
    count = [0] * length
    
    for c in line:
        count[ord(c.upper()) - ord('A')] += 1
    max_count = max(count)
    
    result = None
    
    for i in range(length):
        if count[i] == max_count:
            if result:
                return '?'
            result = chr(i + ord('A'))
            
    return result

print(sol(line))