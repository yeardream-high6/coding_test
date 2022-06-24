def solution(prices):
    answer = [None] * len(prices)

    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            pop_ind = stack.pop()
            answer[pop_ind] = i - pop_ind
            #print(f"p[{pop_ind}] > p[{i}] 이라서 answer[{pop_ind}] = {i - pop_ind}")
        stack.append(i)
    while stack:
        pop_ind = stack.pop()
        answer[pop_ind] = (len(prices)-1) - pop_ind
        #print(f"p[{pop_ind}]는 끝까지 가서 answer[{pop_ind}] = {(len(prices)-1) - pop_ind}")
    return answer
