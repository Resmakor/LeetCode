class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) > max_diff:
                max_diff = abs(nums[i] - nums[i + 1])
        if abs(nums[0] - nums[-1]) > max_diff:
            return abs(nums[0] - nums[-1])
        return max_diff