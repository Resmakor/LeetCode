from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = Counter(text)
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])