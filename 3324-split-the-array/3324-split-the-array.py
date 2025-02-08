from collections import Counter
class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        frequencies = Counter(nums)
        for value in frequencies.values():
            if value > 2:
                return False
        return True