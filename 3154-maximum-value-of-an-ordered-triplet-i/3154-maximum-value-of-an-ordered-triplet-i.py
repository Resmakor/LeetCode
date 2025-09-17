class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        max_diff, max_value, max_result = 0, nums[0], 0
        for i in range(1, len(nums)):
            max_result = max(max_result, max_diff * nums[i])
            max_diff = max(max_diff, max_value - nums[i])
            max_value = max(max_value, nums[i])
        return max_result