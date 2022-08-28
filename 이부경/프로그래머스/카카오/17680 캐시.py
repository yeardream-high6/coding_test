from collections import deque

def solution(cacheSize, cities):
    time = 0
    dq = deque()
    cities = [city.lower() for city in cities]
    for i, city in enumerate(cities):
        if city in dq:
            time += 1
            dq.remove(city)
        else:
            time += 5

        if cacheSize > 0:
            dq.append(city)
        if len(dq) > cacheSize:
            dq.popleft()

    return time