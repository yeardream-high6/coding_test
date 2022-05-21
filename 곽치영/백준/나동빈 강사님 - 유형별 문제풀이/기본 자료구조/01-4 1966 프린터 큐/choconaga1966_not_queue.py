import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    index = 0
    order = 1
    curr_max = max(priorities)
    while curr_max > 0:    
        if priorities[index] == curr_max:
            if index == M:
                break
            priorities[index] = 0 # 출력한 것은 0으로 바꿈
            order += 1
            curr_max = max(priorities)
            
        index = (index + 1) % len(priorities) # 순환
    
    print(order)