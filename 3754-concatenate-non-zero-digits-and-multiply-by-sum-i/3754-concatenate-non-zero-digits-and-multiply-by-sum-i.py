class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        for num in str(n):
            if str(num) != '0':
                x += str(num)
        if x == "":
            return 0
        x = int(x)
        sum_of_digits = sum([int(el) for el in str(x)])
        return x * sum_of_digits