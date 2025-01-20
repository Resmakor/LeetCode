class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        output, min_diff = [], float("inf")
        arr.sort()
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                output = []
                output.append([arr[i], arr[i + 1]])
                min_diff = diff
            elif diff == min_diff:
                output.append([arr[i], arr[i + 1]])
        return output