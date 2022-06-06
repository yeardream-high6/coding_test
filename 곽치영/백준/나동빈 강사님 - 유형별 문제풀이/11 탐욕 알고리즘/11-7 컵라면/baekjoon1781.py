import sys
read_line = sys.stdin.readline

N = int(read_line())

# (reward, deadline) list
problems = [None] * N

for i in range(N):
    deadline, reward = map(int, read_line().split())
    problems[i] = (reward, deadline)

# reward 순 정렬
problems.sort(reverse=True)

last_free_time = [None] * (N+1)

sum_reward = 0

for prob in problems:
    reward, deadline = prob

    # deadline 이전 가장 마지막 빈 시간 찾기
    time = deadline
    while last_free_time[time] is not None:
        time = last_free_time[time]
    free_time = time

    # 경로 압축
    time = deadline
    while last_free_time[time] is not None:
        last_free_time[time], time = free_time, last_free_time[time]
    
    # 가장 마지막 빈 시간에 문제 배정
    if free_time > 0:
        sum_reward += reward
        last_free_time[free_time] = free_time - 1

print(sum_reward)
