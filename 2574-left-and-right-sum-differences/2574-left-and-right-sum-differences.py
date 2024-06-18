class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            answer.append(abs(sum(nums[0:i]) - sum(nums[i + 1:])))
        return answer
            