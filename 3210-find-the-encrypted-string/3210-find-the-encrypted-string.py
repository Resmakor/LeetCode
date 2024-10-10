class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output, s_size = "", len(s)
        for i in range(s_size):
            output += s[(i + k) % s_size]
        return output