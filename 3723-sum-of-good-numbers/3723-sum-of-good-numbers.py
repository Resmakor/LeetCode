class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        n = nums
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(n):
                if nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                    output += nums[i]
            elif i - k >= 0 and i + k >= len(n):
                if nums[i] > nums[i - k]:
                    output += nums[i]
            elif i - k < 0 and i + k < len(n):
                if nums[i] > nums[i + k]:
                    output += nums[i]
            elif i - k < 0 and i + k >= len(n):    
                output += nums[i]
        return output
