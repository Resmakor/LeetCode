class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        base_7, minus = "", False
        if num < 0:
            minus = True
            num = abs(num)
        while num != 0:
            base_7 = str(num % 7) + base_7
            num //= 7
        if minus:
            return '-' + base_7
        return base_7