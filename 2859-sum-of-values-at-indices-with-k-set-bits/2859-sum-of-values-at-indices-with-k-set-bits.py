class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        for i in range(len(nums)):
            bin_num = bin(i).strip("0b")
            if bin_num.count("1") == k:
                output += nums[i]
        return output
            