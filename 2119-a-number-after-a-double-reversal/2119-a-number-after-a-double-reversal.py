class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if num == 0 else str(num)[::-1].lstrip('0') == str(num)[::-1]
                
        