class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minim, max_diff = nums[0], -1
        for i in range(1, len(nums)):
            if nums[i] > minim:
                max_diff = max(max_diff, nums[i] - minim)
            else:
                minim = nums[i]
        return max_diff
