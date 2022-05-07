line = input()

def sol2(line):
    count = {}
    for c in line:
        c = c.upper()
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    sorted_pair = sorted(count.items(), key=lambda x: -x[1])
    
    if len(sorted_pair) == 1 or sorted_pair[0][1] != sorted_pair[1][1]:
        return sorted_pair[0][0]
    else:
        return '?'

print(sol2(line))