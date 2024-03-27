class Solution(object):
    def bin_to_dec(self, bin):
        """
        :type bin: str
        :rtype: int
        """
        power_of_2 = 1
        dec = 0
        for digit in bin[::-1]:
            if digit == '1':
                dec += power_of_2
            power_of_2 *= 2
        return dec
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bin = str(bin(n)).replace("0b", "") 
        n_complement = ""
        for digit in n_bin:
            if digit == '1':
                n_complement += '0'
            else:
                n_complement += '1'
        return self.bin_to_dec(n_complement)
            