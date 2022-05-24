import sys
sys.stdin=open("input.txt", "rt")

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

# 삽입정렬
# 메모리초과
for i in range(1,len(nums)):
    for j in range(i,0,-1):
        if nums[j] < nums[j-1]:
            nums[j],nums[j - 1] = nums[j - 1],nums[j]
        else:
            break
for k in nums:
    print(k)