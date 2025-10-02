class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_distance = max(nums)
        for num in nums:
            if abs(num) < min_distance:
                min_distance = abs(num)
        if min_distance in nums:
            return min_distance
        return min_distance * (-1)