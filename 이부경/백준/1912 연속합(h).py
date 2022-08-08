N = int(input())
nums = list(map(int,input().split()))

total = nums[0]
temp_total = nums[0]
for i in range(1, len(nums)):
    temp_total += nums[i]
    if temp_total < nums[i]:
        temp_total = nums[i]
    if total < temp_total:
        total = temp_total

print(total)