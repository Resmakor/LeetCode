class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        array_size = len(nums)
        for i in range(array_size - 1):
            if nums[i] == nums[i + 1]:
                counter += 1
                nums[i + 1] += 1
            elif nums[i] > nums[i + 1]:
                counter += nums[i] - nums[i + 1] + 1
                nums[i + 1] += nums[i] - nums[i + 1] + 1
        return counter
                
        