class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output, zero_counter = [], 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        for num in nums:
            if num == 0:
                zero_counter += 1  
            else:
                output.append(num)
        output.extend([0] * zero_counter)
        return output