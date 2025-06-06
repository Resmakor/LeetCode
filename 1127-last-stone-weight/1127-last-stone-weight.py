class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1] -= stones[-2]
                stones.pop(-2)
        if len(stones) == 1:
            return stones[0]
        return 0