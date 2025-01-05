from collections import Counter
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output, counter = [], Counter(digits)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    if counter[i] > 0 and counter[j] > (i == j) and counter[k] > (k == i) + (k == j):
                        output.append(i * 100 + j * 10 + k)
        return output