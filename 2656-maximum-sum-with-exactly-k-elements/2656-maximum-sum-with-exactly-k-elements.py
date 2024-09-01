class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        for i in range(k):
            max_sum = max(nums)
            index = nums.index(max_sum)
            nums[index] = max_sum + 1
            output += max_sum
        return output