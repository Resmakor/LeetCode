class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        maximum = max(nums)
        for element in nums:
            if element != minimum and element != maximum:
                return element
        return -1