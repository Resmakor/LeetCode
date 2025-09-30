class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitwise_or = 0
        for num in nums:
            if num % 2 == 0:
                bitwise_or |= num
        return bitwise_or