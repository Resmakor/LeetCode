class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if k <= numOnes:
            return k
        remaining_after_ones = k - numOnes
        if remaining_after_ones <= numZeros:
            return numOnes
        remaining_after_zeros = remaining_after_ones - numZeros
        return numOnes - remaining_after_zeros