class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum_list = []
        running_sum = 0
        for element in nums:
            running_sum += element
            running_sum_list.append(running_sum)
        return running_sum_list
            