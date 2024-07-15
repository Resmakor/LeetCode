class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        min_side_len = [min(rectangle) for rectangle in rectangles]
        max_side_len = max(min_side_len)
        return min_side_len.count(max_side_len)