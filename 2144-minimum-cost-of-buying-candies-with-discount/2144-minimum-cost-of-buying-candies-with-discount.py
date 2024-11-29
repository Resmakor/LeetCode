class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        output = 0
        for i in range(0, len(cost), 3):
            if i + 1 < len(cost):
                output += cost[i] + cost[i + 1]
            else:
                output += cost[i]
        return output