class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        substring_nums = [int(num_str[i: i + k]) for i in range(len(num_str) - k + 1)]
        count = 0
        for n in substring_nums:
            if n and num % n == 0:
                count += 1
        return count
        

answer = Solution().divisorSubstrings(num = 240, k = 2)
print(answer)

answer = Solution().divisorSubstrings(num = 430043, k = 2)
print(answer)