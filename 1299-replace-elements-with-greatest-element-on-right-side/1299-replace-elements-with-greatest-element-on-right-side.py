class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp_max = -1
        arr_size_decr = len(arr) - 1
        for i in range(arr_size_decr, -1, -1):
            if arr[i] > temp_max:
                temp_max, arr[i] = arr[i], temp_max
            else:
                arr[i] = temp_max
        return arr