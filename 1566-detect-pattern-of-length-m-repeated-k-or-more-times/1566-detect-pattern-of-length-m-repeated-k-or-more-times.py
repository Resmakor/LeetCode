class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(len(arr) - 1):
            temp = arr[i:i + m]
            if temp * k == arr[i:i + m * k]:
                return True
        return False