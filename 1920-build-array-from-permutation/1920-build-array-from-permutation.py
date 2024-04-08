class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        permutation = []
        for num in nums:
            permutation.append(nums[num])
        return permutation