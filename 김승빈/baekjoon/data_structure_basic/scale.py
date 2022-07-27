# 음계 문제 - 배열, 구현
# https://www.acmicpc.net/problem/2920
# python3로 제출이 안되는 경우 pypy3로 변경하기
a = list(map(int,input().split(" ")))

ascending = True
descending = True

for i in range(1,8):
    if a[i-1] < a[i]:
        descending = False
    elif a[i-1] > a[i]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")