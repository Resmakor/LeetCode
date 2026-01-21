class Solution:
    def isFascinating(self, n: int) -> bool:
        n_2 = 2 * n
        n_3 = 3 * n
        string = str(n) + str(n_2) + str(n_3)
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for char in string:
            if char == '0' or char not in digits:
                return False
            digits.remove(char)
        return True