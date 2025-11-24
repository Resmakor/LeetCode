class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        curr_value, output = "", []
        for num in nums:
            curr_value += str(num)
            output.append(int(curr_value, 2) % 5 == 0)
        return output