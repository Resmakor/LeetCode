from collections import Counter
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        words_count = len(words)
        words = ''.join(words)
        counter = Counter(words)
        for key in counter.keys():
            if counter[key] % words_count != 0:
                return False
        return True