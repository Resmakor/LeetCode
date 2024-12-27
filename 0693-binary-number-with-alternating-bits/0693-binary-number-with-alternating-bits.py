class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(bin(n).lstrip('0b'))
        for i in range(len(n) - 1):
            if i != len(n) - 1:
                if n[i] == n[i + 1]:
                    return False
        return True

        
         