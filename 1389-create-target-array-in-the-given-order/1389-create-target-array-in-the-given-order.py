class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(nums)):
            target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
        
        