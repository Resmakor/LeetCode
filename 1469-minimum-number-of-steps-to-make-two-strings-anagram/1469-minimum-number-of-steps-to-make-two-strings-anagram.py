from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        output = 0
        s_counter, t_counter  = Counter(s), Counter(t)
        for key in s_counter:
            if s_counter[key] > t_counter[key]:
                output += s_counter[key] - t_counter[key]
        return output
