class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = nums.pop(0) + nums.pop(0)
        operations = 1
        while len(nums) >= 2:
            curr_score = nums.pop(0) + nums.pop(0)
            if score == curr_score:
                operations += 1
            else:
                return operations
        return operations