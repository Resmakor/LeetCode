class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        output = 0
        for jewel in jewels:
            output += stones.count(jewel)
        return output