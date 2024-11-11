class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_size = len(nums)
        output = 0
        for i in range(nums_size):
            for j in range(i, nums_size):
                for k in range(j, nums_size):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        output += 1
        return output