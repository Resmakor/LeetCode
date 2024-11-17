class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            new_nums = nums[0:i] + nums[i + 1:]
            flag = True
            for j in range(len(new_nums) - 1):
                if new_nums[j] >= new_nums[j + 1]:
                    flag = False
                    break
            if flag:
                return True
        return False