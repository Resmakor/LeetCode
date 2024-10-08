class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, element in enumerate(nums):
            temp_sum = 0
            for digit in str(element):
                temp_sum += int(digit)
            if index == 0:
                output = temp_sum
            elif temp_sum < output:
                output = temp_sum
        return output