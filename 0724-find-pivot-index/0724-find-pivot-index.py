class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum, right_sum = 0, sum(nums)
        for index, element in enumerate(nums):
            right_sum -= element
            if left_sum == right_sum:
                return index
            left_sum += element
        return -1