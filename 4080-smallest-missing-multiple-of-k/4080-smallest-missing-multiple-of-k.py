class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        search = k
        for num in nums:
            if num > search:
                return search
            if num == search:
                search += k
        return search