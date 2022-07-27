# 블랙잭 = 배열, 완전 탐색
# 카드 중 3개를 뽑는 모든 경우의 수는 C(n,3)이며, n은 최대 100 => n(n-1)(n-2)/3!
# python은 1초에 최대 2000만 개의 연산 가능하므로 단순히 3중 반복문으로 모든 경우의 수를 확인하여 문제 해결 가능


n,m = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))

result = 0
length = len(data)

for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_num = data[i] + data[j] + data[k]
            if sum_num <= m:
                result = max(result, sum_num)
print(result)  