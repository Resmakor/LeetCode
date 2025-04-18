class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(bin(n).lstrip('0b'))
        counter = 0
        output = 0
        for i in range(len(n)):
            if n[i] == '1':
                if counter > output:
                    output = counter
                counter = 1
            else:
                counter += 1
        return output