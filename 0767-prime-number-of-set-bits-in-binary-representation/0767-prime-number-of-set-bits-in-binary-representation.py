class Solution(object):
    def isNotPrime(self, number):
        return 2 not in [number, pow(2, number, number)]
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        output = 0
        for i in range(left, right + 1, 1):
            set_bits = str(bin(i).lstrip('0b')).count('1')
            if not self.isNotPrime(int(set_bits)):
                output += 1
        return output
