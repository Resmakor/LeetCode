class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [element for element in nums if element != 0]
        return len(list(set(nums)))