class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for i in range(len(nums)):
            output += sum(nums[max(0, i - nums[i]):i + 1])
        return output