class Solution:
    def __init__(self):
        self.value_to_char = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 
            20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 
            30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
        }

    def decToAny(self, n: int, base: int) -> str:
        output = ""
        while n > 0:
            remainder = n % base
            output = self.value_to_char[remainder] + output
            n //= base
        return output

    def concatHex36(self, n: int) -> str:
        n_2 = n * n
        n_3 = n_2 * n
        hexadecimal_str = self.decToAny(n_2, 16)
        hexatrigesimal_str = self.decToAny(n_3, 36)
        return hexadecimal_str + hexatrigesimal_str
