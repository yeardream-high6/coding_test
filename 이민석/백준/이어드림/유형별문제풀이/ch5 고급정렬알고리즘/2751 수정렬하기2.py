import sys
sys.stdin=open("input.txt", "rt")

#시간초과
"""
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

# 삽입정렬
for i in range(1,len(nums)):
    for j in range(i,0,-1):
        if nums[j] < nums[j-1]:
            nums[j],nums[j - 1] = nums[j - 1],nums[j]
        else:
            break
for k in nums:
    print(k)


"""

#강사코드
"""
n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

for x in data:
    print(x)

"""