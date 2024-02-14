class Solution(object):
    def fib(self, n):
        a = 0
        b = 1
        if n == 0:
            return a
        if n == 1:
            return b
        counter = 1
        while (counter != n):
            tmp = b
            b += a
            a = tmp
            counter += 1
        return b
        