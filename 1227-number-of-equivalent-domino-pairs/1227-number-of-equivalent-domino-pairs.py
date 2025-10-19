class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        sorted_freq = {}
        output = 0
        for domino in dominoes:
            if domino[0] > domino[1]:
                sorted_domino = tuple([domino[1], domino[0]])
            else:
                sorted_domino = tuple([domino[0], domino[1]])
            if sorted_domino in sorted_freq.keys():
                sorted_freq[sorted_domino] += 1
            else:
                sorted_freq[sorted_domino] = 1
        for domino in sorted_freq:
            if sorted_freq[domino] > 1:
                output += math.factorial(sorted_freq[domino]) / (2 * math.factorial(sorted_freq[domino] - 2))
        return output