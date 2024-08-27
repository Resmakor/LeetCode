class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages  = []
        for i in range(len(nums) // 2):
            minimum = min(nums)
            nums.remove(minimum)
            maximum = max(nums)
            nums.remove(maximum)
            averages.append((minimum + maximum) / 2.0)
        return min(averages)