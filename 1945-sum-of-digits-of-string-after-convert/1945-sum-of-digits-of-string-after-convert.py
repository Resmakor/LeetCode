class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        output = ""
        for element in s:
            output += str(ord(element) - 96)
        for i in range(k):
            output = sum([int(element) for element in str(output)])
        return output