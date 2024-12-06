class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            if len(nums) == 1:
                return nums[0]
            newNums, flag_min = [], True
            for i in range(0, len(nums), 2):
                if flag_min:
                    newNums.append(min(nums[i], nums[i + 1]))
                    flag_min = False
                else:
                    newNums.append(max(nums[i], nums[i + 1]))
                    flag_min = True
            nums = newNums