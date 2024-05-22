class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        str_num = str(num)
        reversed_1 = str_num[::-1].lstrip('0')
        return reversed_1 == str_num[::-1]
                
        