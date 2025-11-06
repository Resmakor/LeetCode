class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        intersection = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                intersection += 1
        if nums[-1] > nums[0]:
            intersection += 1
        return intersection <= 1