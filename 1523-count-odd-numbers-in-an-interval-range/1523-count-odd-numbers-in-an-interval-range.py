class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        integers = high - low + 1
        if low % 2 == 1:
            return int(math.ceil(integers / 2.0))
        else:
            return integers / 2