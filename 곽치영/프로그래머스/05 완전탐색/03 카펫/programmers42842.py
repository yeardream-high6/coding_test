# a = 1
# b = w + h = brown / 2 + 2
# c = w * h = brown + yellow
# (x - w)(x - h) = x^2 - (w+h)x + wh = 0
# x = [b ± √(b^2 - 4ac)] /2

import math

def solution(brown, yellow):
    b = brown // 2 + 2
    c = brown + yellow
    sqrt_part = math.isqrt(b*b - 4*1*c)
    return [(b + sqrt_part) //2, (b - sqrt_part) //2]
