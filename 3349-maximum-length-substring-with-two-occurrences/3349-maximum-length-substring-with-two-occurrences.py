from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = []
        for i in range(len(s)):
            for j in range(i + 1):
                substring, flag = s[j:len(s) - i + j], True
                counter = Counter(substring)
                for value in counter.values():
                    if value > 2:
                        flag = False
                        break
                if flag:
                    return len(substring)