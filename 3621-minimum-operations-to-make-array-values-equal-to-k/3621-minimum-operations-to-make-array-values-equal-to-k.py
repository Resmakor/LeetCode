class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return -1 if min(nums) < k else len(set(nums).difference({k}))