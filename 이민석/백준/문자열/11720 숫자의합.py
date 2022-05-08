import sys
sys.stdin=open("input.txt", "rt")
n = input()
nums = list(input())
sum = 0
for i in nums:
    sum += int(i)
print(sum)