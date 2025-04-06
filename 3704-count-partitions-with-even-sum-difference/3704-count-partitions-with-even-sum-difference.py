class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for i in range(1, len(nums)):
            if (sum(nums[0:i]) - sum(nums[i:])) % 2 == 0:
                output += 1
        return output