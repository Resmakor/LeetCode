class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        output = ""
        for x in n:
            if x == '0':
                continue
            else:
                output += x
        return int(output)