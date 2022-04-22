import sys
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[0] + people[-1] > limit:
            people.pop()
            answer += 1
        else:
            people.popleft()
            people.pop()
            answer += 1
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 50, 80, 50,90],100))
print(solution([50,70,70, 50, 80, 50,90],100))