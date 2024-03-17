class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = str(n)
        reversed_n = str(n[::-1])
        n_with_separator = ""
        for index, digit in enumerate(reversed_n):
            if (index % 3 == 0 and index != 0):
                n_with_separator = "." + n_with_separator
            n_with_separator = digit + n_with_separator
        return n_with_separator     