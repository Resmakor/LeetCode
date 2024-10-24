class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = []
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                output.append(len(set(nums[i:j])) ** 2)
        return sum(output)
                