class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        averages = set()
        while len(nums) > 0:
            minim, maxim = min(nums), max(nums)
            averages.add((minim + maxim) / 2.0)
            nums.remove(minim)
            nums.remove(maxim)
        return len(averages)