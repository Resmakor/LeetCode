class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_of_substrings = []
        for i in range(len(s) - 1):
            list_of_substrings.append(s[i] + s[i + 1])
        for substring in list_of_substrings:
            if substring in s[::-1]:
                return True
        return False