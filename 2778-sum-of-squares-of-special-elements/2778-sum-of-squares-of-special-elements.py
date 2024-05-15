class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_size = len(nums)
        output = 0
        for i in range(len(nums)):
            if n_size % (i + 1) == 0:
                output += nums[i] * nums[i]
        return output
        