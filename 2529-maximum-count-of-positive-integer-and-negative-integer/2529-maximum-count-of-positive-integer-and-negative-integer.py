class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = 0
        pos = 0
        for element in nums:
            if element < 0:
                neg += 1
            elif element > 0:
                pos += 1
        return max(neg, pos)
                