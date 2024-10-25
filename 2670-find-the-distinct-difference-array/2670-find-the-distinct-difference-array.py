class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            prefix = set(nums[:i + 1])
            suffix = set(nums[i + 1:])
            output.append(len(prefix) - len(suffix))
        return output