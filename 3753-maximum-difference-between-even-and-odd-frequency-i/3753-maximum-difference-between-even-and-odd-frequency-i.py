from collections import Counter
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = Counter(s)
        odd, even = [], []
        for key in frequency:
            if frequency[key] % 2 == 0:
                even.append(frequency[key])
            else:
                odd.append(frequency[key])
        return max(odd) - min(even)
    