class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights_size = len(heights)
        old_heights = list(heights)
        heights.sort()
        differences = 0
        for i in range(heights_size):
            if old_heights[i] != heights[i]:
                differences += 1
        return differences