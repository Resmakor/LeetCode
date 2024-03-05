class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = []
        for element in nums:
            new_nums.append(element ** 2)
        new_nums.sort()
        return new_nums