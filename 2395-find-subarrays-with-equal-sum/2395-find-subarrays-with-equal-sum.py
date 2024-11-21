class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_size = len(nums)
        for i in range(nums_size):
            for j in range(i + 1, nums_size - 1):
                if nums[i] + nums[i + 1] == nums[j] + nums[j + 1]:
                    return True
        return False