class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maks_1 = 0
        maks_1_index = 0
        maks_2 = 0
        for index, element in enumerate(nums):
            if element > maks_1:
                maks_1 = element
                maks_1_index = index
        for index, element in enumerate(nums):
            if element > maks_2 and maks_1_index != index:
                maks_2 = element
        return (maks_1 - 1) * (maks_2 - 1)