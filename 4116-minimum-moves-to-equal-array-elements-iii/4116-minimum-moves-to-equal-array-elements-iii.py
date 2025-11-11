class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output, maxim = 0, max(nums)
        for num in nums:
            output += maxim - num
        return output