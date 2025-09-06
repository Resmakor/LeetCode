from collections import Counter
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        count = Counter(moves)
        return abs(count['_'] - min(count['L'], count['R']) + max(count['L'], count['R']))