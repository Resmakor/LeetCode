class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        range_set = set(range(left, right + 1))
        for arr_range in ranges:
            arr_range = set(range(arr_range[0], arr_range[1] + 1))
            range_set = range_set.difference(arr_range)
            if len(range_set) == 0:
                return True
        return False