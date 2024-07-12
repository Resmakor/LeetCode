class Solution(object):
    def GCD(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.GCD(max(nums), min(nums))