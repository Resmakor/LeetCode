class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minim, maxim = min(nums), max(nums)
        output = 0
        for num in nums:
            if num > minim and num < maxim:
                output += 1
        return output
