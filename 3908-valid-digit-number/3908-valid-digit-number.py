class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str_n = str(n)
        str_x = str(x)
        return str_n[0] != str_x and str_x in str_n