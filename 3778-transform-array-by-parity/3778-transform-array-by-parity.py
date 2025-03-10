class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                count_even += 1
        return [0] * count_even + [1] * (len(nums) - count_even)