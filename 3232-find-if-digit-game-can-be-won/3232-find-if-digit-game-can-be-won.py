class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_sum = 0
        double_sum = 0
        for element in nums:
            if element >= 10:
                double_sum += element
            else:
                single_sum += element
        return single_sum != double_sum