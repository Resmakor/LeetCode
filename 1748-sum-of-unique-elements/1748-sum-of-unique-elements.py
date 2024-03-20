class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums = {}
        for element in nums:
            dict_nums[element] = 0
        for element in nums:
            dict_nums[element] += 1
        dict_sum = 0
        for key, value in dict_nums.items():
            if value == 1:
                dict_sum += key
        return dict_sum
        