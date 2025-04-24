class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                bitOR = nums[i] | nums[j]
                if bitOR % 2 == 0:
                    return True
        return False