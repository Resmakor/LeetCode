class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        sorted_freq = {}
        output = 0
        for domino in dominoes:
            sorted_domino = tuple(sorted(domino))
            if sorted_domino in sorted_freq.keys():
                sorted_freq[sorted_domino] += 1
            else:
                sorted_freq[sorted_domino] = 1
        for domino in sorted_freq:
            if sorted_freq[domino] > 1:
                output += math.factorial(sorted_freq[domino]) / (2 * math.factorial(sorted_freq[domino] - 2))
        return output