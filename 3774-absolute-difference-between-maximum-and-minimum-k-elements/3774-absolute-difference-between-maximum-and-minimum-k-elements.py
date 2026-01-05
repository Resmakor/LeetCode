class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        return abs(sum(nums[0:k]) - sum(nums[len(nums) - k: len(nums)]))