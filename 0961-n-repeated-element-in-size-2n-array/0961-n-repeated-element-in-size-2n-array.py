class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        set_nums = set(nums)
        for element in set_nums:
            if nums.count(element) == n:
                return element