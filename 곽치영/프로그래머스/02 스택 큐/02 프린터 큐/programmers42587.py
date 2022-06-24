# 100은 작으니까 쉽게 쉽게 하자 (큐 안씀)

def solution(priorities, location):
    index = 0
    order = 1
    curr_max = max(priorities)
    while curr_max > 0:    
        if priorities[index] == curr_max:
            if index == location:
                return order
            priorities[index] = 0 # 출력한 것은 0으로 바꿈
            order += 1
            curr_max = max(priorities)

        index = (index + 1) % len(priorities) # 순환
