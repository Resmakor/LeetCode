class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output, current_position = 0, 0
        for num in nums:
            current_position += num
            if current_position == 0:
                output += 1
        return output
                