from collections import Counter
class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        frequency = Counter(str(n))
        min_frequency = min(frequency.values())
        potential_output = [x for x in frequency if frequency[x] == min_frequency]
        return int(min(potential_output))