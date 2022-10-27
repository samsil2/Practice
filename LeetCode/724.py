from typing import List
"""
sums all the numbers
as left=right, total - (2*left) = pivot
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for pivot in range(len(nums)):
            if nums[pivot]== total - (2*left):
                return pivot
            left=left+nums[pivot]
        return -1


nums= [1,7,3,6,5,6]
s= Solution()
print(s.pivotIndex(nums))