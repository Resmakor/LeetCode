from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = Counter(s), Counter(t)
        for key in t:
            if key not in s.keys() or t[key] != s[key]:
                return key