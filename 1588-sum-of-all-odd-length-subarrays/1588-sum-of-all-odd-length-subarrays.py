class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_size = len(arr)
        output = 0
        for i in range(1, arr_size + 1, 2):
            for j in range(arr_size - i + 1):
                output += sum(arr[j:j + i])
        return output