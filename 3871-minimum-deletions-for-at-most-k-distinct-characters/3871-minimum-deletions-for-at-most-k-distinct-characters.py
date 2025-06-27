from collections import Counter
class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        output, distinct_chars = 0, len(set(list(s)))
        if distinct_chars == k: 
            return 0
        sorted_occurences = sorted(Counter(s).values())
        for i in range(distinct_chars - k):
            output += sorted_occurences[i]
        return output