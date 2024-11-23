class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = [0] * 26
        for character in s:
            alphabet[ord(character) - ord('a')] += 1
        for i in range(len(s)):
            if alphabet[ord(s[i]) - ord('a')] == 1:
                return i
        return -1