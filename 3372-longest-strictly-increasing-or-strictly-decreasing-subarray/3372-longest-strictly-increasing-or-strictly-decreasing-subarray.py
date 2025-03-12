class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        incr, decr, maxim = 1, 1, 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                incr += 1
                decr = 1
            elif nums[i] < nums[i + 1]:
                decr += 1
                incr = 1
            else:
                incr, decr = 1, 1
            maxim = max(maxim, max(incr, decr))
        return maxim