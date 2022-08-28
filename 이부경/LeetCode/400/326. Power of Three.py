from ensurepip import version


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n /= 3
        return n == 1
n = 3 ** 19
print(bin(n))
#3의 거듭 제곱은 약수가 3의 거듭제곱밖에 없으니까
#print((3 ** 19).bit_length())
#print((3 ** 20).bit_length())
# print((1).bit_count())
# print((2).bit_count())
# print((3).bit_count())
# print((4).bit_count())
# n.bit_count
print(version())

import sys
print(sys.version)