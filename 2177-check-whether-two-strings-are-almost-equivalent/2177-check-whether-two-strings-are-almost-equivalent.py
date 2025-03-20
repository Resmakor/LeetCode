from collections import Counter
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        for key in c1:
            if key not in c2:
                if c1[key] > 3:
                    return False
            if abs(c1[key] - c2[key]) > 3:
                return False
        for key in c2:
            if key not in c1:
                if c2[key] > 3:
                    return False
            if abs(c1[key] - c2[key]) > 3:
                return False
        return True