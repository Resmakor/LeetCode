class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_size = len(nums)
        triplets = []
        for i in range(nums_size - 2):
            for j in range(i + 1, nums_size - 1):
                for k in range(j + 1, nums_size):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        triplets.append(nums[i] + nums[j] + nums[k])
        if len(triplets) == 0:
            return -1
        return min(triplets)