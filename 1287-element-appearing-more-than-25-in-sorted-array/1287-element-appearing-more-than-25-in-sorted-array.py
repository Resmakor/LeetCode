class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_size, arr_set = len(arr), set(arr)
        for element in arr_set:
            if float(arr.count(element)) / arr_size > 0.25:
                return element