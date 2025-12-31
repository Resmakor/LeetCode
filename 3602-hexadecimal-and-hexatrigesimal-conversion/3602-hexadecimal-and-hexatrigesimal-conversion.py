class Solution:
    def __init__(self):
        self.base36_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def decToAny(self, n: int, base: int) -> str:
        output = ""
        while n > 0:
            remainder = n % base
            output = self.base36_chars[remainder] + output
            n //= base
        return output

    def concatHex36(self, n: int) -> str:
        n_2 = n * n
        n_3 = n_2 * n
        hexadecimal_str = self.decToAny(n_2, 16)
        hexatrigesimal_str = self.decToAny(n_3, 36)
        return hexadecimal_str + hexatrigesimal_str
