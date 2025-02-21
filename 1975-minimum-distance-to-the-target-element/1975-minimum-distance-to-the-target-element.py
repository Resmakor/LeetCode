class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        output = len(nums)
        for index, num in enumerate(nums):
            if num == target and abs(index - start) < output:
                output = abs(index - start)
        return output