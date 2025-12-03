class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output = ""
        rev = True
        for i in range(0, len(s), k):
            if rev:
                output += s[i:i + k][::-1]
                rev = False
            else:
                output += s[i:i + k]
                rev = True
        return output