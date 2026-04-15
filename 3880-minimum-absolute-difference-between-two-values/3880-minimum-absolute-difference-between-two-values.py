class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        prevNum, prevIndex, minim = 0, 0, inf
        for index, num in enumerate(nums):
            if num == 0:
                continue
            if prevNum + num == 3 and minim > index - prevIndex:
                minim = index - prevIndex
            prevNum, prevIndex = num, index
        if minim != inf:
            return minim
        return -1