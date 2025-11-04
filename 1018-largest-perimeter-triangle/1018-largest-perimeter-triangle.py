class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums_size = len(nums)
        for i in range(nums_size - 1, 1, -1):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if a + b > c:
                return a + b +c
        return 0