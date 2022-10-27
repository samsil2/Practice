class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        # i -> index, num -> value

        for i, num in enumerate(nums):
            if i == 0:
                ans.append(num)
            else:
                ans.append(ans[i - 1] + nums[i])

        return ans