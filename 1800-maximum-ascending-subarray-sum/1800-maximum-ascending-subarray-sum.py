class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output, current_sum = 0, 0
        nums_size = len(nums)
        for i in range(nums_size - 1):
            current_sum += nums[i]
            if nums[i] >= nums[i + 1]:
                if output < current_sum:
                    output = current_sum
                current_sum = 0
        if current_sum + nums[-1] > output:
            return current_sum + nums[-1]
        return output
                