from collections import defaultdict
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(list(set(arr)))
        mapped = defaultdict(list)
        output = []
        for index, element in enumerate(sorted_arr):
            mapped[element] = index + 1
        for element in arr:
            output.append(mapped[element])
        return output
