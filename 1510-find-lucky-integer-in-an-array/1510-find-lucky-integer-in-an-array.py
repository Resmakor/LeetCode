from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_c, maxim = Counter(arr), -1
        for key in arr_c:
            if arr_c[key] == key:
                maxim = max(key, maxim)
        return maxim