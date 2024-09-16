class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        key = ""
        num1, num2, num3 = str(num1), str(num2), str(num3) 
        num1 = '0' * (4 - len(num1)) + num1
        num2 = '0' * (4 - len(num2)) + num2
        num3 = '0' * (4 - len(num3)) + num3
        for i in range(4):
            key += min(num1[i], num2[i], num3[i])
        if key == "0000":
            return 0
        return int(key.lstrip('0'))
        