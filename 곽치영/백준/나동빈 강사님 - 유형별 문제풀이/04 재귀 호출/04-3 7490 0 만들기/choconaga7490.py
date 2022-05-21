import sys
input = sys.stdin.readline

T = int(input())

for case_number in range(T):
    if case_number > 0:
        print()

    N = int(input())
    
    blank = ' '
    plus = '+'
    minus = '-'

    ops = [None] * N
    ops[0] = ''

    values = list(range(1, N+1))

    def get_formula(n):
        return ''.join(ops[i] + str(values[i]) for i in range(n))

    def recursive_step(i, accumulated_result, last_op, last_num):
        #print(f"{get_formula(i-1):<13} = {accumulated_result:<6d} {last_op} {last_num:<7}", end='')

        old_result = accumulated_result
        if last_op == plus:
            accumulated_result += last_num
        elif last_op == minus:
            accumulated_result -= last_num
        
        #print(f"= {accumulated_result}")

        if i < N:
            ops[i] = blank
            # N < 10
            recursive_step(i+1, old_result, last_op, last_num*10 + values[i])
            ops[i] = plus
            recursive_step(i+1, accumulated_result, plus, values[i])
            ops[i] = minus
            recursive_step(i+1, accumulated_result, minus, values[i])
        else:
            if accumulated_result == 0:
                print(get_formula(i))

    recursive_step(1, 0, plus, 1)