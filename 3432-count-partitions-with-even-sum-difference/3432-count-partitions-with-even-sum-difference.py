class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output, n = 0, len(nums)
        L = nums[0]
        R = sum(nums) - L
        for i in range(1, n):
            if (L - R) % 2 == 0:
                output += 1
            L += nums[i]
            R -= nums[i]
        return output