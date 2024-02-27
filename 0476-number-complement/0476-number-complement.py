class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(bin(num).replace("0b", "")))
        for i in range (len(num)):
            if (num[i] == '0'):
                num[i] = "1"
            else:
                num[i] = "0"
        num = "".join(num)
        num = int(num, 2)
        return num