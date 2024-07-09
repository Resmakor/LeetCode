class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        nums_size = len(nums)
        output = 0
        for i in range(0, nums_size):
            for j in range(i + 1, nums_size):
                for k in range(j + 1, nums_size):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        output += 1
        return output
        