class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minim = min(nums) + k
        maxim = max(nums) - k
        return max(maxim - minim, 0)