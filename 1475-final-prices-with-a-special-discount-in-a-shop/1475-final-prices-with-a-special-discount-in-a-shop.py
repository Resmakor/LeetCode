class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        output = []
        i = 0
        while i != len(prices):
            added = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    output.append(prices[i] - prices[j])
                    added = True
                    break
            if not added:
                output.append(prices[i])
            i += 1
        return output
            