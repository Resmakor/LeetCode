class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_collection, output = set(), 0
        for element in nums[::-1]:
            output += 1
            if element > 0 and element <= k and element not in current_collection:
                current_collection.add(element)
                if len(current_collection) == k:
                    return output