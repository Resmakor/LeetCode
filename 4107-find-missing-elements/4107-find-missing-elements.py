class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minim, maxim = min(nums), max(nums)
        return sorted(list(set(range(minim, maxim)).difference(set(nums))))