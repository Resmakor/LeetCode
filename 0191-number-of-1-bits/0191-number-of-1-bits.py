class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(bin(n)).lstrip("0b")
        return n.count("1")
        
        