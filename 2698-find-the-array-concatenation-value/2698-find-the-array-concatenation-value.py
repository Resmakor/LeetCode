class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_div_2 = len(nums) // 2
        output = 0
        for i in range(len_div_2):
            if i < len_div_2:
                output += int(str(nums[i]) + str(nums[len(nums) - 1 - i]))
        if len(nums) % 2 == 1:
            return output + nums[len_div_2]
        return output