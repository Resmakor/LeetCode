class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_operations_counter = 0
        for element in nums:
            if element < k:
                min_operations_counter += 1
        return min_operations_counter