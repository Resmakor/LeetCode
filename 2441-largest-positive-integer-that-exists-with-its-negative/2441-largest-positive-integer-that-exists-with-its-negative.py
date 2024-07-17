class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[-1 - i] < 0:
                return -1
            elif nums[-1 - i] * (-1) in nums:
                return nums[-1 - i]
        return -1