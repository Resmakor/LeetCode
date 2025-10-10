class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        break_index = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                break_index = i + 1
                break
        if break_index == -1:
            return 0
        for i in range(break_index + 1, n - 1):
            if nums[i] > nums[i + 1]:
                return -1
        if nums[n - 1] > nums[0]:
            return -1
        return n - break_index
        