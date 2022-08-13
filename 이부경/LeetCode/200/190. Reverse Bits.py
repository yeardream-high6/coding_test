class Solution:
    def reverseBits(self, n: int) -> int:
        #return int(bin(n)[2:].zfill(32)[::-1], 2)
        output = 0
        for _ in range(32):
            output <<= 1
            output |= n & 1
            n >>= 1
        return output
