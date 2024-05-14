class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        while True:
            if num[-1] == '0':
                num = num[:-1]
            else:
                return num