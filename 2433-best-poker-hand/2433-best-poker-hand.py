class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if suits.count(suits[0]) == 5:
            return 'Flush'
        pair = False
        for rank in ranks:
            if ranks.count(rank) >= 3:
                return 'Three of a Kind'
            elif ranks.count(rank) == 2:
                pair = True
        return 'Pair' if pair else 'High Card'