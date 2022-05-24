import sys
sys.stdin=open("input.txt", "rt")

n,k = map(int,input().split())

nums = list(map(int, input().split()))
nums = sorted(nums)

print(nums[k-1])