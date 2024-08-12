class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        points = []
        for element in nums:
            points.extend(range(element[0], element[1] + 1))
        return len(list(set(points)))