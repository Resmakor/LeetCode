class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ones = []
        counter = 0
        while n >= counter:
            bin_number = str(bin(counter).replace("0b", ""))
            ones.append(bin_number.count('1'))
            counter += 1
        return ones
            
        