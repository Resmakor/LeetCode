class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == key and abs(i - j) <= k:
                    output.append(i)
                    break
        return output