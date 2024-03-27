class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decomp_list = []
        for i in range(0, len(nums), 2):
            decomp_list += nums[i] * [nums[i + 1]]
        return decomp_list