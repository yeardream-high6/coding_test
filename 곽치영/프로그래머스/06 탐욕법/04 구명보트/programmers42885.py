def solution(people, limit):
    people = sorted(people)

    left = 0
    right = len(people) - 1
    answer = 0

    while left < right:
        # 남아있는 가장 가벼운 사람과 탈 수 없으면 혼자 타야 한다.
        if people[left] + people[right] > limit:
            right -= 1
            answer += 1
        # 아니면 가장 가벼운사람과 가장 무거운 사람이 탄다.
        else:
            left += 1
            right -= 1
            answer += 1
    # 마지막에 혼자 남은 경우
    if left == right:
        answer += 1

    return answer


def solution2(people, limit):
    people = sorted(people)

    left = 0
    right = len(people) - 1
    answer = 0

    while left < right:
        # 가장 무거운 사람과 탈 수 있는 사람은 누구와도 탈 수 있다.
        # 따라서 해당 사람들은 서로 자리를 바꿔 탈 수 있다.
        # 따라서 아무나 태워도 상관 없다. 편의상 가장 가벼운 사람을 태운다.
        if people[left] + people[right] <= limit:
            left += 1
        # 가장 무거운 사람을 태운다.
        answer += 1
        right -= 1
    # 마지막에 혼자 남은 경우
    if left == right:
        answer += 1

    return answer
