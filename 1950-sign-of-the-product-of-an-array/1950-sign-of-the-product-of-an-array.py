class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 1
        for num in nums:
            if num == 0:
                output = 0
                break
            elif num > 0:
                output *= 1
            else:
                output *= -1
        return output