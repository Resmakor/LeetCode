class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        pref_size = len(pref)
        counter = 0
        for word in words:
            if word[:pref_size] == pref:
                counter += 1
        return counter