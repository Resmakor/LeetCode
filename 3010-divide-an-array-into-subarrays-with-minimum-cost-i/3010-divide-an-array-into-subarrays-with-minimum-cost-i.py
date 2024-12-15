class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_num = nums[0]
        nums = sorted(nums[1:])
        return first_num + nums[0] + nums[1]

        