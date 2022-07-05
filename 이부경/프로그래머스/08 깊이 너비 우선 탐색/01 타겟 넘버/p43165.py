def f(numbers, target, sum, i):
    if i >= len(numbers):
        if target == sum:
            return 1
        else:
            return 0
        
    a = f(numbers, target, sum + numbers[i], i + 1)
    b = f(numbers, target, sum - numbers[i], i + 1)
    
    return a+ b
    
def solution(numbers, target):
    answer = f(numbers, target, 0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))