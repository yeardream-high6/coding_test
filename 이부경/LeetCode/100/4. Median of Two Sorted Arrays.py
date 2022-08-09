from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        total_len = len(nums1) + len(nums2)
        i = total_len // 2
        if total_len % 2:
            return nums[i]
        else:
            return (nums[i - 1] + nums[i]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        odd = (m + n) % 2
        middle = (m + n - 1) // 2

        ret = sorted(nums1+nums2)
            
        if odd:
            return ret[middle]
        else:
            return (ret[middle] + ret[middle + 1]) / 2        

nums1 = [1,3]
nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]
answer = Solution().findMedianSortedArrays(nums1, nums2)
print(answer)