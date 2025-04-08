class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        while True:
            if len(nums) == len(list(set(nums))):
                return output
            else:
                nums = nums[3:]
                output += 1