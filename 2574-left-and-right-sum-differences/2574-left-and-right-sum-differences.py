class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        nums_size = len(nums)
        for i in range(nums_size):
            answer.append(abs(sum(nums[0:i]) - sum(nums[i + 1:])))
        return answer
            