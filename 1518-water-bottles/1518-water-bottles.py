class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        output = 0
        full, empty = numBottles, 0
        while full + empty >= numExchange:
            output += full
            current_bottles = empty + full
            empty, full = current_bottles % numExchange, current_bottles // numExchange
        return output + full