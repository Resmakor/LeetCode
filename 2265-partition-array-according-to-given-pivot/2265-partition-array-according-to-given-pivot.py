class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left_arr, pivots, right_arr = [], [], []
        for element in nums:
            if element < pivot:
                left_arr.append(element)
            elif element == pivot:
                pivots.append(element)
            else:
                right_arr.append(element)
        return left_arr + pivots + right_arr