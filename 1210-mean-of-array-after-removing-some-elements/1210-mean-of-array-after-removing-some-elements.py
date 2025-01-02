class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        removed_elements = 0.05 * len(arr)
        counter = 0
        while counter < removed_elements:
            arr.remove(min(arr))
            counter += 1
        counter = 0
        while counter < removed_elements:
            arr.remove(max(arr))
            counter += 1
        return sum(arr) / float(len(arr))