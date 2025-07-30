class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return int(str(nums[0]) + str(nums[1]))
        return int(str(nums[0]) + str(nums[-1])) + self.findTheArrayConcVal(nums[1:-1])